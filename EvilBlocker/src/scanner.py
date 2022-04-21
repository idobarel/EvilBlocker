import scapy.all as scapy
from src.device import Device
import time


class Scanner():
    ip: str
    clients: list

    def __init__(self, ip) -> None:
        self.ip = ip
        self.clients = []

    def scan(self):
        packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=self.ip)
        answered = scapy.srp(packet, timeout=2, verbose=False)[0]

        for element in answered:
            client = Device(element[1].psrc, element[1].hwsrc)
            self.clients.append(client)

        time.sleep(2)
        print(f"[+] Found {len(self.clients)} clients!")
