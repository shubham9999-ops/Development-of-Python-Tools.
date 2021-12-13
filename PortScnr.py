import nmap
import ipaddress
import re
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535
print("                 *********      **      **      *")
print("                     \        **  **  **  **    /")
print("******  **   **      *        **  **  **  **    *")
print("|    |   ** **       \        **  **  **  **    /")
print("******     |         *          **      **      *********")
print("|          *                                             ")
print("*          |                                             ")
print("\n")
while True:
    ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
    try:
        ip_address_obj = ipaddress.ip_address(ip_add_entered)
        print("You entered a valid ip address.")
        break
    except:
        print("You entered an invalid ip address")


while True:
    print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

nm = nmap.PortScanner()
for port in range(port_min, port_max + 1):
    try:
        result = nm.scan(ip_add_entered, str(port))
        port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
        print(f"Port {port} is {port_status}")
    except:
        print(f"Cannot scan port {port}.")
