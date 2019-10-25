from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def get_home():
    """
    Create home.html file which is inherited from  base.html
    (must have footer and nav bar from base.html).
    Add two links which will redirect you to pages vegetables and fruits.
    """
    return render_template("home.html")


@app.route("/vegetables")
def get_vegetables():
    """"
    Add endpoint “/vegetables” - will render vegetables.html file,
    pass list of vegetables to your template [beans, carrot, beetroot, cucumber].
    If vegetable is beetroot made it uppercase
    """
    list_of_vegetables = ['beans', 'carrot', 'beetroot', 'cucumber']
    return render_template("vegetables.html", list_of_vegetables=list_of_vegetables)


@app.route("/fruits")
def get_fruits():
    """
    Add endpoint “/fruits” - will render fruits.html file,
    pass list of fruits to your template [melon, apple, strawberry, grape].
    If fruit is strawberry make it red color.
    """
    list_of_fruits = ['melon', 'apple', 'strawberry', 'grape']
    return render_template("fruits.html", list_of_fruits=list_of_fruits)


if __name__ == '__main__':
    app.run(debug=True)

