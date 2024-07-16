# your_secure_admin_password
from flask import Flask, request, jsonify, send_from_directory, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
import os
import subprocess

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///local.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy, Bcrypt, and Migrate
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    second_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    compiled_code = db.Column(db.Text, nullable=True)

# Admin model
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Function to create admin user (initialize once)
def create_admin():
    with app.app_context():
        admin_username = 'admin'
        admin_password = 'your_secure_admin_password'  # Change this to a secure admin password

        hashed_password = bcrypt.generate_password_hash(admin_password).decode('utf-8')
        admin = Admin.query.filter_by(username=admin_username).first()
        if not admin:
            admin = Admin(username=admin_username, password=hashed_password)
            db.session.add(admin)
            db.session.commit()

# Ensure admin user exists
create_admin()




# Serve login page as default route
@app.route('/')
def login_page():
    return send_from_directory('frontend', 'login.html')

# Serve static files (styles.css and script.js)
@app.route('/frontend/<path:path>')
def send_static(path):
    return send_from_directory('frontend', path)

# Handle user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful', 'redirect': url_for('index')})
    return jsonify({'message': 'Invalid credentials'}), 401

# Handle admin login
@app.route('/admin/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    admin = Admin.query.filter_by(username=data['username']).first()
    if admin and bcrypt.check_password_hash(admin.password, data['password']):
        session['admin_id'] = admin.id
        return jsonify({'message': 'Login successful', 'redirect': url_for('admin_page')})
    return jsonify({'message': 'Invalid credentials'}), 401

# Serve index.html if logged in
@app.route('/index')
def index():
    if 'user_id' in session:
        return send_from_directory('frontend', 'index.html')
    return redirect(url_for('login_page'))

# Handle R code compilation request
@app.route('/compile', methods=['POST'])
def compile_code():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401

    data = request.get_json()
    code = data['code']

    # Temporary file to store R code
    with open('temp.R', 'w') as file:
        file.write(code)

    # Run R script and capture output
    result = subprocess.run(['Rscript', 'temp.R'], capture_output=True, text=True)
    output = result.stdout.strip()
    error = result.stderr.strip()

    # Save compiled code to user
    user = User.query.get(session['user_id'])
    user.compiled_code = output + '\n\n' + error + ('\n[Execution complete with exit code 1]' if error else '\n[Execution complete with exit code 0]')
    db.session.commit()

    if error:
        return jsonify({'output': output + '\n\n' + error + '\n[Execution complete with exit code 1]'})
    return jsonify({'output': output + '\n[Execution complete with exit code 0]'})

# Handle user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(
        first_name=data['first_name'],
        second_name=data['second_name'],
        email=data['email'],
        password=hashed_password
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Registration successful', 'redirect': url_for('login_page')})

# Handle user logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login_page'))

# Admin page
@app.route('/admin')
def admin_page():
    if 'admin_id' not in session:
        return redirect(url_for('admin_login_page'))
    return send_from_directory('frontend', 'admin.html')

# Admin page for deleting users
@app.route('/admin/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if 'admin_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})

# Fetch user details for admin page
@app.route('/admin/users')
def get_users():
    if 'admin_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401

    users = User.query.all()
    user_list = [{'id': user.id, 'first_name': user.first_name, 'second_name': user.second_name, 'email': user.email, 'compiled_code': user.compiled_code} for user in users]
    return jsonify({'users': user_list})

# Example of changing password
if __name__ == '__main__':
        app.run(debug=False)

