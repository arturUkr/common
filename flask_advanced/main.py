from flask import Flask, render_template
from products.main_products import product
from supermarkets.main_market import market
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(product)
app.register_blueprint(market)

@app.route('/home')
def get_home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
