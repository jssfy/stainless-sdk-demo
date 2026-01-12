# Users

Types:

```python
from python_demo.types import User, UserListResponse
```

Methods:

- <code title="post /users">client.users.<a href="./src/python_demo/resources/users.py">create</a>(\*\*<a href="src/python_demo/types/user_create_params.py">params</a>) -> <a href="./src/python_demo/types/user.py">User</a></code>
- <code title="get /users/{id}">client.users.<a href="./src/python_demo/resources/users.py">retrieve</a>(id) -> <a href="./src/python_demo/types/user.py">User</a></code>
- <code title="put /users/{id}">client.users.<a href="./src/python_demo/resources/users.py">update</a>(id, \*\*<a href="src/python_demo/types/user_update_params.py">params</a>) -> <a href="./src/python_demo/types/user.py">User</a></code>
- <code title="get /users">client.users.<a href="./src/python_demo/resources/users.py">list</a>(\*\*<a href="src/python_demo/types/user_list_params.py">params</a>) -> <a href="./src/python_demo/types/user_list_response.py">UserListResponse</a></code>
- <code title="delete /users/{id}">client.users.<a href="./src/python_demo/resources/users.py">delete</a>(id) -> None</code>

# Products

Types:

```python
from python_demo.types import Product, ProductListResponse
```

Methods:

- <code title="post /products">client.products.<a href="./src/python_demo/resources/products.py">create</a>(\*\*<a href="src/python_demo/types/product_create_params.py">params</a>) -> <a href="./src/python_demo/types/product.py">Product</a></code>
- <code title="get /products/{id}">client.products.<a href="./src/python_demo/resources/products.py">retrieve</a>(id) -> <a href="./src/python_demo/types/product.py">Product</a></code>
- <code title="get /products">client.products.<a href="./src/python_demo/resources/products.py">list</a>(\*\*<a href="src/python_demo/types/product_list_params.py">params</a>) -> <a href="./src/python_demo/types/product_list_response.py">ProductListResponse</a></code>

# Orders

Types:

```python
from python_demo.types import Order, OrderItem, OrderStatus, OrderListResponse
```

Methods:

- <code title="post /orders">client.orders.<a href="./src/python_demo/resources/orders.py">create</a>(\*\*<a href="src/python_demo/types/order_create_params.py">params</a>) -> <a href="./src/python_demo/types/order.py">Order</a></code>
- <code title="get /orders">client.orders.<a href="./src/python_demo/resources/orders.py">list</a>(\*\*<a href="src/python_demo/types/order_list_params.py">params</a>) -> <a href="./src/python_demo/types/order_list_response.py">OrderListResponse</a></code>
