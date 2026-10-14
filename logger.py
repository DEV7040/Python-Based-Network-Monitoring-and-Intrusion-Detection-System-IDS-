import csv
import os
from datetime import datetime


LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "network_events.csv")


def initialize_log():

    os.makedirs(LOG_FOLDER, exist_ok=True)

    if not os.path.exists(LOG_FILE):

        with open(LOG_FILE, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Time",
                "Source IP",
                "Destination IP",
                "Protocol",
                "Destination Port",
                "Event"
            ])


def log_event(packet, event="Normal Traffic"):

    initialize_log()

    with open(LOG_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            packet["src_ip"],
            packet["dst_ip"],
            packet["protocol"],
            packet["dst_port"],
            event
        ])