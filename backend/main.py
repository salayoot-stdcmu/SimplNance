from flask import Flask, render_template
from fastapi import FastAPI

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello, World!"

@app.get("/check_error")
def check_error():
    # Simulate an error for testing purposes
    raise 1/0

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8282, debug=True)