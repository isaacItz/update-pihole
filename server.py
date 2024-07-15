from flask import Flask, request, jsonify
from main import IPConfigUpdater
import os
#print(dir(main))
file_name = os.getenv('FILE_PATH', '99-openshift.conf.test')

ip_manager = IPConfigUpdater(file_name)
ip_manager.backup_file()

app = Flask(__name__)

@app.route('/ip', methods=['POST'])
def receive_ip():
    data = request.get_json()
    print(f"data: {data}")
    ip_address = data.get('ip')
    domain = data.get('domain')

    valid = validate(data)
    if not valid[0]:
        return valid[1:]

    if not ip_manager.has_domain(domain) or ip_manager.has_ip_changed(ip_address, domain):
        ip_manager.update_ips_file(domain, ip_address)

    response = {"message": "OK"}
    return jsonify(response)

def validate(data):
    valid = True
    err = {"error": ""}
    code = 200
    if not data.get('ip'):
        err["error"] = "No IP address provided"
        code = 400
        valid = False
    if not data.get('domain'):
        err["error"] = "No Domain provided"
        code = 400
        valid = False

    return valid, err, code

if __name__ == '__main__':
    app.run()
