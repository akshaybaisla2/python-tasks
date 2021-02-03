import re
def validIPAddress(IP:str):
    def isIp4(s):
        try:
            return str(int(s)) == s and 0<= int(s) <= 255
        except:
            return False

    def isIp6(s):
        if len(s) > 4: return False

        try:
            int(s,16)
            return True
        except:
            return False

    ip4 = IP.split(".")
    ip6 = IP.split(":")

    if len(ip4) == 4 and all(isIp4(n) for n in ip4):
            return "IPv4"
    if len(ip6) == 8 or 4 and all(isIp6(n) for n in ip6):
            return "IPv6"
    return "Invalid IP"
print(validIPAddress(IP="8003::1"))