import port_scanner
from unittest import main
import pyfiglet

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)


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

# Run unit tests automatically
# main(module='test_module', exit=False)