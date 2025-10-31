from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    print("\n Full Packet Structure:")
    packet.show()
    
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto

        print(f"\n[+] Packet: {src_ip} → {dst_ip} | Protocol: {proto}")

        if TCP in packet:
            print("    TCP Segment")
            print(f"    Src Port: {packet[TCP].sport}, Dst Port: {packet[TCP].dport}")
        elif UDP in packet:
            print("    UDP Segment")
            print(f"    Src Port: {packet[UDP].sport}, Dst Port: {packet[UDP].dport}")

        print(f"    Payload: {bytes(packet.payload)}")

sniff(prn=packet_callback, store=False, timeout=30)
