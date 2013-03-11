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


class IsoHuntItem(SearchItem):
    """Manipulates the results from ISO Hunt to a standard search item"""

    def __init__(self, item):
        """item is an array recieved from an ISO Hunt search"""
        self.title = self.noHtmlPlease(item['title'])
        self.category = item['category']
        self.filesize = item['size']
        self.files = str(item['files'])
        self.seeders = str(item['Seeds'])
        self.leechers = str(item['leechers'])
        self.link = item['link'].replace('\\', '')
