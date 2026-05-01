from flask import Flask, render_template, request, redirect, session, jsonify
import psutil

app = Flask(__name__)
app.secret_key = "secret123"

USERNAME = "admin"
PASSWORD = "admin"

# Initialize CPU measurement (IMPORTANT to avoid 0%)
psutil.cpu_percent(interval=None)


# 🔐 LOGIN ROUTE
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['user'] = request.form['username']
            return redirect('/dashboard')
    return render_template("login.html")


# 📊 DASHBOARD PAGE
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return render_template("index.html")


# 🔄 LIVE DATA API (VERY IMPORTANT)
@app.route('/data')
def data():
    cpu = psutil.cpu_percent(interval=None)
    memory = psutil.virtual_memory().percent

    return jsonify({
        "cpu": cpu,
        "memory": memory
    })


# 🚀 RUN APP
if __name__ == "__main__":
    app.run(debug=True)