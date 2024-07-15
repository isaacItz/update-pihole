#!/usr/bin/python3

import requests
import json
import os
import time
import socket

def get_local_ip():
  try:
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Connect to a remote server (doesn't need to be reachable)
    s.connect(("8.8.8.8", 80))

    # Get the local IP address associated with this socket
    local_ip = s.getsockname()[0]
  except OSError as e:
    print(f"Network may be unavailable {e}")
    return None;
  finally:
    # Close the socket
    s.close()

  return local_ip

if __name__ == "__main__":
  last_ip = None
  while True:
    ip = get_local_ip()
    domain = os.getenv('DOMAIN', 'ivl.pro')

    print(f"Local IP Address: {ip}")
    #we won't do anything if Network is Unreachable
    if ip != None and ip != last_ip:
      host = os.getenv('HOST', 'ips.ivl.pro')
      port = os.getenv('PORT', '443')
      protocol = os.getenv('PROTO', 'http')
      url = f'{protocol}://{host}:{port}/ip'
      print(url)
      data = {
        "ip": ip,
        "domain": domain
      }
      headers = {
        'Content-Type': 'application/json'
      }
      try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        print(response.text)
        last_ip = ip
      except Exception as e:
        print(f'probmema al hacer la solicitud: {e}')

    time.sleep(60)
