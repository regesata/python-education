CREATE TABLE potential_customers
(
    id          INT PRIMARY KEY,
    email       VARCHAR(255) NOT NULL,
    name        VARCHAR(100),
    surname     VARCHAR(100),
    second_name VARCHAR(100),
    city        VARCHAR(100)
);
--Task 1
SELECT u.first_name, u.email
FROM users u
WHERE city LIKE 'city 17'
UNION ALL
SELECT p.name, p.email
FROM potential_customers p
WHERE city LIKE 'city 17';
--Task 2
SELECT first_name, email
FROM users
ORDER BY city, first_name;
--Task 3
SELECT category_title AS category, count(product_id) AS "product count"
FROM categories
         JOIN products p on categories.category_id = p.category_id
GROUP BY category_title
ORDER BY count(product_id) DESC;
--Task 4
--4.1
SELECT p.product_title
FROM products p
         LEFT JOIN carts_product cp on p.product_id = cp.products_product_id
WHERE products_product_id is NULL
ORDER BY product_id;

SELECT product_title
FROM products p
WHERE p.product_id NOT IN (SELECT products_product_id FROM carts_product)
ORDER BY product_id;
--4.2

SELECT p.product_title
FROM products p
WHERE p.product_id IN (
    SELECT cp.products_product_id
    FROM carts_product cp
    WHERE cp.carts_cart_id IN (SELECT m.carts_cart_id
                               FROM m_order m
                               WHERE m.order_status_order_status_id = 5)
)
    AND p.product_id NOT IN (
        SELECT cp.products_product_id
        FROM carts_product cp
        WHERE cp.carts_cart_id IN (SELECT m.carts_cart_id
                                   FROM m_order m
                                   WHERE m.order_status_order_status_id < 5)
    )
   OR p.product_id IN (
    SELECT p.product_id
    FROM products p
             LEFT JOIN carts_product cp on p.product_id = cp.products_product_id
    WHERE products_product_id is NULL
)
ORDER BY p.product_id;

--4.3

SELECT p.product_title, COUNT(products_product_id) AS count
FROM carts_product
         LEFT JOIN products p on p.product_id = carts_product.products_product_id
GROUP BY p.product_title
ORDER BY count DESC
LIMIT 10;

SELECT p.product_title, COUNT(products_product_id) AS count
FROM (SELECT c.products_product_id
      FROM carts_product c
      WHERE c.carts_cart_id IN
            (SELECT m.carts_cart_id
             FROM m_order m
             WHERE m.order_status_order_status_id in (1, 2, 3, 4)
            )
     )sc
LEFT JOIN products p on p.product_id = sc.products_product_id
GROUP BY p.product_title
ORDER BY count DESC
LIMIT 10;

--4.5
SELECT u.first_name, u.last_name, m.total FROM m_order m
LEFT JOIN carts c on c.cart_id = m.carts_cart_id
LEFT JOIN users u on u.user_id = c.users_user_id
WHERE m.order_status_order_status_id in (3, 4)
ORDER BY m.total DESC;

-- I can`t test this query cos each cart is created by only one user
SELECT u.first_name, u.last_name, COUNT(c.users_user_id) FROM m_order m
LEFT JOIN carts c on c.cart_id = m.carts_cart_id
LEFT JOIN users u on u.user_id = c.users_user_id
WHERE m.order_status_order_status_id BETWEEN 1 AND 4
GROUP BY c.users_user_id, u.first_name, u.last_name
ORDER BY COUNT(c.users_user_id) DESC
LIMIT 5;

--This query has the same problem
SELECT u.first_name, u.last_name, COUNT(c.users_user_id) FROM carts c
LEFT JOIN users u on u.user_id = c.users_user_id
LEFT JOIN m_order mo on c.cart_id = mo.carts_cart_id
WHERE mo.carts_cart_id IS NULL
GROUP BY c.users_user_id, u.first_name, u.last_name
ORDER BY COUNT(c.users_user_id) DESC
LIMIT 5;












