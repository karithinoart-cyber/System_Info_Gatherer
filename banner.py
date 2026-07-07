"""
banner.py
Displays the application banner.
"""

from config import PROJECT_NAME, VERSION, AUTHOR, LINE

try:
    from colorama import init, Fore, Style

    init(autoreset=True)
    COLOR_ENABLED = True

except ImportError:
    COLOR_ENABLED = False


class Banner:

    @staticmethod
    def show():

        if COLOR_ENABLED:

            print(Fore.CYAN + LINE)
            print(Fore.GREEN + r"""
   _____           _                     _____        __
  / ____|         | |                   |_   _|      / _|
 | (___  _   _ ___| |_ ___ _ __ ___       | |  _ __ | |_ ___
  \___ \| | | / __| __/ _ \ '_ ` _ \      | | | '_ \|  _/ _ \
  ____) | |_| \__ \ ||  __/ | | | | |    _| |_| | | | || (_) |
 |_____/ \__, |___/\__\___|_| |_| |_|   |_____|_| |_|_| \___/
           __/ |
          |___/
""")

            print(Fore.YELLOW + f"{PROJECT_NAME} v{VERSION}")
            print(Fore.WHITE + f"Author : {AUTHOR}")
            print(Fore.CYAN + LINE)
            print(Style.RESET_ALL)

        else:

            print(LINE)
            print(PROJECT_NAME)
            print(f"Version : {VERSION}")
            print(f"Author  : {AUTHOR}")
            print(LINE)