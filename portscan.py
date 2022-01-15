#coding:UTF-8

import socket
import sys 


if len(sys.argv) < 2: 
    print("Usage: portscan.py [IP] [ports - leave empty to listen to all ports]")    
    sys.exit(1)

default_ports = [21, 22, 80, 8080, 443, 53, 3306, 3389]

for port in default_ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5)

    try:
        response = client.connect_ex((sys.argv[1], port ))
        if response == 0:
            print("Port: ", str(port), "open")

    except:
        print("ERROR - Host not found")
        sys.exit(1)
