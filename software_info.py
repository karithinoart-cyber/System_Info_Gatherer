"""
software_info.py
----------------------------------------------------
Software Information Module

Collects:
- Installed Software (Windows Registry)
- Installed Python Packages
- Python Runtime Information

Author : I.P SINGH
Version : 2.0
"""

import platform
import subprocess
import sys

try:
    import winreg
except ImportError:
    winreg = None


class SoftwareInfo:
    """Collect software information."""

    @staticmethod
    def get_python_information():
        """
        Return Python runtime information.
        """
        return {
            "Python Version": platform.python_version(),
            "Implementation": platform.python_implementation(),
            "Compiler": platform.python_compiler(),
            "Build": platform.python_build(),
            "Executable": sys.executable,
        }

    @staticmethod
    def get_installed_python_packages():
        """
        Return installed pip packages.
        """
        packages = []

        try:
            output = subprocess.check_output(
                [sys.executable, "-m", "pip", "list"],
                text=True
            )

            lines = output.splitlines()[2:]

            for line in lines:
                parts = line.split()

                if len(parts) >= 2:
                    packages.append({
                        "Package": parts[0],
                        "Version": parts[1]
                    })

        except Exception as error:
            packages.append({
                "Error": str(error)
            })

        return packages

    @staticmethod
    def read_registry(root, path):
        """
        Read installed software from Windows Registry.
        """

        software = []

        try:
            key = winreg.OpenKey(root, path)
            count = winreg.QueryInfoKey(key)[0]

            for i in range(count):

                try:
                    subkey_name = winreg.EnumKey(key, i)
                    subkey = winreg.OpenKey(key, subkey_name)

                    name = ""
                    version = ""
                    publisher = ""

                    try:
                        name = winreg.QueryValueEx(
                            subkey,
                            "DisplayName"
                        )[0]
                    except FileNotFoundError:
                        pass

                    try:
                        version = winreg.QueryValueEx(
                            subkey,
                            "DisplayVersion"
                        )[0]
                    except FileNotFoundError:
                        pass

                    try:
                        publisher = winreg.QueryValueEx(
                            subkey,
                            "Publisher"
                        )[0]
                    except FileNotFoundError:
                        pass

                    if name:
                        software.append({
                            "Name": name,
                            "Version": version,
                            "Publisher": publisher
                        })

                except Exception:
                    continue

        except Exception:
            pass

        return software

    @staticmethod
    def get_installed_software():
        """
        Return installed software.
        """

        if platform.system() != "Windows":
            return [{
                "Message": "Installed software enumeration is supported on Windows only."
            }]

        if winreg is None:
            return [{
                "Message": "winreg module is unavailable."
            }]

        software = []

        registry_locations = [
            (
                winreg.HKEY_LOCAL_MACHINE,
                r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
            ),
            (
                winreg.HKEY_LOCAL_MACHINE,
                r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
            ),
            (
                winreg.HKEY_CURRENT_USER,
                r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
            )
        ]

        for root, path in registry_locations:
            software.extend(
                SoftwareInfo.read_registry(root, path)
            )

        # Remove duplicate entries
        unique = {}

        for item in software:
            unique[item["Name"]] = item

        return sorted(
            unique.values(),
            key=lambda x: x["Name"].lower()
        )

    @staticmethod
    def get_all_software_information():
        """
        Return all software information.
        """

        return {
            "Python Information":
                SoftwareInfo.get_python_information(),

            "Installed Python Packages":
                SoftwareInfo.get_installed_python_packages(),

            "Installed Software":
                SoftwareInfo.get_installed_software()
        }


if __name__ == "__main__":

    import json

    data = SoftwareInfo.get_all_software_information()

    print(json.dumps(data, indent=4))