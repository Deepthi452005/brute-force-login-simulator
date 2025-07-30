from flask import Flask, render_template, request
from datetime import datetime
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import bcrypt

app = Flask(__name__)

# Setup Flask-Limiter
limiter = Limiter(get_remote_address, app=app, default_limits=["10 per minute"])

# In-memory store for failed attempts (per IP)
failed_attempts = {}

# Check credentials from hashed users.txt
def check_credentials(username, password):
    try:
        with open("users.txt", "r") as file:
            for line in file:
                stored_user, stored_hash = line.strip().split(":")
                if stored_user == username:
                    return bcrypt.checkpw(password.encode(), stored_hash.encode())
    except FileNotFoundError:
        print("[!] users.txt not found.")
    return False

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
@limiter.limit("5 per minute")  # Additional per-IP route protection
def login():
    username = request.form["username"]
    password = request.form["password"]
    ip = request.remote_addr

    # Log every attempt
    with open("login_attempts.log", "a") as log:
        log.write(f"[{datetime.now()}] {ip} -> Attempted: {username}:{password}\n")

    # Initialize IP tracking
    if ip not in failed_attempts:
        failed_attempts[ip] = 0

    # Lock out after 5 failures
    if failed_attempts[ip] >= 5:
        return render_template("login.html", message="Too many failed attempts. Try again later.", color="orange")

    # Check login
    if check_credentials(username, password):
        failed_attempts[ip] = 0  # Reset on success
        return render_template("login.html", message="Login Successful!", color="lime")
    else:
        failed_attempts[ip] += 1
        return render_template("login.html", message="Invalid Credentials", color="red")

if __name__ == "__main__":
    app.run(debug=True)
