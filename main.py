from __future__ import absolute_import, print_function, unicode_literals
import sys
from ItemCollection import IsoHuntSearch, KickassSearch
from colorama import Fore, Style

current_query = ''
there_be_results = False


def main():
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
        search = KickassSearch(query)
        display_results(search.results)
    else:
        print ('Incorrect usage. Please use the format: hunt <search term>')

    return


def display_results(search_results):

    for item in search_results:
        print (Fore.RED + '---' + Fore.RESET)

        stat_string = (Fore.MAGENTA + 'Size: '
                       + Fore.RESET + item.filesize
                       + Fore.BLUE + Style.DIM + ' - ' + Style.NORMAL
                       + Fore.MAGENTA + 'Files: ' + Fore.RESET + item.files
                       + Fore.BLUE + Style.DIM + ' - ' + Style.NORMAL
                       + Fore.MAGENTA + 'S/L: '
                       + Fore.RESET + item.seeders
                       + Fore.YELLOW + '/'
                       + Fore.RESET + item.leechers)

        print (Fore.GREEN + item.title)
        print (stat_string)
        print (Fore.BLUE + item.link)

    print (Fore.RED + '---' + Fore.RESET)

if __name__ == '__main__':
    main()
