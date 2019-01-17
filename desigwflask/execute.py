from flask import Flask, render_template , url_for, request ,  redirect

 
username = None

app = Flask(__name__)




@app.route('/')
def home():

    return render_template('index.html', title = 'Home')

@app.route('/aboutus')
def aboutus():

    return render_template('about.html', title = 'About Us')

@app.route('/portfolio')
def portfolio():

    return render_template('portfolio.html', title = 'Portfolio')

@app.route('/product')
def product():

    return render_template('product.html', title = 'Products')

@app.route('/services')
def services():

    return render_template('services.html', title = 'Services')


