# -*- coding: utf-8 -*-
"""Query the https://portal.dnb.de/opac.htm service for
German ISBN metadata. There is a Search/Retrieve via URL service:
http://www.dnb.de/EN/Service/DigitaleDienste/SRU/sru_node.html
that returns an XML entry, but it requires registration"""

import logging
import re
from isbnlib.dev import stdmeta
from isbnlib.dev._bouth23 import u
from isbnlib.dev.webquery import query as wquery

UA = 'isbnlib (gzip)'
SERVICE_URL = 'https://portal.dnb.de/opac.htm?method=showFullRecord&currentResultId="{isbn}"%26any&currentPosition=0'
LOGGER = logging.getLogger(__name__)


def parser_dnb(data):
    """Parse the response from the DNB service. The input data is the result webpage in html from the search."""
    data = re.split('<tr>', data)  # split rows in table into lines for loop
    recs = {}
    recs['Authors'] = []
    try:
        for line in data:
            line = line.replace('\n', ' ').replace('\t', '')
            if len(recs) == 5:  # skip the rest of the file if we have all recs
                break
            # Author:
            #<td width="25%" ><strong>Person(en)</strong></td>
            #<td >Bayerl, Linda (Verfasser)<br/>Dengl, Sabine (Illustrator)</td></tr>
            # Sometimes they also contain an href on the name and sometimes they start with <td class='yellow'>
            elif re.search(r"<strong>Person.+</strong>", line):
                authors = re.findall('</td>(.*)</td', line)[0]
                authors = authors.replace('<td >', '')
                authors = re.split('<br/>', authors)  # several authors?
                for auth in authors:
                    if 'href' in auth:  # name contains link
                        auth = re.findall(r'<a href=".*" >(.*)</a>', auth)[0]
                    # Remove job description in brackets after the name:
                    auth = u(re.sub(r'\(.*?\)', '', auth))
                    recs['Authors'].append(auth)
            # Publisher:
            #<strong>Verlag</strong></td><td >Hamburg : Carlsen</td>
            #</tr><tr><td width="25%" class='yellow'><strong>...
            elif re.search(r"<strong>Verlag</strong>", line):
                publisher = re.findall('td .*>(.*)</td', line)[0]
                # get only the publisher's name
                if ':' in publisher:
                    publisher = publisher.split(':')[1].strip()
                recs['Publisher'] = u(publisher)
            # Title:
            #<td width="25%" class='yellow'><strong>Titel</strong>
            #</td><td class='yellow'>Kindergartenblock - Verbinden, vergleichen, Fehler finden ab 4 Jahre / Linda Bayerl</td></tr>
            elif re.search(r"<strong>Titel</strong", line):
                title = re.findall('td .*>(.*)/.*</td', line)[0]
                title = u(title.replace('td >', '').replace('</td', ''))
                recs['Title'] = u(title)
            # Publication year:
            #<td width="25%" class='yellow'><strong>Zeitliche Einordnung</strong>
            #</td><td class='yellow'>Erscheinungsdatum: 2015</td></tr>
            elif re.search(r"<strong>Zeitliche Einordnung</strong", line):
                recs['Year'] = u(re.findall(r'\d{4}', line)[0])
            # Language:
            #<tr><td class="yellow" width="25%"> <strong>Sprache(n)</strong>
            #</td> <td class="yellow"> Deutsch (ger) </td></tr>
            #</td> <td class="yellow"> Englisch (eng), Neugriechisch (gre) </td></tr>
            elif re.search(r"<strong>Sprache\(n\)</strong", line):
                # There can be more than one language, so match all possible cases:
                langs = re.findall(r'>* \((.*?)\)', line)  # list of matches
                language = ','.join(langs)
                recs['Language'] = u(language)
            elif line == '':
                continue

    except IndexError:
        LOGGER.debug('Check the parsing for German DNB (possible error!)')
    try:
        # delete almost empty records
        if not recs['Title'] and not recs['Authors']:
            recs = {}
    except KeyError:
        recs = {}
    return recs


def _mapper(isbn, records):
    """Make records canonical.
    canonical: ISBN-13, Title, Authors, Publisher, Year, Language
    """
    # handle special case
    if not records:  # pragma: no cover
        return {}
    # add ISBN-13
    records['ISBN-13'] = u(isbn)
    # call stdmeta for extra cleaning and validation
    return stdmeta(records)


def query(isbn):
    """Query the German DNB service for metadata. """
    data = wquery(
        SERVICE_URL.format(isbn=isbn), user_agent=UA, parser=parser_dnb)
    if not data:  # pragma: no cover
        LOGGER.debug('No data from DNB for isbn %s', isbn)
        return {}
    return _mapper(isbn, data)
