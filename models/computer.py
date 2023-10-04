import re

ip_address_pattern = re.compile(r"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]["
                                r"0-9]?)){3}")

class Computer:

    def __init__(self, ip: str, mac_address: str, os: str, status: str = "Active", name: str = None):
        self.ip = ip
        self.mac_address = mac_address
        self.os = os
        self.status = status
        self.name = name if name is not None else f"Computer {self.ip}"

    def __init__(self, json):
        self.ip = json['ip']
        self.mac_address = json['mac_address']
        self.os = json['os']
        self.status = json['status']
        self.name = json['name'] if json['name'] is not None else f"Computer {self.ip}"

    def __repr__(self):
        return self.name if self.name != "Computer" else f"{self.name} {self.ip}"

    def __str__(self):
        return self.name if self.name != "Computer" else f"{self.name} {self.ip}"

    def set_ip(self, ip):
        self.ip = ip

    def set_mac_address(self, mac):
        self.mac_address = mac

    def set_os(self, os):
        self.os = os

    def set_status(self, status: str):
        statuses = ["Active", "Retired", "Missing"]
        if status.title() in statuses:
            self.status = status
        else:
            print(f"Computer instantiated with invalid status, {status}. Defaulting to 'Active'")
            self.status = "Active"

    def set_ip_input(self):
        accepting = True
        while accepting:
            self.ip = str(input("ip: "))
            if ip_address_pattern.match(self.ip):
                accepting = False
            else:
                print("Invalid IP, please re-enter")
                continue

    def set_mac_address_input(self):
        self.mac_address = str(input("mac_address: "))

    def set_os_input(self):
        allowed_os = ['Mac', 'Windows', 'Linux', 'Other']
        accepting = True
        while accepting:
            self.os = input("os: ").title()
            if self.os in allowed_os:
                accepting = False
            else:
                print(f"Invalid OS, enter one of: {allowed_os}")
                continue

    def set_status_input(self):
        statuses = ["Active", "Retired", "Missing"]
        accepting = True
        while accepting:
            status = input("status: ")
            if status.title() in statuses:
                self.status = status
            else:
                print(f"invalid status, enter one of: {statuses}")
                continue

    def set_name_input(self):
        self.name = input("name: ")

    def display(self):
        print(f"""
        {self.name}
        ip: {self.ip}
        mac: {self.mac_address}
        os: {self.os}
        status: {self.status}""")

    def get_json(self):
        return {
            "ip": self.ip,
            "mac_address": self.mac_address,
            "os": self.os,
            "status": self.status,
            "name": self.name
        }
        

