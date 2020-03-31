from flask import Flask, render_template, request, url_for
import requests
import csv

app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/')
@app.route('/dashboard')

def upload():
    return render_template('dashboard.html')
