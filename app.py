# Create a folder for your project, and within that folder, create a Python file (e.g., app.py).

# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
