--Index reduces Execution time from 0.9 ms to 0.1 ms
BEGIN;
CREATE INDEX ON carts_product(carts_cart_id);
EXPlAIN (ANALYSE) SELECT u.last_name, u.first_name, p.product_title FROM carts_product
JOIN carts c on c.cart_id = carts_product.carts_cart_id
JOIN users u on u.user_id = c.users_user_id
JOIN products p on p.product_id = carts_product.products_product_id
WHERE carts_cart_id = 300;
ROLLBACK;