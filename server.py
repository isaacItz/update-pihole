from flask import Flask, request, jsonify
from main import IPConfigUpdater
import os
#print(dir(main))
file_name = os.getenv('FILE_PATH', '99-openshift.conf.test')

ip_manager = IPConfigUpdater(file_name)

app = Flask(__name__)

@app.route('/ip', methods=['POST'])
def receive_ip():
    data = request.get_json()
    print(f"data: {data}")
    ip_address = data.get('ip')
    domain = data.get('domain')

    if not ip_address:
        return jsonify({"error": "No IP address provided"}), 400

    if not ip_manager.has_domain(domain) or ip_manager.has_ip_changed(ip_address, domain):
        ip_manager.update_ips_file(domain, ip_address)

    response = {"message": "OK"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
