"""
network_info.py
----------------------------------------------------
Network Information Module

Collects:
- Hostname
- Private IP
- Public IP
- MAC Address
- Network Interfaces
- Network Statistics
- Active Connections

Author : I.P SINGH
Version : 2.0
"""

import socket
import uuid

import psutil
import requests


class NetworkInfo:
    """Collect network information."""

    @staticmethod
    def get_hostname():
        """Return hostname."""

        return socket.gethostname()

    @staticmethod
    def get_private_ip():
        """Return local/private IP."""

        try:
            return socket.gethostbyname(socket.gethostname())
        except Exception:
            return "Unavailable"

    @staticmethod
    def get_public_ip():
        """Return public IP."""

        try:
            response = requests.get(
                "https://api.ipify.org?format=json",
                timeout=5
            )

            return response.json()["ip"]

        except Exception:
            return "Unavailable"

    @staticmethod
    def get_mac_address():
        """Return MAC Address."""

        mac = uuid.getnode()

        return ":".join(
            f"{(mac >> ele) & 0xff:02X}"
            for ele in range(40, -1, -8)
        )

    @staticmethod
    def get_network_interfaces():
        """Return all network interfaces."""

        interfaces = {}

        addresses = psutil.net_if_addrs()

        for interface, addr_list in addresses.items():

            interfaces[interface] = []

            for addr in addr_list:

                interfaces[interface].append({

                    "Family": str(addr.family),
                    "Address": addr.address,
                    "Netmask": addr.netmask,
                    "Broadcast": addr.broadcast

                })

        return interfaces

    @staticmethod
    def get_network_statistics():
        """Return network I/O statistics."""

        stats = psutil.net_io_counters()

        return {

            "Bytes Sent": stats.bytes_sent,
            "Bytes Received": stats.bytes_recv,
            "Packets Sent": stats.packets_sent,
            "Packets Received": stats.packets_recv,
            "Input Errors": stats.errin,
            "Output Errors": stats.errout,
            "Dropped Incoming": stats.dropin,
            "Dropped Outgoing": stats.dropout

        }

    @staticmethod
    def get_active_connections():
        """Return active network connections."""

        connections = []

        try:

            for conn in psutil.net_connections():

                local = ""

                remote = ""

                if conn.laddr:
                    local = f"{conn.laddr.ip}:{conn.laddr.port}"

                if conn.raddr:
                    remote = f"{conn.raddr.ip}:{conn.raddr.port}"

                connections.append({

                    "Local Address": local,
                    "Remote Address": remote,
                    "Status": conn.status,
                    "PID": conn.pid

                })

        except Exception as error:

            connections.append({

                "Error": str(error)

            })

        return connections

    @staticmethod
    def get_dns_information():
        """Return DNS information."""

        try:

            return socket.gethostbyname_ex(
                socket.gethostname()
            )

        except Exception:

            return "Unavailable"

    @staticmethod
    def get_all_network_info():
        """Return all network information."""

        return {

            "Hostname":
                NetworkInfo.get_hostname(),

            "Private IP":
                NetworkInfo.get_private_ip(),

            "Public IP":
                NetworkInfo.get_public_ip(),

            "MAC Address":
                NetworkInfo.get_mac_address(),

            "DNS":
                NetworkInfo.get_dns_information(),

            "Interfaces":
                NetworkInfo.get_network_interfaces(),

            "Statistics":
                NetworkInfo.get_network_statistics(),

            "Connections":
                NetworkInfo.get_active_connections()

        }


if __name__ == "__main__":

    import json

    data = NetworkInfo.get_all_network_info()

    print(json.dumps(data, indent=4))