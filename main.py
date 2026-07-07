"""
main.py
--------------------------------------------------------
System Information Gatherer v2.0

Author : I.P SINGH
Version : 2.0
"""

import time

from banner import Banner
from logger import Logger
from utils import Utils

from system_info import SystemInfo
from hardware_info import HardwareInfo
from network_info import NetworkInfo
from process_info import ProcessInfo
from software_info import SoftwareInfo
from user_info import UserInfo

from report_generator import ReportGenerator
from hash_generator import HashGenerator


class SystemInformationGatherer:

    def __init__(self):

        self.logger = Logger.setup()

        self.data = {}

    def collect_information(self):

        self.logger.info("Collecting system information...")

        Utils.progress_bar(1)

        self.data["System Information"] = (
            SystemInfo.get_all_system_information()
        )

        self.logger.info("Collecting hardware information...")

        self.data["Hardware Information"] = (
            HardwareInfo.get_all_hardware_information()
        )

        self.logger.info("Collecting network information...")

        self.data["Network Information"] = (
            NetworkInfo.get_all_network_info()
        )

        self.logger.info("Collecting process information...")

        self.data["Process Information"] = (
            ProcessInfo.get_all_process_info()
        )

        self.logger.info("Collecting software information...")

        self.data["Software Information"] = (
            SoftwareInfo.get_all_software_information()
        )

        self.logger.info("Collecting user information...")

        self.data["User Information"] = (
            UserInfo.get_all_user_information()
        )

    def save_reports(self):

        self.logger.info("Generating reports...")

        reports = ReportGenerator.generate_reports(
            self.data
        )

        print("\nGenerated Reports")
        Utils.separator()

        for report_type, filename in reports.items():

            print(f"{report_type:<15}: {filename}")

            try:

                hashes = HashGenerator.generate_all(
                    filename
                )

                print(
                    f"SHA256        : {hashes['SHA256']}"
                )

            except Exception as error:

                print(
                    f"Hash Error    : {error}"
                )

            Utils.small_separator()

    def show_summary(self):

        print("\nSUMMARY")
        Utils.separator()

        basic = self.data["System Information"][
            "Basic Information"
        ]

        print(
            f"Username          : {basic['Username']}"
        )

        print(
            f"Hostname          : {basic['Hostname']}"
        )

        print(
            f"Operating System  : {basic['Operating System']}"
        )

        print(
            f"Architecture      : {basic['Architecture']}"
        )

        cpu = self.data["System Information"][
            "CPU Information"
        ]

        print(
            f"CPU Usage         : {cpu['CPU Usage (%)']}%"
        )

        memory = self.data["System Information"][
            "Memory Information"
        ]

        print(
            f"RAM Usage         : {memory['RAM Usage (%)']}%"
        )

        network = self.data["Network Information"]

        print(
            f"Private IP        : {network['Private IP']}"
        )

        print(
            f"Public IP         : {network['Public IP']}"
        )

        process = self.data["Process Information"]

        print(
            f"Running Processes : "
            f"{process['Summary']['Total Running Processes']}"
        )

        Utils.separator()


def main():

    Banner.show()

    logger = Logger.setup()

    start = time.perf_counter()

    logger.info("Application Started")

    try:

        app = SystemInformationGatherer()

        app.collect_information()

        app.show_summary()

        app.save_reports()

        elapsed = (
            time.perf_counter() - start
        )

        logger.info(
            f"Completed in {elapsed:.2f} seconds."
        )

        Utils.success(
            f"Completed Successfully "
            f"({elapsed:.2f} sec)"
        )

    except KeyboardInterrupt:

        logger.warning(
            "Execution interrupted by user."
        )

        Utils.warning(
            "Execution Cancelled."
        )

    except Exception as error:

        logger.exception(error)

        Utils.error(str(error))


if __name__ == "__main__":
    main()