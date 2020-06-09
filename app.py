from flask import Flask, request
import git
app = Flask(__name__)

@app.route('/')
def home():
    return 'Cool site coming soon'
