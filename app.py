from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True  # Set debug mode to True

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return "This is the dashboard"
@app.route('/place_order')
def place_order():
    return "This is the dashboard"

if __name__ == '__main__':
    app.run()
