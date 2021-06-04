import sys
import re


# --------------------------------------- User Interface --------------------------------------- #
def inp(message, *options, assign='', default=''):
    """
    Taken from the repository iocen-form
    https://github.com/iocen/iocen-form
    """
    __ass = ''
    __def = ''
    __opt = ''
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if not assign == '':
        __ass = f'{assign} = '
    if not default == '':
        __def = f'{ConsoleColors.blue}[Default: {default}] {ConsoleColors.end}\n'
    if not options == ():
        __opt = f"{ConsoleColors.bold}{ConsoleColors.red}" \
                f"(Type {', '.join([' for '.join(map(str, i)) for i in zip(letters, options)])})" \
                f"{ConsoleColors.end} "

    result = ''

    failed_attempt = 0
    max_failed_attempt = 10

    while result == '' or (__opt != '' and not result.upper() in letters[:len(options)]):
        result = input(f'\n{ConsoleColors.bold}{message}{ConsoleColors.end}\n{__opt}{__def}>>> {__ass}').strip()

        if result == '':
            if default != '':
                result = default.strip()
            else:
                failed_attempt += 1
                print(
                    f'{ConsoleColors.red}You cannot leave this field blank. {ConsoleColors.bold}({str(failed_attempt)} '
                    f'failed attempt)'
                    f'{ConsoleColors.end}')
        if __opt != '' and not result.upper() in letters[:len(options)]:
            failed_attempt += 1
            print(
                f'{ConsoleColors.red}Invalid input. You must select one from the options above. {ConsoleColors.bold}'
                f'({str(failed_attempt)} failed attempt){ConsoleColors.end}')

        if failed_attempt >= max_failed_attempt:
            print(f'{ConsoleColors.warning}Session has ended. Exiting application...{ConsoleColors.end}')
            sys.exit()

    if len(options) > 0:
        result = result.upper()

    return result


class ConsoleColors:
    header = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    warning = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


def drag_drop():
    filename = re.findall(r'([a-zA-Z]:/[^\\:*?\"><|]*?\.[\w:]+(?![\w.]))',
                          inp('Paste your file directory here.').replace('\\', '/').replace('//', '/'))

    return filename[0]
