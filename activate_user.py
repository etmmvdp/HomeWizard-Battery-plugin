#!env python
import sys
import requests

# Disable warnings about insecure HTTPS requests
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def make_user_request(ip, user, ignore_error=False):
    """Make a POST request to create a user."""
    url = f"https://{ip}/api/user"
    headers = {
        "Content-Type": "application/json",
        "X-Api-Version": "2"
    }
    payload = {"name": f"local/{user}"}

    try:
        response = requests.post(url, headers=headers, json=payload, verify=False)
        response.raise_for_status()
        
        reply = response.json()
        print(f"User {user} created successfully with token {reply.get('token', 'NO TOKEN!')}")
        return reply.get('token')
    
    except requests.exceptions.HTTPError as err:
        if ignore_error and response.status_code == 403:
            return None
        print(f"HTTP error occurred: {err}")
        sys.exit(1)

def check_device(ip, token):
    """Check device status with a GET request."""
    url = f"https://{ip}/api"
    headers = {
        "Authorization": f"Bearer {token}",
        "X-Api-Version": "2"
    }

    try:
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()
        print(response.json())
    
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        sys.exit(1)

def check_users(ip, token):
    """Check the list of users with a GET request."""
    url = f"https://{ip}/api/user"
    headers = {
        "Authorization": f"Bearer {token}",
        "X-Api-Version": "2"
    }

    try:
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()
        print(response.json())

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        sys.exit(1)

def main():
    """Main function to coordinate user and device interactions."""
    if len(sys.argv) != 3:
        print("Usage: python script.py <ip> <user>")
        sys.exit(1)

    ip_address, user = sys.argv[1], sys.argv[2]

    # First POST request, should fail (ignore errors)
    make_user_request(ip_address, user, ignore_error=True)

    input("Press key on device, then press Enter to continue...")

    # Second POST request, returns token
    token = make_user_request(ip_address, user)
    check_device(ip_address, token)
    check_users(ip_address, token)

if __name__ == "__main__":
    main()

