# Python-Based Network Monitoring and Intrusion Detection System (IDS)

## 📌 Project Overview

The **Network Monitoring and Intrusion Detection System (IDS)** is a Python-based application that monitors network traffic in real time, analyzes packets, detects suspicious activities, and displays results on a web dashboard.

The system uses **Scapy** for packet capture and **Flask** to provide a web-based dashboard. Network events are stored in a CSV log file for future analysis.

## 🎯 Objectives

- Monitor live network packets.
- Display network traffic statistics.
- Detect suspicious network activities.
- Generate real-time intrusion alerts.
- Store network events in CSV log files.

## ✨ Features

- **Live Packet Monitoring:** Captures network packets and displays source IP, destination IP, protocol, and destination port.
- **Traffic Statistics:** Displays total packets and TCP, UDP, and ICMP counts.
- **Intrusion Detection:** Identifies potentially suspicious activities, such as port scans and unusual traffic patterns, using predefined rules.
- **Real-Time Alerts:** Displays detected suspicious activities with source IP, description, severity, and timestamp.
- **Event Logging:** Stores network events in a CSV file for future investigation.
- **Web Dashboard:** Provides a simple interface for monitoring network activity.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Flask | Web application and dashboard |
| Scapy | Network packet capture and analysis |
| HTML | Dashboard structure |
| CSS | Dashboard styling |
| JavaScript | Dynamic dashboard updates |
| CSV | Network event storage |

## 📂 Project Structure

```text
CNS LAB/
│
├── app.py
├── packet_monitor.py
├── ids.py
├── logger.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── logs/
│   └── network_events.csv
│
└── README.md
```

## ⚙️ Requirements

- Python 3.10 or later
- Flask
- Scapy
- Npcap for packet capture on Windows
- Cursor or Visual Studio Code (recommended)
- Administrator privileges may be required for packet capture.

## 🚀 Installation and Setup

### Step 1: Open the project folder

Open the `CNS LAB` folder in Cursor.

### Step 2: Install Python dependencies

Open the terminal and run:

```bash
python -m pip install flask scapy
```

### Step 3: Install Npcap on Windows

Download and install Npcap from the official website:

https://npcap.com/

Npcap enables packet capture on Windows. Follow the installer instructions and restart Cursor if necessary.

### Step 4: Run the application

In the terminal, navigate to your project folder:

```powershell
cd "C:\Users\gd775\Desktop\CNS LAB"
```

Start the application:

```bash
python app.py
```

### Step 5: Open the dashboard

Open your browser and visit:

http://127.0.0.1:5000

The dashboard should display network statistics, live packet information, and intrusion alerts when detection rules are triggered.

## 🔍 How It Works

1. **Packet Capture:** Scapy captures network packets.
2. **Packet Analysis:** The application extracts packet details such as IP addresses, protocols, and ports.
3. **Intrusion Detection:** The IDS checks traffic against predefined detection rules.
4. **Alert Generation:** If suspicious activity matches a rule, the system generates an alert.
5. **Event Logging:** Network events and detected incidents are recorded in the CSV log file.
6. **Dashboard Display:** Flask serves the dashboard, which displays traffic statistics and alerts.

## 🚨 Example Intrusion Alert

```text
Type: Port Scan
Source IP: 34.98.122.109
Description: Multiple ports accessed (10)
Severity: HIGH
Time: 15:33:02
```

This alert indicates that the observed traffic matched the configured port-scan detection rule. It does not prove that the source IP is malicious.

## 📄 Log File

Network events are stored in:

```text
logs/network_events.csv
```

Depending on the logger implementation, records may include:

- Timestamp
- Source IP address
- Destination IP address
- Protocol
- Destination port
- Event type or alert description

These records can be reviewed using Excel, a text editor, or a CSV viewer.

## 🔐 Security and Limitations

- Run packet monitoring only on networks and devices you are authorized to monitor.
- Alerts are based on predefined rules and may produce false positives.
- This project is an educational prototype, not a replacement for an enterprise-grade IDS.
- Captured traffic may contain sensitive information. Protect log files and avoid collecting data unnecessarily.
- The Flask development server is intended for local testing, not public production deployment.

## 🔮 Future Enhancements

- Live traffic graphs and protocol distribution charts.
- IP-based traffic filtering and search.
- Improved detection rules and severity classification.
- Alert history and log download options.
- Start/stop monitoring controls.
- Dashboard dark mode and browser notifications.
- Configurable thresholds and network interface selection.

## 🎓 Expected Outcomes

1. Live network packet monitoring.
2. A visual traffic statistics dashboard.
3. Detection of suspicious network activity.
4. Real-time intrusion alerts.
5. CSV-based network event logs.

## 👨‍💻 Project Information

**Project Name:** Python-Based Network Monitoring and Intrusion Detection System (IDS)

**Domain:** Computer Networks and Cybersecurity

**Project Type:** Educational / Academic Project

## 📜 License

This project is intended for educational and learning purposes. Add a license file if you plan to distribute it publicly.
