import sys
import re

################################################################################################################################################
def join(iterator, seperator):
    it = map(str, iterator)
    seperator = str(seperator)
    string = next(it, '')
    for s in it:
        string += seperator + s
    return string
def inp(message, assign='', default='', *options):
    __ass = ''
    __def = ''
    __opt = ''
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') 

    if not assign == '': __ass = f'{assign} = '
    if not default == '': __def = f'{bcol.OKCYAN}[Default: {default}] {bcol.ENDC}'
    if not options == (): __opt = f"{bcol.BOLD}(Type {join([' for '.join(map(str, i)) for i in zip(letters, options)], ', ')}){bcol.ENDC}\n"

    result = ''

    failedAttempt = 0
    maxfailedAttempt = 10

    while result == '' or (__opt != '' and not result.upper() in letters[:len(options)]):
        result = input(f'\n{message}\n{__opt}>>> {__ass}{__def}').strip()

        if result == '':
            if default != '': result = default.strip()
            else: 
                failedAttempt += 1
                print(f'{bcol.FAIL}You cannot leave this field blank. {bcol.BOLD}({str(failedAttempt)} failed attempt){bcol.ENDC}')
        elif __opt != '' and not result.upper() in letters[:len(options)]:
            if default != '': result = default.strip()
            else: 
                failedAttempt += 1
                print(f'{bcol.FAIL}Invalid input. You must select one from the options above. {bcol.BOLD}({str(failedAttempt)} failed attempt){bcol.ENDC}')

        if failedAttempt >= maxfailedAttempt: 
            print(f'{bcol.WARNING}Session has ended. Exiting application...{bcol.ENDC}')
            sys.exit()

    return result
class bcol:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
################################################################################################################################################
def dragdrop():
    filename = re.findall(r'([a-zA-Z]:\/[^\\\:\*\?\"\>\<\|]*?\.[\w:]+(?![\w\.]))', inp('Drag and drop your file here').replace('\\', '/').replace('//', '/'))
    
    return filename[0]
