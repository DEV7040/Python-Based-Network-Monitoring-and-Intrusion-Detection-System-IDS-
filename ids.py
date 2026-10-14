
import time
from collections import defaultdict

ip_ports = defaultdict(set)
ip_packets = defaultdict(list)

alerts = []

SUSPICIOUS_PORTS = {4444, 5555, 6666}


def check_packet(packet):
    current_time = time.time()

    src_ip = packet["src_ip"]
    dst_port = packet["dst_port"]

    # --------------------------------
    # 1. Suspicious Port Detection
    # --------------------------------

    try:
        port = int(dst_port)

        if port in SUSPICIOUS_PORTS:
            create_alert(
                src_ip,
                "Suspicious Port Activity",
                f"Connection to port {port}",
                "HIGH"
            )

    except (ValueError, TypeError):
        pass

    # --------------------------------
    # 2. Port Scan Detection
    # --------------------------------

    try:
        port = int(dst_port)

        ip_ports[src_ip].add(port)

        if len(ip_ports[src_ip]) >= 10:

            create_alert(
                src_ip,
                "Port Scan",
                f"Multiple ports accessed ({len(ip_ports[src_ip])})",
                "HIGH"
            )

            ip_ports[src_ip].clear()

    except (ValueError, TypeError):
        pass

    # --------------------------------
    # 3. High Packet Activity
    # --------------------------------

    ip_packets[src_ip].append(current_time)

    # Keep only packets from last 5 seconds
    ip_packets[src_ip] = [
        t for t in ip_packets[src_ip]
        if current_time - t <= 5
    ]

    if len(ip_packets[src_ip]) >= 100:

        create_alert(
            src_ip,
            "High Traffic",
            "More than 100 packets in 5 seconds",
            "MEDIUM"
        )

        ip_packets[src_ip].clear()


def create_alert(source_ip, alert_type, description, severity):

    alert = {
        "time": time.strftime("%H:%M:%S"),
        "source_ip": source_ip,
        "type": alert_type,
        "description": description,
        "severity": severity
    }

    # Avoid too many duplicate alerts
    if alert not in alerts:
        alerts.insert(0, alert)

        # Keep last 20 alerts
        if len(alerts) > 20:
            alerts.pop()


def get_alerts():
    return alerts