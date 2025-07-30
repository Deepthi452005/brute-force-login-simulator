# 🔐 Brute Force Login Simulator

A Python-based web application that simulates a login form and logs brute force attack attempts. Built using Flask, this project is ideal for demonstrating and understanding how brute force attacks occur and how they can be logged and prevented.

---

## 📌 Features

- Custom-designed HTML login page
- Logs every login attempt with timestamp
- Verifies credentials from an encrypted (hashed) password file
- Displays login success or failure messages
- Simple and clear UI with green-themed design
- Prevents actual vulnerabilities (for educational use only)

---

## 🚀 Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Python (Flask)
- **Logging**: `login_attempts.log` for all login trials
- **Password Handling**: SHA-256 hashing (for safe credential storage)

---

## 📁 Project Structure
brute_force_simulator/
│
├── app.py # Main Flask app
├── users.txt # Encrypted user credentials
├── login_attempts.log # Log file of all login attempts
├── templates/
│ └── login.html # Login page template
2. Set Up Virtual Environment (Optional)
3. Install Requirements
4. Start the Application

⚠️ Disclaimer
This simulator is for educational and demonstration purposes only. It is not a real authentication system and should never be used in production environments.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙋‍♂️ Author
Deepu Deepthi
Student | Cybersecurity Enthusiast
Feel free to connect or suggest improvements!
