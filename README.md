# Internship Task: Packet Sniffing and Protocol Analysis

## Objective
Build a Python program to capture and analyze network packets using Scapy.

## Tools Used
- Python 3
- Scapy
- Kali Linux

## Steps Completed
1. Built packet sniffer using Scapy
2. Analyzed ARP packet structure
3. Studied OSI model and protocol flow
4. Compared Scapy vs Socket libraries
5. Displayed key packet info (IP, ports, payload)
   
## Sample Output
Full Packet Structure:
###[ Ethernet ]###
  dst       = 08:00:27:1f:b7:23
  src       = 52:55:0a:00:02:02
  type      = ARP
###[ ARP ]###
     hwtype    = Ethernet (10Mb)
     ptype     = IPv4
     hwlen     = 6
     plen      = 4
     op        = is-at
     hwsrc     = 52:55:0a:00:02:02
     psrc      = 10.0.2.2
     hwdst     = 08:00:27:1f:b7:23
     pdst      = 10.0.2.15
###[ Padding ]###
        load      = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

