#!/bin/env python 
import sys
import requests
import json

requests.packages.urllib3.disable_warnings()

if len(sys.argv) != 3:
    print("usage: python script.py <ip> <user>")
    sys.exit(1)

IP_ADDRESS = sys.argv[1]
USER = sys.argv[2]

def make_user_request(ip, user, ignoreError=False):
    url = f"https://{ip}/api/user"
    headers = {
        "Content-Type": "application/json",
        "X-Api-Version": "2"
    }
    payload = {"name": f"local/{user}"}
    
    response = requests.post(url, headers=headers, json=payload, verify=False)
    
    if ignoreError and response.status_code == 403:
        return None

    response.raise_for_status()
    reply = response.json()

    print(f"User {user} created successfully with token {reply.get('token', 'NO TOKEN!')}")
    return reply.get('token')


def check_device(ip, token):
    url = f"https://{ip}/api"
    headers = {
        "Authorization": f"Bearer {token}",
        "X-Api-Version": "2"
    }

    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()
    print(response.json())

def check_users(ip, token):
    url = f"https://{ip}/api/user"
    headers = {
        "Authorization": f"Bearer {token}",
        "X-Api-Version": "2"
    }

    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()
    print(response.json())

# First POST request, should fail
make_user_request(ip=IP_ADDRESS, user=USER, ignoreError=True)
input("Press key on device, then press Enter to continue...")
# Second POST request, returns token
token = make_user_request(IP_ADDRESS, USER)
check_device(IP_ADDRESS, token)
check_users(IP_ADDRESS, token)



