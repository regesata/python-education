COPY carts(cart_id, users_user_id, subtotal,
           total, timestamp)
FROM '/usr/src/carts.csv'
DELIMITER ',';

COPY categories(category_id, category_title, category_description)
FROM '/usr/src/categories.csv'
DELIMITER ',';

COPY products(product_id, product_title,product_description, in_stock, price, slug, category_id)
FROM '/usr/src/products.csv'
DELIMITER ',';

COPY m_order(order_id, carts_cart_id, order_status_order_status_id, shipping_total, total,
    created_at, updated_at)
FROM '/usr/src/orders.csv'
DELIMITER ',';

COPY order_status(order_status_id, status_name)
FROM '/usr/src/order_statuses.csv'
DELIMITER ',';

COPY carts_product(carts_cart_id, products_product_id)
FROM '/usr/src/cart_products.csv'
DELIMITER ',';