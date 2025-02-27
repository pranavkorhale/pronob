from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static")

@app.route("/")
def serve_index():
    return send_from_directory("static", "index.html")

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host="0.0.0.0", port=8080, debug=True)  # No SSL
=======
    app.run(host="0.0.0.0", port=8080, debug=True)  # No SSL
>>>>>>> 66de6c4 (change in code=> commit for PRONOB static site)
