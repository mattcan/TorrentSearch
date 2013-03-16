from bs4 import BeautifulSoup


class SearchItem:
    """Abstract class representing a search item"""

    # attributes for the SearchItem
    title = ''
    link = ''
    category = ''
    filesize = ''
    files = ''
    seeders = ''
    leechers = ''

    def __init__(self, item):
        pass

    def noHtmlPlease(self, text_to_strip):
        return ''.join(BeautifulSoup(text_to_strip).findAll(text=True))

    def str_to_int(self, value):
        if value == '':
            return 0
        else:
            return int(value)


class IsoHuntItem(SearchItem):
    """Manipulates the results from ISO Hunt to a standard search item"""

    def __init__(self, item):
        """item is an array recieved from an ISO Hunt search"""
        self.title = self.noHtmlPlease(item['title'])
        self.category = item['category']
        self.filesize = item['size']
        self.files = str(item['files'])
        self.seeders = self.str_to_int(item['Seeds'])
        self.leechers = self.str_to_int(item['leechers'])
        self.link = item['link'].replace('\\', '')


class PirateBayItem(SearchItem):
    """Builds a Search Item from TPB request data"""

    def __init__(self, item):
        """item is an array of the torrent data"""
        pass


class KickassItem(SearchItem):
    """Builds a search item that is kick ass"""

    def __init__(self, item, base_url):
        """item is html string to parse"""
        soup = BeautifulSoup(item.encode(), "lxml")

        torrentName = soup.find('div', 'torrentname')

        self.title = torrentName.find('a', 'normalgrey').text
        self.category = 'N/A'
        self.filesize = soup.find('td', 'nobr').text
        self.files = soup.find('td', 'nobr').next_sibling.next_sibling.string
        self.seeders = self.str_to_int(soup.find('td', 'green').text)
        self.leechers = self.str_to_int(soup.find('td', 'red').text)
        self.link = base_url + torrentName.find('a', 'torType')['href']
