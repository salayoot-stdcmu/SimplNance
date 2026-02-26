from flask import Flask, render_template
from fastapi import FastAPI

app = Flask(__name__, static_folder="../frontend/src/static", template_folder="../frontend/src/routes")
# print(app.url_map)

@app.route("/")
def home():
    print("HOME HIT")
    return "OK"

@app.get("/check_error")
def check_error():
    # Simulate an error for testing purposes
    raise 1/0

@app.get("/base")
def main():
    return render_template('app.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8282, debug=True)