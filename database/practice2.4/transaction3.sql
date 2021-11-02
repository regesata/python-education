BEGIN;

ALTER TABLE products
    DROP CONSTRAINT products_category_id_fkey;

ALTER TABLE carts_product
    DROP CONSTRAINT  carts_product_products_product_id_fkey;

ALTER TABLE products
ADD CONSTRAINT products_category_id_fkey
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
    ON DELETE CASCADE ;

ALTER TABLE carts_product
ADD CONSTRAINT carts_product_products_product_id_fkey
    FOREIGN KEY (products_product_id) REFERENCES products(product_id)
    ON DELETE CASCADE;
COMMIT;


BEGIN;

SAVEPOINT deletion;
DELETE FROM categories WHERE category_id = 1;
ROLLBACK TO SAVEPOINT deletion;

INSERT INTO categories(category_id, category_title, category_description)
VALUES (21, 'Title 21', 'Description title 21');
--Creates new order, cart and puts products to cart
INSERT INTO carts(cart_id, users_user_id, subtotal, total, timestamp) VALUES
(2001, 150, 350.11, 350.11, now());

INSERT INTO carts_product(carts_cart_id, products_product_id) VALUES
(2001, 85),
(2001, 99),
(2001, 100);

INSERT INTO m_order(order_id, carts_cart_id, order_status_order_status_id,
                    shipping_total, total, created_at, updated_at) VALUES
(1501, 2001, 1, 30, 350.11, now(), now());


SAVEPOINT update_order_status;
UPDATE m_order SET order_status_order_status_id = 2
WHERE order_id = 1501;
ROLLBACK TO SAVEPOINT  update_order_status;

RELEASE SAVEPOINT update_order_status;
RELEASE SAVEPOINT deletion;
COMMIT;











