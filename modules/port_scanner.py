import data.common_ports as common_ports
import socket
import re


def get_open_ports(target, port_range, option=False):

    if is_host_invalid(target) and re.search('[a-z]', target):
        return 'Error: Invalid hostname'
    if is_host_invalid(target):
        return 'Error: Invalid IP address'

    list_open_ports = [port for port in range(
        port_range[0], port_range[1] + 1) if is_port_open(target, port) == True]

    if option:
        return get_return_string(target, list_open_ports)
    else:
        return list_open_ports


def is_host_invalid(host):
    try:
        socket.gethostbyname(host)
        return False
    except:
        return True


def is_port_open(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((host, int(port))):
        return False
    else:
        return True


def get_return_string(target, list_open_ports):
    returnString = str()
    returnString += 'Open ports for '
    try:
        x = socket.gethostbyaddr(target)
        returnString += str(x[0]) + ' (' + str(x[2][0]) + ')\n'
    except:
        returnString += str(target) + '\n'
    returnString += 'PORT     SERVICE\n'
    # # port take 9 space, then service
    for port in list_open_ports:
        port = str(port)
        returnString += port
        spaceBetween = 9 - len(port)
        for i in range(spaceBetween):
            returnString += ' '
        returnString += str(common_ports.ports_and_services[int(port)])

    return returnString
