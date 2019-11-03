
### Main:

* ```config.py``` - секретний ключ;



### Blueprint Products:

* ```/product``` - список продуктів із посиланнями на ```/product/<id>```, із фільтрацією, наприклад ```/product?price=25.5&name=snikers```;

* ```/product/<id>``` - сторінка продукту;

* ```/add_product``` - форма для додавання продукту в json-файл із списков продуктів;

* ```list_product.json``` - json-файл із списком продуктів;



### Blueprint Supermarkets:

* ```/supermarket``` - список маркетів із посиланнями на ```/supermarket/<id>```, із фільтрацією, наприклад ```/supermarket?location=Kyiv```;

* ```/supermarket/<id>``` - сторінка маркету;

* ```/add_supermarket``` - форма для додавання маркету в json-файл із списков маркетів;

* ```list_markets.json``` - json-файл із списком маркетів;



### Error handler:

* для ```/product/<id>``` і ```/supermarket/<id>``` - неправильний ```<id>```;
* для фільтрації - проблеми із фільтрами, наприклад ```http://127.0.0.1:5000/product?price=25.5&name=aaa```;



### Session:

* для продуктів реалізовано на сторінці ```/product```, якщо був клік по продукту, то пропадає посилання;

* ```/clear_session``` - очистити із сесії назви продуктів, всі посилання на ```/product``` стають клікабельні;
