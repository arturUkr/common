from flask import Flask, render_template
from utils import get_data, prepare_str


app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data())


@app.route("/author")
def get_author():
    dict_of_link = {prepare_str(x.get('title')): x.get('title') for x in get_data()}
    return render_template("author.html", dict_of_link=dict_of_link)


@app.route('/<page_name>')
def get_page(page_name):
    obj = prepare_str(page_name)
    obj_text = [x.get('text') for x in get_data() if prepare_str(x.get('title')) == obj]
    dict_of_link = {prepare_str(x.get('title')): x.get('title') for x in get_data()}
    if obj_text:
        return render_template("base_page.html", title=obj, text=obj_text[0], dict_of_link=dict_of_link)
    else:
        return render_template("error_page.html", title=page_name, dict_of_link=dict_of_link)


if __name__ == "__main__":
    app.run(debug=True)
