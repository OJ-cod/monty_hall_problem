from flask import Flask, jsonify, request
import threading
import random
import time

app = Flask(__name__)

# Stats storage
stats = {
    "wins": 0,
    "losses": 0,
    "total": 0,
    "running": False
}

doors = {0, 1, 2}


def simulate():
    while stats["running"]:
        local_wins = 0
        local_losses = 0

        for _ in range(100):
            prize = random.choice(list(doors))
            choice = random.choice(list(doors))

            if choice == prize:
                opened = random.choice(list(doors - {prize}))
            else:
                opened = list(doors - {prize, choice})[0]

            switched = list(doors - {choice, opened})[0]

            if switched == prize:
                local_wins += 1
            else:
                local_losses += 1

        stats["wins"] += local_wins
        stats["losses"] += local_losses
        stats["total"] += 100
        time.sleep(1)


def start_background_simulation():
    if not stats["running"]:
        stats["running"] = True
        thread = threading.Thread(target=simulate)
        thread.daemon = True
        thread.start()


@app.route("/stats", methods=["GET"])
def get_stats():
    return jsonify({
        "wins": stats["wins"],
        "losses": stats["losses"],
        "total": stats["total"],
        "win_rate": round(stats["wins"] / stats["total"], 4) if stats["total"] else 0,
        "loss_rate": round(stats["losses"] / stats["total"], 4) if stats["total"] else 0
    })


@app.route("/start", methods=["POST"])
def start_simulation():
    if not stats["running"]:
        start_background_simulation()
        return jsonify({"message": "Simulation started."})
    else:
        return jsonify({"message": "Simulation already running."})


# @app.route("/reset", methods=["POST"])
# def reset_stats():
#     stats["wins"] = 0
#     stats["losses"] = 0
#     stats["total"] = 0
#     stats["running"] = False
#     return jsonify({"message": "Stats reset and simulation stopped."})


if __name__ == "__main__":
    start_background_simulation()  # 🔥 Auto-start simulation
    app.run(debug=True)
