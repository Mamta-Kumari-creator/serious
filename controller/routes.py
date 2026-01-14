from main import app
from flask import render_template, request, redirect, url_for, flash, session
from controller.models import *

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

