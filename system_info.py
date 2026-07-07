"""
system_info.py
----------------------------------------------------
System Information Module

Collects:
- Operating System Information
- Computer Information
- CPU Information
- Memory Information
- Disk Information
- Boot Time
- Uptime

Author : I.P SINGH
Version : 2.0
"""

import platform
import socket
import getpass
from datetime import datetime

import psutil


class SystemInfo:
    """Collect system information."""

    @staticmethod
    def get_basic_information():
        """Return basic system information."""

        uname = platform.uname()

        return {
            "Username": getpass.getuser(),
            "Hostname": socket.gethostname(),
            "Operating System": uname.system,
            "Node Name": uname.node,
            "Release": uname.release,
            "Version": uname.version,
            "Machine": uname.machine,
            "Processor": uname.processor,
            "Architecture": platform.architecture()[0],
            "Python Version": platform.python_version(),
            "Platform": platform.platform(),
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    @staticmethod
    def get_cpu_information():
        """Return CPU information."""

        frequency = psutil.cpu_freq()

        return {
            "Physical Cores": psutil.cpu_count(logical=False),
            "Logical Cores": psutil.cpu_count(logical=True),
            "Current Frequency (MHz)": round(frequency.current, 2) if frequency else "N/A",
            "Minimum Frequency (MHz)": round(frequency.min, 2) if frequency else "N/A",
            "Maximum Frequency (MHz)": round(frequency.max, 2) if frequency else "N/A",
            "CPU Usage (%)": psutil.cpu_percent(interval=1)
        }

    @staticmethod
    def get_memory_information():
        """Return memory information."""

        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()

        return {
            "Total RAM (GB)": round(memory.total / (1024 ** 3), 2),
            "Available RAM (GB)": round(memory.available / (1024 ** 3), 2),
            "Used RAM (GB)": round(memory.used / (1024 ** 3), 2),
            "RAM Usage (%)": memory.percent,
            "Swap Total (GB)": round(swap.total / (1024 ** 3), 2),
            "Swap Used (GB)": round(swap.used / (1024 ** 3), 2),
            "Swap Usage (%)": swap.percent
        }

    @staticmethod
    def get_disk_information():
        """Return disk partition information."""

        disks = []

        for partition in psutil.disk_partitions():

            try:

                usage = psutil.disk_usage(partition.mountpoint)

                disks.append({
                    "Device": partition.device,
                    "Mount Point": partition.mountpoint,
                    "File System": partition.fstype,
                    "Total Size (GB)": round(usage.total / (1024 ** 3), 2),
                    "Used Space (GB)": round(usage.used / (1024 ** 3), 2),
                    "Free Space (GB)": round(usage.free / (1024 ** 3), 2),
                    "Usage (%)": usage.percent
                })

            except PermissionError:
                continue

        return disks

    @staticmethod
    def get_boot_information():
        """Return boot time and uptime."""

        boot_time = datetime.fromtimestamp(psutil.boot_time())
        now = datetime.now()

        uptime = now - boot_time

        return {
            "Boot Time": boot_time.strftime("%Y-%m-%d %H:%M:%S"),
            "System Uptime": str(uptime)
        }

    @staticmethod
    def get_load_average():
        """Return system load average (Linux/macOS only)."""

        try:

            import os

            load = os.getloadavg()

            return {
                "1 Minute": load[0],
                "5 Minutes": load[1],
                "15 Minutes": load[2]
            }

        except Exception:

            return {
                "Message": "Load average is not available on this operating system."
            }

    @staticmethod
    def get_all_system_information():
        """Return all system information."""

        return {
            "Basic Information": SystemInfo.get_basic_information(),
            "CPU Information": SystemInfo.get_cpu_information(),
            "Memory Information": SystemInfo.get_memory_information(),
            "Disk Information": SystemInfo.get_disk_information(),
            "Boot Information": SystemInfo.get_boot_information(),
            "Load Average": SystemInfo.get_load_average()
        }


if __name__ == "__main__":

    import json

    data = SystemInfo.get_all_system_information()

    print(json.dumps(data, indent=4))