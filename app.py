from flask import Flask, render_template, jsonify

import packet_monitor
import ids
import logger


app = Flask(__name__)


# Initialize CSV log
logger.initialize_log()


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/api/data")
def get_data():

    stats = packet_monitor.get_statistics()

    packets = stats["packets"]

    # Check packets with IDS
    for packet in packets:

        ids.check_packet(packet)

    # Get alerts
    alerts = ids.get_alerts()

    return jsonify({

        "total": stats["total"],

        "tcp": stats["tcp"],

        "udp": stats["udp"],

        "icmp": stats["icmp"],

        "other": stats["other"],

        "packets": packets,

        "alerts": alerts

    })


if __name__ == "__main__":

    print("--------------------------------")
    print(" Python Network IDS")
    print("--------------------------------")

    print("Dashboard:")
    print("http://127.0.0.1:5000")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )