from __future__ import absolute_import, print_function, unicode_literals
import sys
from ItemCollection import IsoHuntSearch
from colorama import Fore, Style

current_query = ''
there_be_results = False


def main():
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
        search = IsoHuntSearch(query)
        display_results(search.results)
    else:
        print ('Incorrect usage. Please use the format: hunt <search term>')

    return


def menu():
    print ('------------------')
    print ('  IsoHunt Search  ')
    print ('  --------------  ')
    print ('1. New Search')
    print ('2. Next page')
    print ('3. Previous page')
    print ('4. Exit')
    print ('------------------')

    return raw_input('> ')


def menu_handler():
    while(True):
        menu_result = menu()

        global there_be_results
        global last_grabbed_row
        global rows_to_get

        if menu_result == '1':
            last_grabbed_row = 0
            display_results()

        elif menu_result == '2':
            """ next page of results """
            if there_be_results:
                # get next set of results
                last_grabbed_row += 1 + rows_to_get
                if last_grabbed_row > 1000:
                    last_grabbed_row = 1000 - rows_to_get

                display_results(True)
            else:
                print ('You need to search for a torrent first')

        elif menu_result == '3':
            """ previous page of results """
            if there_be_results:
                # get previous results
                last_grabbed_row -= 1 - rows_to_get
                if last_grabbed_row < 0:
                    last_grabbed_row = 0

                display_results(True)
            else:
                print ('You need to search for a torrent first')

        elif menu_result == '4':
            print (Fore.YELLOW + 'Thanks for playing!' + Fore.RESET)
            return -1

        else:
            print ('The menu item you selected was not valid')


def get_search_query():
    print ('-----------------')
    print ('Enter search term')
    print ('-----------------')
    return raw_input('> ')


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
