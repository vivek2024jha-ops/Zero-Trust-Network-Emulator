import secrets
from datetime import datetime

# Users and their roles
users = {
    "admin": {
        "role": "admin",
        "credential": "Admin@123"
    },
    "analyst": {
        "role": "analyst",
        "credential": "Analyst@123"
    }
}

# Least-privilege access policy
policies = {
    "admin": ["server", "database", "logs"],
    "analyst": ["logs"]
}


def send_slack_alert(message):
    # Demo Slack alert
    print(f"[SLACK ALERT] {message}")


def rotate_credentials(username):
    new_credential = secrets.token_urlsafe(12)
    users[username]["credential"] = new_credential

    print(f"[CREDENTIAL ROTATION] Credential rotated for {username}")

    return new_credential


def authenticate(username, credential):
    if username not in users:
        return False

    return secrets.compare_digest(
        users[username]["credential"],
        credential
    )


def request_access(username, resource, credential):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Authentication check
    if not authenticate(username, credential):

        message = (
            f"{timestamp} | Authentication failed | "
            f"User: {username}"
        )

        print(f"[DENIED] {message}")
        send_slack_alert(message)
        return

    role = users[username]["role"]

    # Authorization / least privilege check
    if resource not in policies.get(role, []):

        message = (
            f"{timestamp} | Unauthorized access attempt | "
            f"{username} ({role}) -> {resource}"
        )

        print(f"[DENIED] {message}")
        send_slack_alert(message)
        return

    print(
        f"[ALLOWED] {timestamp} | "
        f"{username} ({role}) -> {resource}"
    )


def main():

    print("=" * 60)
    print("       ZERO-TRUST NETWORK EMULATOR")
    print("=" * 60)

    # Valid access
    request_access(
        "analyst",
        "logs",
        "Analyst@123"
    )

    # Unauthorized resource
    request_access(
        "analyst",
        "database",
        "Analyst@123"
    )

    # Failed authentication
    request_access(
        "unknown_user",
        "server",
        "wrongpassword"
    )

    # Credential rotation
    new_credential = rotate_credentials("analyst")

    # Access using rotated credential
    request_access(
        "analyst",
        "logs",
        new_credential
    )

    print("=" * 60)


if __name__ == "__main__":
    main()