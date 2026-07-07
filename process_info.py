"""
process_info.py
----------------------------------------------------
Process Information Module

Collects:
- Running Processes
- PID
- Process Name
- Status
- CPU Usage
- Memory Usage
- Executable Path
- Username
- Parent PID
- Process Creation Time

Author : I.P SINGH
Version : 2.0
"""

from datetime import datetime

import psutil


class ProcessInfo:
    """Collect process information."""

    @staticmethod
    def get_running_processes():
        """
        Return information about running processes.
        """

        processes = []

        for process in psutil.process_iter([
            "pid",
            "name",
            "username",
            "status",
            "cpu_percent",
            "memory_percent",
            "exe",
            "ppid",
            "create_time"
        ]):

            try:

                info = process.info

                processes.append({

                    "PID": info["pid"],

                    "Name": info["name"],

                    "Username": info["username"],

                    "Status": info["status"],

                    "CPU (%)": round(
                        info["cpu_percent"], 2
                    ),

                    "Memory (%)": round(
                        info["memory_percent"], 2
                    ),

                    "Executable": info["exe"],

                    "Parent PID": info["ppid"],

                    "Created": datetime.fromtimestamp(
                        info["create_time"]
                    ).strftime("%Y-%m-%d %H:%M:%S")

                })

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess
            ):
                continue

        return processes

    @staticmethod
    def get_top_cpu_processes(limit=10):
        """
        Return top CPU-consuming processes.
        """

        processes = ProcessInfo.get_running_processes()

        processes.sort(
            key=lambda x: x["CPU (%)"],
            reverse=True
        )

        return processes[:limit]

    @staticmethod
    def get_top_memory_processes(limit=10):
        """
        Return top memory-consuming processes.
        """

        processes = ProcessInfo.get_running_processes()

        processes.sort(
            key=lambda x: x["Memory (%)"],
            reverse=True
        )

        return processes[:limit]

    @staticmethod
    def get_process_summary():
        """
        Return process summary.
        """

        total = len(psutil.pids())

        running = 0
        sleeping = 0
        stopped = 0

        for proc in psutil.process_iter(["status"]):

            try:

                status = proc.info["status"]

                if status == psutil.STATUS_RUNNING:
                    running += 1

                elif status == psutil.STATUS_SLEEPING:
                    sleeping += 1

                elif status == psutil.STATUS_STOPPED:
                    stopped += 1

            except Exception:
                continue

        return {

            "Total Running Processes": total,

            "Running": running,

            "Sleeping": sleeping,

            "Stopped": stopped

        }

    @staticmethod
    def get_all_process_info():
        """
        Return all process information.
        """

        return {

            "Summary":
                ProcessInfo.get_process_summary(),

            "Top CPU Processes":
                ProcessInfo.get_top_cpu_processes(),

            "Top Memory Processes":
                ProcessInfo.get_top_memory_processes(),

            "All Processes":
                ProcessInfo.get_running_processes()

        }


if __name__ == "__main__":

    import json

    data = ProcessInfo.get_all_process_info()

    print(json.dumps(data, indent=4))