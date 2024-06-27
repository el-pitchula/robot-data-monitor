from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página de login
@app.route('/')
def login():
    return render_template('login.html')

# Rota para a página de dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Rota para a página de controle manual
@app.route('/controle')
def controle():
    return render_template('controle.html')

if __name__ == '__main__':
    app.run(debug=True)
