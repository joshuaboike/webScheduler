from flask import Flask
from flask import render_template
import os

schedule_api_consumer_key = 'BFJomKU_A7GjchucbDjAuPlMun4a'
schedule_api_secret_key   = 'fIKZn4rnkkqs6VsQvrDFek04qVAa'
app = Flask(__name__)

app.secret_key = os.urandom(24)