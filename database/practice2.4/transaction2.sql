--new transaction for users table
BEGIN;

INSERT INTO users(user_id, email, password, first_name, last_name, middle_name,
                  is_staff, country, city, address, phone_number)
VALUES (3001, 'user3001@gmali.com', 123456789,'John', 'Smith', 'JS', 0, 'countryZZ',
        'city 901', 'address 123444', '13-46-789-7');

UPDATE users SET is_staff = 1 WHERE user_id = 3001;

INSERT INTO users(user_id, email, password, first_name, last_name, middle_name,
                  is_staff, country, city, address, phone_number)
VALUES (3003, 'user3003@gmali.com', 123451100,'John1', 'Smith1', 'JS11', 0, 'countryAA',
        'city 911', 'address 1544', '7-87-77-22');

DELETE FROM users WHERE user_id = 3003;

COMMIT ;