from SearchItem import IsoHuntItem, KickassItem
from bs4 import BeautifulSoup
import ast
import requests
import re


class Query(object):
    """Abstract class for looking up a query"""

    def __init__(self, query_string):
        self.rows_to_get = 10
        self.last_retrieved_row = 0
        self.results = []
        self.query = query_string

    def __build_url(self, query_string):
        pass

    def __get_results(self):
        pass


class IsoHuntSearch(Query):
    """Searches ISO Hunt for given string"""

    __base_url = 'http://isohunt.com/js/json.php?'

    def __init__(self, query_string):
        super(IsoHuntSearch, self).__init__(query_string)
        self.results = self.__get_results()

    def __build_url(self):
        url_query = 'ihq=' + self.query
        url_firstrow = '&start=' + str(self.last_retrieved_row)
        url_rows = '&rows=' + str(self.rows_to_get)

        url = self.__base_url + url_query + url_firstrow + url_rows

        return url

    def __get_results(self):

        url = self.__build_url()
        r = requests.get(url)
        req_results = ast.literal_eval(r.text)
        results = []

        #print req_results['items']
        for item in req_results['items']['list']:
            results.append(IsoHuntItem(item))

        return results


class PirateBaySearch(Query):
    """Searches TPB for torrents"""

    def __init__(self, query_string):
        pass


class KickassSearch(Query):
    """Searches kat.ph for torrents"""

    __base_url = "http://kat.ph"

    def __init__(self, query_string):
        super(KickassSearch, self).__init__(query_string)
        self.results = self.__get_results()

    def __build_url(self):
        return self.__base_url + "/search/" + self.query + "/"

    def __get_results(self):
        items = self.__parse_items()
        results = []

        for i in items:
            results.append(KickassItem(i, self.__base_url))

        return results

    def __parse_items(self):
        html = requests.get(self.__build_url())
        soup = BeautifulSoup(html.text, "lxml")
        pattern = re.compile('torrent_*')

        return [tr for tr in soup.find_all('tr', id=pattern)]
