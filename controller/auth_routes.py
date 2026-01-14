from main import app
from flask import render_template, request, redirect, url_for, flash, session
from controller.models import *

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('base.html')
    if 'user_email' in session:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('password')
        # Add your authentication logic here
        if not username or not password:
            flash('Please enter both username and password', 'error')
            return redirect(url_for('login'))
        if '@' not in username:
            flash('Invalid email format', 'error')
            return redirect(url_for('login'))
        
        #query database to check if user exists
        user=User.query.filter_by(user_email=username).first()
        if not user:
            flash('User does not exist')
            return redirect(url_for('login'))
        if user.passsword != password:
            flash('Incorrect password')
            return redirect(url_for('login'))

        # if username == 'admin' and password == 'password':
        #     session['username'] = username
        #     flash('Login successful!', 'success')
        #     return redirect(url_for('dashboard'))
        # else:
        #     flash('Invalid credentials', 'error')

        session['user_email'] = user.user_email
        session['user_role'] = [role.name for role in user.roles]
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))