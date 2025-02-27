from flask import Flask
import ssl

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>PRONOB Secure Server is Running with SSL!</h1>"

if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="certificate.pem", keyfile="privateKey.pem")
    
    app.run(host="0.0.0.0", port=8080, debug=True, ssl_context=context)
