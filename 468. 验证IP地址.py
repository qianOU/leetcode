class Solution:
    def validIPAddress(self, IP: str) -> str:
        IP = IP.replace('.', ':')
        ip = IP.split(':')
        print(ip)
        if len(ip) == 4:
            condition = lambda one: one.isdigit() and (one[0] != '0' and int(one) < 256) or len(one) == 1
            for one in ip:
                if not condition(one):
                    return 'Neither'
            return 'IPv4'
        elif len(ip) == 8:
            condition = lambda one: 1<=len(one)<=4 and all(i.lower() in 'abcdef' for i in one if i.isalpha()) 
                                    # len(one.lstrip('0')) + 1 >= len(one)
            for one in ip:
                if not condition(one): 
                    print(one)
                    return 'Neither'
            return 'IPv6'
        
        return 'Neither'

print(Solution().validIPAddress("2001:0db8:85a3:0000:0:8A2E:0370:733a"))