import socket, sys

def check_port(ip, port_list):
    try:
        for port in port_list:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip,port))
            if result == 0:
                print(f'Port: {port} \t Open')
            else:
                print(f'Port: {port} \t Close')
            sock.close()
    except socket.error as error:
        print(str(error))
        print('Connection error')
        sys.exit

check_port('172.217.173.67',range(442,445))#range(1,1023)
#google.com.py: 172.217.173.67:443