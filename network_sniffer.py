from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

packet_count = 0

def process_packet(packet):
    global packet_count
    packet_count += 1

    print(f"\n--- Packet #{packet_count} ---")

    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        print(f"Source IP      : {src_ip}")
        print(f"Destination IP : {dst_ip}")

        if TCP in packet:
            print(f"Protocol       : TCP")
            print(f"Source Port    : {packet[TCP].sport}")
            print(f"Dest Port      : {packet[TCP].dport}")
            flags = packet[TCP].flags
            print(f"TCP Flags      : {flags}")

        elif UDP in packet:
            print(f"Protocol       : UDP")
            print(f"Source Port    : {packet[UDP].sport}")
            print(f"Dest Port      : {packet[UDP].dport}")

        elif ICMP in packet:
            print(f"Protocol       : ICMP")
            print(f"ICMP Type      : {packet[ICMP].type}")

        else:
            print(f"Protocol       : Other (proto number: {protocol})")

        if Raw in packet:
            payload = packet[Raw].load
            try:
                decoded = payload.decode('utf-8', errors='replace')
                print(f"Payload (text) : {decoded[:100]}")
            except:
                print(f"Payload (hex)  : {payload.hex()[:100]}")

    else:
        print("Non-IP packet captured")


def start_sniffing(interface=None, count=20):
    print("=" * 50)
    print("   Basic Network Sniffer - CodeAlpha Task 1")
    print("=" * 50)
    print(f"Capturing {count} packets... Press Ctrl+C to stop early.\n")

    try:
        sniff(iface=interface, prn=process_packet, count=count, store=False)
    except KeyboardInterrupt:
        pass

    print(f"\n[Done] Total packets captured: {packet_count}")


if __name__ == "__main__":
    start_sniffing(interface=None, count=20)
