from flask import Blueprint, jsonify, request, render_template, flash, abort, redirect, url_for, session
from products.work_with_json import load_prod_data, save_prod_data
from products.form_product import AddProduct
from werkzeug.utils import secure_filename
import os


product = Blueprint('products',
                    __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/static/products')


@product.route('/product', methods=['GET', 'POST'])
def get_all_products():

    if request.method == 'GET':
        data = load_prod_data()

        if request.args:
            for arg, value in request.args.items():
                if value:
                    data = [prod for prod in data if prod.get(arg) == value]

        if data:
            return render_template("all_products.html", data=data)
        else:
            abort(404)


@product.route('/product/<int:id>')
def get_product(id):
    try:
        all_data = load_prod_data()
        data = [prod for prod in all_data if prod.get('id') == id]
        session[data[0]['name']] = True
        return render_template('product.html', data=data[0])
    except IndexError:
        abort(404)


@product.route('/add_product', methods=['POST', 'GET'])
def add_product():
    all_data = load_prod_data()
    form = AddProduct()
    if form.validate_on_submit():

        last_product_id = max(load_prod_data(), key=lambda x: x['id'])['id']   # last id

        file_name = secure_filename(form.product_img_name.data.filename)
        form.product_img_name.data.save(os.path.join('products/static', file_name))

        new_product = {
            'id': last_product_id + 1,
            'name': form.product_name.data,
            "description": form.product_description.data,
            'img_name': file_name,
            'price': form.product_price.data
        }
        save_prod_data(new_data=new_product)
        return redirect(url_for('products.get_all_products'))

    return render_template('add_product.html', form=form)


@product.errorhandler(404)
def handle_404(error):
    return render_template('error_404.html')


@product.route('/clear_session', methods=['POST', 'GET'])
def clear_sesion():
    prod_name = [prod.get('name') for prod in load_prod_data()]
    for prod in prod_name:
        if session[prod]:
            session[prod] = False
    return 'ok'
