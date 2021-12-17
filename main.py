import port_scanner
from unittest import main

print("What is the url/IP you would like to scan?")
URLorIP = input()

try:
    print("Enter the first port of the range as an integer:")
    startRange = int(input())
    print("Enter the second port of range as an integer:")
    endRange = int(input())
except ValueError:
    print("This is not a valid integer number. Please try again.")
    quit()

ports = port_scanner.get_open_ports(URLorIP, [startRange,endRange])
print("Open ports:", ports)

# # Called with URL   
# ports = port_scanner.get_open_ports(URLorIP, [75,85])
# print("Open ports:", ports)

# # Called with ip address
# ports = port_scanner.get_open_ports("104.26.10.78", [8079, 8090])
# print("Open ports:", ports)

# # Verbose called with ip address and no host name returned -- single open port
# ports = port_scanner.get_open_ports("104.26.10.78", [440, 450], True)
# print(ports + '\n')

# # Verbose called with ip address and valid host name returned -- single open port
# ports = port_scanner.get_open_ports("137.74.187.104", [440, 450], True)
# print(ports + '\n')

# # Verbose called with host name -- multiple ports returned
# ports = port_scanner.get_open_ports("scanme.nmap.org", [20, 80], True)
# print(ports + '\n')

# # Run unit tests automatically
# # main(module='test_module', exit=False)