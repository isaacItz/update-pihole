#!/usr/bin/python3

import time
import socket

local_db = {}

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

def update_ips_file(file_path, domain, new_ip):
  #read file
  with open(file_path, 'r') as file:
    lines = file.readlines()

  #update the ips
  updated_lines = []
  for line in lines:
    if domain in line:
      parts = line.split("/")
      new_line = f"{'/'.join(parts[0:2])}/{new_ip}\n"
      updated_lines.append(new_line)
    else:
      updated_lines.append(line)

    #remove \n from each line
    #updated_lines = [line.strip() for line in updated_lines]

    # for test purposes we won't change the original file
    with open(f"{file_path}.test", 'w') as file:
    #with open(file_path, 'w') as file:
      for line in updated_lines:
        file.write(line)

  return updated_lines

def check_changes(ip, domain):
  global local_db
  return local_db[domain] != ip:

  with open(file, 'r') as file:
    lines = file.readlines()

  for line in lines:
    if domain in line:
      return True;
  return True;



if __name__ == "__main__":
  while True:
    ip = get_local_ip()
    domain = 'ivl.pro'
    file = './99-openshift.conf'

    print(f"Local IP Address: {ip}")
    #we won't do anything if Network is Unreachable
    if ip == None:
      pass

    if domain in local_db:
      if check_changes(ip, domain):
        print('actualizamos la db ')
        newips = update_ips_file(file, domain, ip)
        local_db[domain] = ip
    else:
      print('guardamos por que no existe el dominio en la bd')
      newips = update_ips_file(file, domain, ip)
      local_db[domain] = ip

    time.sleep(5)
