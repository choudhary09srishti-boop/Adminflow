from admin_panel.app import app
from flask import request, jsonify
from agent.brain import ask_groq
from agent.browser import run_browser_task
from agent.decision import check_and_decide

BASE_URL = "http://127.0.0.1:8000"

@app.route("/run-task", methods=["POST"])
def run_task():
    data = request.get_json()
    task = data["request"]
    instruction = ask_groq(task)

    if "create" in task.lower():
        url = BASE_URL + "/"
    elif "reset" in task.lower():
        url = BASE_URL + "/reset"
    elif "user" in task.lower() or "list" in task.lower():
        url = BASE_URL + "/users"
    else:
        url = instruction

    result = run_browser_task(url, task, data.get("data", {}))
    return jsonify({"status": "done", "result": result})

@app.route("/check-user", methods=["POST"])
def check_user():
    data = request.get_json()
    decision = check_and_decide(data)
    return jsonify(decision)