import modules.port_scanner as port_scanner


print(port_scanner.get_open_ports("209.216.230.240", [440, 445]))
print(port_scanner.get_open_ports("www.stackoverflow.com", [79, 82]))

print(port_scanner.get_open_ports("104.26.10.78", [440, 445], True))
print(port_scanner.get_open_ports("137.74.187.104", [440, 445], True))
print(port_scanner.get_open_ports("scanme.nmap.org", [79, 80], True))

print(port_scanner.get_open_ports("266.255.9.10", [79, 82]))
print(port_scanner.get_open_ports("266.255fdsfdsf.9.10", [79, 82]))
print(port_scanner.get_open_ports("scanme.nmap", [79, 82]))
print(port_scanner.get_open_ports("scanme.nmap1", [79, 82]))
