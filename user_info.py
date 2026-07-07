"""
user_info.py
----------------------------------
Collect user and environment information.

Author : I.P SINGH
Version: 2.0
"""

import getpass
import os
import platform
import socket
from datetime import datetime

import psutil


class UserInfo:

    @staticmethod
    def get_current_user():
        """Return current user information."""

        return {
            "Username": getpass.getuser(),
            "Hostname": socket.gethostname(),
            "Home Directory": os.path.expanduser("~"),
            "Current Working Directory": os.getcwd(),
            "Operating System": platform.system()
        }

    @staticmethod
    def get_logged_in_users():
        """Return logged-in users."""

        users = []

        try:

            for user in psutil.users():

                users.append({
                    "Username": user.name,
                    "Terminal": user.terminal,
                    "Host": user.host,
                    "Started": datetime.fromtimestamp(
                        user.started
                    ).strftime("%Y-%m-%d %H:%M:%S")
                })

        except Exception as error:

            users.append({
                "Error": str(error)
            })

        return users

    @staticmethod
    def get_environment_variables():
        """Return environment variables."""

        variables = {}

        for key, value in os.environ.items():
            variables[key] = value

        return variables

    @staticmethod
    def get_system_uptime():
        """Return system uptime."""

        boot = datetime.fromtimestamp(psutil.boot_time())
        now = datetime.now()

        uptime = now - boot

        return {
            "Boot Time": boot.strftime("%Y-%m-%d %H:%M:%S"),
            "Uptime": str(uptime)
        }

    @staticmethod
    def get_user_sessions():
        """Return active user sessions."""

        sessions = []

        try:

            for session in psutil.users():

                sessions.append({
                    "User": session.name,
                    "Terminal": session.terminal,
                    "Host": session.host
                })

        except Exception as error:

            sessions.append({
                "Error": str(error)
            })

        return sessions

    @staticmethod
    def is_admin():
        """
        Determine whether the program is running with
        administrator/root privileges.
        """

        try:

            if os.name == "nt":
                import ctypes
                return bool(
                    ctypes.windll.shell32.IsUserAnAdmin()
                )

            return os.getuid() == 0

        except Exception:
            return False

    @staticmethod
    def get_all_user_information():

        return {

            "Current User":
                UserInfo.get_current_user(),

            "Logged In Users":
                UserInfo.get_logged_in_users(),

            "Environment Variables":
                UserInfo.get_environment_variables(),

            "System Uptime":
                UserInfo.get_system_uptime(),

            "User Sessions":
                UserInfo.get_user_sessions(),

            "Administrator":
                UserInfo.is_admin()

        }