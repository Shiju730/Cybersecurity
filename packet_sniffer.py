from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    # Show full packet structure
    print("\n🔍 Full Packet Structure:")
    packet.show()

    # Optional: Keep your custom summary too
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

# Run the sniffer (add timeout or count if needed)
sniff(prn=packet_callback, store=False, timeout=30)
