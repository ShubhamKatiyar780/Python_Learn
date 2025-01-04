import csv
import bcrypt
import re
import requests
import sys
import os

# Constants
MAX_LOGIN_ATTEMPTS = 5
API_URL = "http://ip-api.com/json/"
CSV_FILE = "regno.csv"
def load_users(filename):
    users = {}
    if not os.path.exists(filename):
        return users
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users[row['email']] = {
                'hashed_password': row['hashed_password'].encode(),
                'security_question': row['security_question'],
                'security_answer': row['security_answer']
            }
    return users


def save_users(filename, users):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['email', 'hashed_password', 'security_question', 'security_answer'])
        for email, data in users.items():
            writer.writerow([email, data['hashed_password'].decode(), data['security_question'], data['security_answer']])


def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def check_password(hashed, password):
    return bcrypt.checkpw(password.encode(), hashed)


def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def is_valid_password(password):
    if (len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"\d", password) and
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
        return True
    return False


def register_user(users):
    email = input("Enter your email: ")
    if not is_valid_email(email):
        print("Invalid email format.")
        return False

    if email in users:
        print("Email is already registered.")
        return False

    while True:
        password = input("Enter your password: ")
        if is_valid_password(password):
            break
        else:
            print("Password does not meet the criteria.")

    security_question = input("Enter a security question: ")
    security_answer = input("Enter the answer to your security question: ")

    users[email] = {
        'hashed_password': hash_password(password),
        'security_question': security_question,
        'security_answer': security_answer
    }
    save_users(CSV_FILE, users)
    print("Registration successful.")
    return True


def authenticate_user(email, password, users):
    if email in users and check_password(users[email]['hashed_password'], password):
        return True
    return False


def password_recovery(email, users):
    if email in users:
        answer = input(f"Answer the security question to reset your password: {users[email]['security_question']} ")
        if answer == users[email]['security_answer']:
            while True:
                new_password = input("Enter your new password: ")
                if is_valid_password(new_password):
                    users[email]['hashed_password'] = hash_password(new_password)
                    save_users(CSV_FILE, users)
                    print("Password reset successful.")
                    return True
                else:
                    print("Password does not meet the criteria.")
        else:
            print("Incorrect answer to the security question.")
    else:
        print("Email not found.")
    return False

def login(users):
    attempts = 0
    while attempts < MAX_LOGIN_ATTEMPTS:
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if not is_valid_email(email):
            print("Invalid email format.")
            continue

        if authenticate_user(email, password, users):
            print("Login successful!")
            return True
        else:
            print("Invalid email or password.")
            attempts += 1
            print(f"Attempts remaining: {MAX_LOGIN_ATTEMPTS - attempts}")

            if attempts >= MAX_LOGIN_ATTEMPTS:
                print("Too many failed login attempts. Exiting application.")
                sys.exit()
    return False


def get_geolocation(ip=""):
    url = API_URL + ip
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data['status'] == 'success':
            print(f"IP: {data['query']}")
            print(f"Country: {data['country']}")
            print(f"City: {data['city']}")
            print(f"Region: {data['regionName']}")
            print(f"Latitude: {data['lat']}")
            print(f"Longitude: {data['lon']}")
            print(f"Timezone: {data['timezone']}")
            print(f"ISP: {data['isp']}")
        else:
            print("No data found for the entered IP address.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching geolocation data: {e}")


if __name__ == "__main__":
    users = load_users(CSV_FILE)

    while True:
        option = input("Choose an option: [1] Register [2] Login [3] Forgot Password [4] Exit: ")

        if option == "1":
            register_user(users)
        elif option == "2":
            if login(users):
                ip = input("Enter an IP address to get its geolocation (or press Enter for your IP): ")
                get_geolocation(ip)
        elif option == "3":
            email = input("Enter your registered email: ")
            if password_recovery(email, users):
                continue
        elif option == "4":
            print("Exiting application.")
            break
        else:
            print("Invalid option. Please try again.")
