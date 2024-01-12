"""Server for Sports Team App"""

import os
from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
from pprint import pprint
from passlib.hash import argon2