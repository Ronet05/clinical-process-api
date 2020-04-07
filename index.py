from flask import Flask, render_template, request, url_for, json
import requests
import csv
from api_eicu import eicu_parser

app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/')
@app.route('/dashboard')

def form_input():
    list_values = [1,3,4,6]
    parser = eicu_parser()
    cols_in_json = parser.show_vars(list_values)
    return render_template('dashboard.html', cols = cols_in_json)


