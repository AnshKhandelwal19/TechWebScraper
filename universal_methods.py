#---------------------------------------------------------#
# Takes system arguments and creates search string
# If arguments are empty, it will ask for user input
# Returns a string : 'item+key+words'
#---------------------------------------------------------#
def create_search(src):
    search = ''
    if len(src) > 1:
        for i in range(1, len(src)-1, 1):
            search += src[i]
            search += '+'
        search += src[len(src)-1]
    else:
        print('Search Key Words: ')
        search = input()
    return search