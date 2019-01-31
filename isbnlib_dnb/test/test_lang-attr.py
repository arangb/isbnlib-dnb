#!/usr/bin/env python3.7

import re
import logging
LOGGER = logging.getLogger(__name__)

def test_parser_dnb(data):
    """Parse the response from the DNB service. The input data is the result webpage in html from the search."""
    # assert that languages occur in the test data
    assert re.search(r"<strong>Sprache\(n\)</strong", line) is not None
    # do what the parser does, this should be tested separately
    # and the code would need refactoring for that
    data = re.split('<tr>', data)  # split rows in table into lines for loop
    recs = {}
    recs['Authors'] = []
    recs['Title'] = ""
    try:
        for line in data:
            line = line.replace('\n', ' ').replace('\t', '')
            # print(line)
            if len(recs) == 5:  # skip the rest of the file if we have all recs
                break
            # Language:
            #<tr><td class="yellow" width="25%"> <strong>Sprache(n)</strong>
            #</td> <td class="yellow"> Deutsch (ger) </td></tr>
            elif re.search(r"<strong>Sprache\(n\)</strong", line):
                # this could be broken into smaller peaces to test separately
                language = re.findall(r'td.*>(.*)</td', line)[0].strip()
                assert language == "Deutsch (ger)"
                # recs['Language'] = u(language)
                recs['Language'] = language
    except IndexError:
        LOGGER.debug('Check the parsing for German DNB (possible error!)')
    return recs

def main():
    with open('test.html', 'r') as fh:
        data = fh.read()
    test_parser_dnb(data)

if __name__ == "__main__":
    main()
