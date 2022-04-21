import scapy.all as scapy


class Device():
    mac: str
    ip: str

    def __init__(self, ip, mac="") -> None:
        self.ip = ip
        self.mac = self.setMac() if mac != "" else mac

    def setMac(self):
        packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=self.ip)
        ans = scapy.srp(packet, timeout=2, verbose=False)[0]
        try:
            return ans[0][1].hwsrc
        except:
            raise ValueError("Make sure the device is online!")

    def __str__(self) -> str:
        return f"{self.ip} <-> {self.mac}"
