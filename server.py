"""Server for Sports Team App"""

import os
from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
from pprint import pprint
from passlib.hash import argon2


secret_key = 'dev'

app = Flask(__name__)
app.secret_key = secret_key
app.jinja_env.undefined = StrictUndefined



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)