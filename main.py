import sys
from newegg_search import *
from universal_methods import *
#---------------------------------------------------------#
# Main function
#---------------------------------------------------------#
def main():
    search = create_search(sys.argv)
    print(search)

    data = newegg_search(search)
    for i in data:
        print(f'{i[0]} || {i[1]}')


#Calls main function
if __name__ == '__main__':
    main()