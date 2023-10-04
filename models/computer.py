class Computer:

    def __init__(self, ip: str, mac_address: str, os: str, status: str = "Active", name: str = None):
        self.ip = ip
        self.mac_address = mac_address
        self.os = os
        self.set_status(status)
        self.name = name if name is not None else f"Computer {self.ip}"

    def __init__(self, json:dict):
        self.ip = json.get('ip')
        self.mac_address = json.get('mac_address')
        self.os = json.get('os')
        self.status = json.get('status')
        self.name = json.get('name') if json.get('name') is not None else f"Computer {self.ip}"

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

    def display(self):
        print(f"""
        {self.name}
        mac: {self.mac_address}
        os: {self.os}
        status: {self.status}""")
