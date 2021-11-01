CREATE TABLE users(
    user_id INT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    middle_name VARCHAR(255),
    is_staff SMALLINT NOT NULL,
    country VARCHAR(255),
    city VARCHAR(255),
    address TEXT
);

CREATE TABLE carts(
    cart_id INT PRIMARY KEY,
    users_user_id INT NOT NULL,
    subtotal money,
    total money,
    timestamp TIMESTAMP(2),
    FOREIGN KEY (users_user_id)
        REFERENCES users (user_id)
);
CREATE TABLE categories(
    category_id INT PRIMARY KEY,
    category_title VARCHAR(255) NOT NULL,
    category_description TEXT
);

CREATE TABLE products(
    product_id INT PRIMARY KEY,
    product_title VARCHAR(255) NOT NULL,
    product_description TEXT,
    in_stock INT,
    price DECIMAL NOT NULL,
    slug VARCHAR(45),
    category_id INT,
    FOREIGN KEY (category_id)
        REFERENCES categories (category_id)
);

CREATE TABLE carts_product(
    carts_cart_id INT,
    products_product_id INT,
    FOREIGN KEY (carts_cart_id)
        REFERENCES carts (cart_id),
    FOREIGN KEY (products_product_id)
        REFERENCES products (product_id)
);

CREATE TABLE order_status(
    order_status_id INT PRIMARY KEY,
    status_name VARCHAR(255) NOT NULL
);

CREATE TABLE m_order(
    order_id INT PRIMARY KEY,
    carts_cart_id INT,
    order_status_order_status_id INT,
    shipping_total DECIMAL,
    total DECIMAL NOT NULL,
    created_at TIMESTAMP(2),
    updated_at TIMESTAMP(2),
    FOREIGN KEY (carts_cart_id)
        REFERENCES carts (cart_id),
    FOREIGN KEY (order_status_order_status_id)
        REFERENCES order_status (order_status_id)

);

ALTER TABLE users ADD
    phone_number INT;

ALTER TABLE users
    ALTER COLUMN phone_number TYPE  VARCHAR(100);

UPDATE products
    SET price = price * 2;

