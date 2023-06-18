from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/detail/mie_ayam')
def detail():
    return render_template('detail.html')

@app.route('/pembayaran')
def pembayaran():
    return render_template('payment.html')

if __name__ == '__main__':
    app.run()