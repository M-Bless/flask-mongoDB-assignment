from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)