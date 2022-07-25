import ipaddress
import sys
try:
    ip=ipaddress.ipaddress(sys.argv[1])
    print('%s is a correct IP %s address'%(ip,ip.version))
except:
    print("It is invalid")