"""
utils.py
-----------------------------------------
Utility functions for the
System Information Gatherer.

Author : I.P SINGH
Version: 2.0
"""

import os
import sys
import time
from datetime import datetime

try:
    from colorama import Fore, Style
    COLOR = True
except ImportError:
    COLOR = False


class Utils:

    @staticmethod
    def separator(length=70):
        """Print separator line."""
        print("=" * length)

    @staticmethod
    def small_separator(length=70):
        """Print small separator."""
        print("-" * length)

    @staticmethod
    def current_time():
        """Return current timestamp."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def clear_screen():
        """Clear terminal screen."""

        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def pause():
        """Pause program."""

        input("\nPress ENTER to continue...")

    @staticmethod
    def format_bytes(size):
        """
        Convert bytes to human readable format.
        """

        power = 1024
        unit = 0
        units = ["Bytes", "KB", "MB", "GB", "TB", "PB"]

        while size >= power and unit < len(units) - 1:
            size /= power
            unit += 1

        return f"{size:.2f} {units[unit]}"

    @staticmethod
    def progress_bar(seconds=3):
        """
        Display simple progress bar.
        """

        print("\nCollecting Information...\n")

        total = 40

        for i in range(total + 1):

            percent = int((i / total) * 100)

            bar = "█" * i + "-" * (total - i)

            sys.stdout.write(
                f"\r[{bar}] {percent}%"
            )

            sys.stdout.flush()

            time.sleep(seconds / total)

        print("\n")

    @staticmethod
    def success(message):

        if COLOR:
            print(Fore.GREEN + "[+] " + message + Style.RESET_ALL)
        else:
            print("[+] " + message)

    @staticmethod
    def warning(message):

        if COLOR:
            print(Fore.YELLOW + "[!] " + message + Style.RESET_ALL)
        else:
            print("[!] " + message)

    @staticmethod
    def error(message):

        if COLOR:
            print(Fore.RED + "[-] " + message + Style.RESET_ALL)
        else:
            print("[-] " + message)

    @staticmethod
    def info(message):

        if COLOR:
            print(Fore.CYAN + "[*] " + message + Style.RESET_ALL)
        else:
            print("[*] " + message)

    @staticmethod
    def print_dictionary(data, indent=0):
        """
        Pretty-print nested dictionaries.
        """

        spacing = " " * indent

        if isinstance(data, dict):

            for key, value in data.items():

                if isinstance(value, (dict, list)):

                    print(f"{spacing}{key}")

                    Utils.print_dictionary(
                        value,
                        indent + 4
                    )

                else:

                    print(
                        f"{spacing}{key}: {value}"
                    )

        elif isinstance(data, list):

            for item in data:

                Utils.print_dictionary(
                    item,
                    indent + 4
                )
                