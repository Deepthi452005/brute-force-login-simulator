import bcrypt

users = {
    "admin": "admin123",
    "deepu": "deepu@123"
}

with open("users.txt", "w") as file:
    for user, pwd in users.items():
        hashed = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())
        file.write(f"{user}:{hashed.decode()}\n")

print("✔️ Hashed passwords saved to users.txt")
