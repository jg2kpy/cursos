from scapy.all import *

pkt_tcp = Ether()/IP(dst='google.com')/TCP(dport=80)

print(pkt_tcp)
print(pkt_tcp.summary())
print(pkt_tcp.show())

send(pkt_tcp)