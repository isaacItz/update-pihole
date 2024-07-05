#!/usr/bin/python3
import socket

def get_local_ip():
  try:
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Connect to a remote server (doesn't need to be reachable)
    s.connect(("8.8.8.8", 80))
    
    # Get the local IP address associated with this socket
    local_ip = s.getsockname()[0]
  finally:
    # Close the socket
    s.close()
  
  return local_ip

def update_ips_file(file_path, new_ip):
  #read file
  with open(file_path, 'r') as file:
    lines = file.readlines()
  
  domain = 'ivl.pro'

  #update the ips
  updated_lines = []
  for line in lines:
    if domain in line:
      parts = line.split("/")
      new_line = f"{'/'.join(parts[0:2])}/{new_ip}"
      updated_lines.append(new_line)
    else:
      updated_lines.append(line)
  for i in updated_lines:
    print(i)

if __name__ == "__main__":
  ip = get_local_ip()
  print(f"Local IP Address: {ip}")
  update_ips_file("./99-openshift.conf", ip)
  
    
