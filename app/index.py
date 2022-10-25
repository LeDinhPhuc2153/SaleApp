from flask import render_template, request
from app import app
import utils


@app.route("/")
def home():
    categories = utils.load_category()

    cate_id = request.args.get('category_id')
    kw = request.args.get('keyword')
    products = utils.load_product(category_id=cate_id)
    return render_template('index.html',
                           categories=categories,
                           products=products)


@app.route('/products/<int:product_id>')
def product_detail(product_id):
    p = utils.get_product_by_id(product_id)
    return render_template('details.html', product=p)


if __name__ == '__main__':
    app.run(debug=True)
