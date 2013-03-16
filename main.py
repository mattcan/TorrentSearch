from __future__ import absolute_import, print_function, unicode_literals
import sys
from ItemCollection import IsoHuntSearch, KickassSearch
from colorama import Fore, Style
from operator import attrgetter


def main():
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
        search = search_results(query)
        display_results(search)
    else:
        print ('Incorrect usage. Please use the format: hunt <search term>')

    return


def search_results(query_string):
    final_results = []
    final_results.extend(IsoHuntSearch(query_string).results)
    final_results.extend(KickassSearch(query_string).results)

    sorted_results = sorted(final_results,
                            key=attrgetter('seeders'),
                            reverse=True)

    return sorted_results[0:9]


def display_results(search_results):

    for item in search_results:
        print (Fore.RED + '---' + Fore.RESET)

        stat_string = (Fore.MAGENTA + 'Size: '
                       + Fore.RESET + item.filesize
                       + Fore.BLUE + Style.DIM + ' - ' + Style.NORMAL
                       + Fore.MAGENTA + 'Files: ' + Fore.RESET + item.files
                       + Fore.BLUE + Style.DIM + ' - ' + Style.NORMAL
                       + Fore.MAGENTA + 'S/L: '
                       + Fore.RESET + str(item.seeders)
                       + Fore.YELLOW + '/'
                       + Fore.RESET + str(item.leechers))

        print (Fore.GREEN + item.title)
        print (stat_string)
        print (Fore.BLUE + item.link)

    print (Fore.RED + '---' + Fore.RESET)

if __name__ == '__main__':
    main()
