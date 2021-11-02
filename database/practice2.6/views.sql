--Views for products table
CREATE OR REPLACE VIEW running_out_of_products AS --products in_stock less or equal 10
    SELECT product_id as id, product_title as title, in_stock as quantity
    FROM products
    WHERE in_stock <= 10;
SELECT * FROM running_out_of_products;


CREATE OR REPLACE VIEW hi_end_products AS  -- products with price more or equal 300
    SELECT product_id as id, product_title as title, price
    FROM products
    WHERE price >= 300
    ORDER BY price;
SELECT * FROM hi_end_products;

CREATE OR REPLACE VIEW running_out_of_hi_end AS -- the most expensive products where in_stock less 11
    SELECT hep.id, hep.title, hep.price, quantity
    FROM running_out_of_products
    JOIN hi_end_products hep on running_out_of_products.title = hep.title;
SELECT * FROM running_out_of_hi_end;

DROP VIEW IF EXISTS running_out_of_products, hi_end_products, running_out_of_hi_end;

--Views for order and order status tables
CREATE OR REPLACE VIEW finished_order AS  -- finished orders
    SELECT mo.order_id, mo.total, mo.updated_at, os.status_name
    FROM m_order mo
    JOIN order_status os on os.order_status_id = mo.order_status_order_status_id
    WHERE os.status_name = 'Finished';
SELECT * FROM finished_order;

CREATE OR REPLACE VIEW total_lost_canceled AS --total sum that lost due to canceling order
    SELECT SUM(total) FROM m_order
    LEFT JOIN order_status os on os.order_status_id = m_order.order_status_order_status_id
    WHERE os.status_name = 'Canceled';
SELECT * FROM total_lost_canceled;

CREATE OR REPLACE VIEW  top_successful_days AS --The top 10 of days when order was paid
    SELECT SUM(total), mo.updated_at
    FROM m_order mo
    JOIN order_status os on os.order_status_id = mo.order_status_order_status_id
    WHERE os.status_name = 'Paid'
    GROUP BY mo.updated_at
    ORDER BY SUM(total) DESC
    LIMIT 10;
SELECT * FROM top_successful_days;

DROP VIEW IF EXISTS finished_order, total_lost_canceled, top_successful_days;

--Views for products and category tables
CREATE OR REPLACE VIEW count_products_by_category AS --number of products in each category
    SELECT COUNT(p.product_id) AS count, c.category_title
    FROM products p
    JOIN categories c on c.category_id = p.category_id
    GROUP BY c.category_title
    ORDER BY count DESC ;
SELECT * FROM count_products_by_category;

CREATE OR REPLACE VIEW products_sum_in_category AS  --total sum of products in each category
    SELECT ROUND(SUM(p.price*p.in_stock),2) AS sum, c.category_title
    FROM products p
    JOIN categories c on c.category_id = p.category_id
    GROUP BY c.category_title
    ORDER BY sum DESC ;
SELECT * FROM products_sum_in_category;

CREATE OR REPLACE VIEW product_with_category AS  --display product with category
    SELECT p.product_title AS title, p.in_stock AS quantity,
           p.price, c.category_title AS category
    FROM products p
    JOIN categories c on p.category_id = c.category_id;
SELECT * FROM product_with_category;

DROP VIEW count_products_by_category, product_with_category, products_sum_in_category;


--Materialized view

CREATE MATERIALIZED  VIEW user_orders_summ
AS
    SELECT SUM(m_order.total), u.user_id FROM m_order
    JOIN carts c on c.cart_id = m_order.carts_cart_id
    JOIN users u on u.user_id = c.users_user_id
    JOIN order_status os on os.order_status_id = m_order.order_status_order_status_id
    WHERE os.status_name = 'Fineshed' OR os.status_name = 'Paid'
    GROUP BY u.user_id
    ORDER BY u.user_id
WITH NO DATA;
REFRESH MATERIALIZED VIEW user_orders_summ;
SELECT * FROM user_orders_summ;
DROP MATERIALIZED VIEW IF EXISTS user_orders_summ;




