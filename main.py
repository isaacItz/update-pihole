#!/usr/bin/python3

class IPConfigUpdater:

  def __init__(self, file_path):
    self.local_db = {}
    self.file_path = file_path

  def update_ips_file(self, domain, new_ip):
    #read file
    with open(self.file_path, 'r') as file:
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
      with open(f"{self.file_path}.test", 'w') as file:
      #with open(file_path, 'w') as file:
        for line in updated_lines:
          file.write(line)

    self.local_db[domain] = new_ip

    return updated_lines

  def has_domain(self, domain):
    return domain in self.local_db

  def has_ip_changed(self, ip, domain):
    return self.local_db[domain] != ip

    with open(file, 'r') as file:
      lines = file.readlines()

    for line in lines:
      if domain in line:
        return True;
    return True;
