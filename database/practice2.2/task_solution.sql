--Task 1
--1.1
SELECT first_name AS Name, last_name AS Last_name,
       middle_name
FROM users;
--1.2
SELECT product_title, product_description, in_stock,
       price
FROM products
ORDER BY product_id;
--1.3
SELECT order_status_id AS ID, status_name AS Title
FROM order_status;
--Task 2
SELECT order_id, created_at, total, order_status_order_status_id
FROM m_order m
WHERE m.order_status_order_status_id IN (3, 4);

SELECT order_id, created_at, total, order_status_order_status_id
FROM m_order m
WHERE m.order_status_order_status_id BETWEEN 3 AND 4;

--Task 3
--3.1
SELECT * FROM products
WHERE price > 80.00 AND price <=150.00
ORDER BY price;

SELECT * FROM products
WHERE price BETWEEN 80.00 AND 150.00
    AND price <> 80
ORDER BY price;

SELECT * FROM(
    SELECT * FROM products WHERE price <=150.00
)AS a WHERE price > 80.00
ORDER BY price;

--3.2
SELECT order_id AS ID, created_at AS Date
    FROM m_order
WHERE created_at > to_date('20201001', 'YYYYMMDD')
ORDER BY created_at;

--3.3
SELECT order_id AS ID, created_at AS Date
    FROM m_order
WHERE created_at >= to_date('20200101', 'YYYYMMDD')
    AND created_at <= to_date('20200630', 'YYYYMMDD')
ORDER BY created_at;

SELECT order_id AS ID, created_at AS Date
    FROM m_order
WHERE created_at BETWEEN to_date('20200101', 'YYYYMMDD')
    AND to_date('20200630', 'YYYYMMDD')
ORDER BY created_at;

SELECT order_id AS ID, created_at AS Date FROM
(SELECT * FROM m_order WHERE created_at >=to_date('20200101', 'YYYYMMDD'))
AS a WHERE a.created_at <=to_date('20200630', 'YYYYMMDD')
ORDER BY a.created_at;

--3.4
SELECT p.product_title AS title, category_title AS category
FROM products p
JOIN  categories c ON p.category_id = c.category_id
WHERE c.category_title IN ('Category 7', 'Category 11', 'Category 18')
ORDER BY  c.category_id;

SELECT p.product_title AS title, category_title AS category
FROM products p
JOIN  categories c ON p.category_id = c.category_id
WHERE c.category_title LIKE 'Category 7'
    OR c.category_title LIKE 'Category 11'
    OR c.category_title LIKE 'Category 18'
ORDER BY  c.category_id;

SELECT p.product_title AS title, category_title AS category
FROM products p
JOIN  categories c ON p.category_id = c.category_id
WHERE c.category_title ='Category 7'
UNION ALL
SELECT p.product_title AS title, category_title AS category
FROM products p
JOIN  categories c ON p.category_id = c.category_id
WHERE c.category_title ='Category 11'
UNION ALL
SELECT p.product_title AS title, category_title AS category
FROM products p
JOIN  categories c ON p.category_id = c.category_id
WHERE c.category_title ='Category 18';

--3.5
SELECT m.order_id AS ID, s.status_name AS status, m.created_at
FROM m_order m
JOIN order_status s ON m.order_status_order_status_id =s.order_status_id
WHERE s.status_name IN ('Accepted', 'In progress', 'Paid')
    AND m.created_at < to_date('20201231', 'YYYYMMDD')
ORDER BY m.created_at;

--3.6
SELECT c.cart_id FROM m_order
RIGHT JOIN carts c ON c.cart_id = m_order.carts_cart_id
WHERE carts_cart_id is NULL;

--Task 4
--4.1
SELECT order_status_order_status_id AS status,
       CAST(AVG(total) AS money) AS average
FROM m_order m
GROUP BY order_status_order_status_id
HAVING  order_status_order_status_id = 4;

SELECT max(total)  AS max
FROM m_order m
WHERE created_at BETWEEN to_date('20200701', 'YYYYMMDD')
        AND to_date('20200930', 'YYYYMMDD')
    AND order_status_order_status_id = 4;