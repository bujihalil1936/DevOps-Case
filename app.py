from kubernetes import client, config
from flask import Flask, jsonify
import base64
import ssl
from datetime import datetime

app = Flask(__name__)

def get_certificate_expiry(certificate_pem):
    certificate = ssl.PEM_cert_to_DER_cert(certificate_pem)
    x509 = ssl.DER_cert_to_X509(certificate)
    return x509.get_notAfter().decode('ascii')

def load_kube_config():
    try:
        config.load_kube_config()
    except:
        config.load_incluster_config()

def get_certificate_info():
    load_kube_config()
    v1 = client.CoreV1Api()
    secrets = v1.list_secret_for_all_namespaces()

    cert_info = []
    for secret in secrets.items:
        if secret.type == "kubernetes.io/tls":
            cert_data = secret.data.get("tls.crt")
            if cert_data:
                cert_pem = base64.b64decode(cert_data).decode('utf-8')
                expiry_date = get_certificate_expiry(cert_pem)
                cert_info.append({
                    "namespace": secret.metadata.namespace,
                    "name": secret.metadata.name,
                    "expiry_date": expiry_date
                })
    return cert_info

@app.route('/certificates', methods=['GET'])
def certificates():
    cert_info = get_certificate_info()
    return jsonify(cert_info)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
