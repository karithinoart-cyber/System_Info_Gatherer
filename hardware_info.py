"""
hardware_info.py
----------------------------------------------------
Hardware Information Module

Collects:
- CPU Information
- BIOS Information
- Motherboard Information
- Physical Memory
- Disk Drives

Author : I.P SINGH
Version : 2.0
"""

import json
import subprocess


class HardwareInfo:
    """Collect hardware information using PowerShell."""

    @staticmethod
    def run_powershell(command):
        """
        Execute a PowerShell command and return the output.
        """

        try:

            result = subprocess.run(
                [
                    "powershell",
                    "-NoProfile",
                    "-ExecutionPolicy",
                    "Bypass",
                    "-Command",
                    command
                ],
                capture_output=True,
                text=True
            )

            return result.stdout.strip()

        except Exception as e:

            return f"Error: {e}"

    @staticmethod
    def get_cpu_information():

        command = """
        Get-CimInstance Win32_Processor |
        Select-Object Name,Manufacturer,NumberOfCores,
        NumberOfLogicalProcessors,MaxClockSpeed |
        ConvertTo-Json
        """

        output = HardwareInfo.run_powershell(command)

        try:
            return json.loads(output)
        except:
            return output

    @staticmethod
    def get_bios_information():

        command = """
        Get-CimInstance Win32_BIOS |
        Select-Object Manufacturer,SMBIOSBIOSVersion,
        SerialNumber,ReleaseDate |
        ConvertTo-Json
        """

        output = HardwareInfo.run_powershell(command)

        try:
            return json.loads(output)
        except:
            return output

    @staticmethod
    def get_motherboard_information():

        command = """
        Get-CimInstance Win32_BaseBoard |
        Select-Object Manufacturer,Product,SerialNumber |
        ConvertTo-Json
        """

        output = HardwareInfo.run_powershell(command)

        try:
            return json.loads(output)
        except:
            return output

    @staticmethod
    def get_ram_information():

        command = """
        Get-CimInstance Win32_PhysicalMemory |
        Select-Object Manufacturer,Capacity,Speed,PartNumber |
        ConvertTo-Json
        """

        output = HardwareInfo.run_powershell(command)

        try:
            return json.loads(output)
        except:
            return output

    @staticmethod
    def get_disk_information():

        command = """
        Get-CimInstance Win32_DiskDrive |
        Select-Object Model,SerialNumber,Size,InterfaceType |
        ConvertTo-Json
        """

        output = HardwareInfo.run_powershell(command)

        try:
            return json.loads(output)
        except:
            return output

    @staticmethod
    def get_all_hardware_information():

        return {

            "CPU":
                HardwareInfo.get_cpu_information(),

            "BIOS":
                HardwareInfo.get_bios_information(),

            "Motherboard":
                HardwareInfo.get_motherboard_information(),

            "RAM":
                HardwareInfo.get_ram_information(),

            "Disk":
                HardwareInfo.get_disk_information()

        }


if __name__ == "__main__":

    print(json.dumps(
        HardwareInfo.get_all_hardware_information(),
        indent=4
    ))