from flask import Blueprint, request, render_template, flash, abort, redirect, url_for
from supermarkets.work_with_file import load_market_data, save_market_data
from supermarkets.form_market import AddMarket
from werkzeug.utils import secure_filename
import os

market = Blueprint('markets',
                   __name__,
                   template_folder='templates',
                   static_folder='static',
                   static_url_path='/static/markets')


@market.route('/supermarket', methods=['POST', 'GET'])
def get_all_markets():

    if request.method == 'GET':
        data = load_market_data()
        if request.args:
            for arg, value in request.args.items():
                if value:
                    data = [prod for prod in data if prod.get(arg) == value]
        if data:
            return render_template('all_supermarkets.html', data=data)
        else:
            abort(404)


@market.route('/supermarket/<int:id>')
def get_market(id):
    try:
        all_data = load_market_data()
        data = [market for market in all_data if market.get('id') == id]
        return render_template('supermarket.html', data=data[0])
    except IndexError:
        abort(404)


@market.route('/add_supermarket', methods=['POST', 'GET'])
def add_market():
    form = AddMarket()
    all_data = load_market_data()

    if form.validate_on_submit():
        last_id = max(all_data, key=lambda x: x['id'])['id']

        file_name = secure_filename(form.market_img_name.data.filename)
        form.market_img_name.data.save(os.path.join('supermarkets/static', file_name))

        new_data = {
            'id': last_id + 1,
            'name': form.market_name.data,
            "location": form.market_location.data,
            'img_name': file_name
        }
        save_market_data(new_data=new_data)
        return redirect(url_for('markets.get_all_markets'))

    return render_template('add_supermarket.html', form_market=form)


@market.errorhandler(404)
def handle_404(error):
    return render_template('error_404.html')
