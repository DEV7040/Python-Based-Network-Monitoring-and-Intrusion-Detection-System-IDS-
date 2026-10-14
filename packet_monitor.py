from scapy.all import sniff, IP, TCP, UDP, ICMP
from collections import Counter
import threading
import time

packet_count = 0
protocol_count = Counter()
recent_packets = []

lock = threading.Lock()


def process_packet(packet):
    global packet_count

    if IP not in packet:
        return

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst

    protocol = "OTHER"
    src_port = "-"
    dst_port = "-"

    if TCP in packet:
        protocol = "TCP"
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

    elif UDP in packet:
        protocol = "UDP"
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport

    elif ICMP in packet:
        protocol = "ICMP"

    packet_info = {
        "time": time.strftime("%H:%M:%S"),
        "src_ip": src_ip,
        "dst_ip": dst_ip,
        "protocol": protocol,
        "src_port": src_port,
        "dst_port": dst_port
    }

    with lock:
        packet_count += 1
        protocol_count[protocol] += 1

        recent_packets.insert(0, packet_info)

        # Keep only last 20 packets
        if len(recent_packets) > 20:
            recent_packets.pop()


def start_monitoring():
    print("Starting network monitoring...")
    sniff(prn=process_packet, store=False)


def get_statistics():
    with lock:
        return {
            "total": packet_count,
            "tcp": protocol_count["TCP"],
            "udp": protocol_count["UDP"],
            "icmp": protocol_count["ICMP"],
            "other": protocol_count["OTHER"],
            "packets": list(recent_packets)
        }


def get_packets():
    with lock:
        return list(recent_packets)


# Start monitoring in background
monitor_thread = threading.Thread(
    target=start_monitoring,
    daemon=True
)

monitor_thread.start()