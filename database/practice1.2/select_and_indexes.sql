--Index reduces cost from 20000 to 9500
BEGIN;
EXPLAIN ANALYZE SELECT c.trademark, c.model_name, c.price, ao.option_name  FROM cars c
JOIN car_options co on c.car_id = co.cars_car_id
JOIN additional_options ao on ao.option_id = co.additional_options_option_id
JOIN branches b on b.branch_id = c.branches_branch_id
WHERE price < 700::money AND b.branch_id = 10000
ORDER BY c.price;
CREATE INDEX ON car_options(cars_car_id);
ROLLBACK;

--Index reduces cost from 14500 to 7000
BEGIN;
EXPLAIN ANALYZE SELECT r.return_order_id, c.first_name, c.second_name, (c2.price * r.period) AS cost,
                       r. period, c2.price, date_of_returning FROM return_orders r
JOIN rent_orders ro on ro.rent_order_id = r.rent_orders_rent_order_id
JOIN customers c on c.customer_id = ro.customers_customer_id
JOIN cars c2 on c2.car_id = ro.cars_car_id
WHERE c.first_name LIKE 'First name 1541';
CREATE INDEX  ON customers(first_name, second_name);
ROLLBACK ;

--Reduce cost from 7500 to 4500
BEGIN;
EXPLAIN ANALYZE SELECT branch_id, phone_number, a.street,  c2.trademark, c2.model_name, c2.price FROM branches
JOIN addresses a on a.address_id = branches.addresses_address_id
JOIN cites c on c.city_id = a.cites_city_id
JOIN cars c2 on branches.branch_id = c2.branches_branch_id
WHERE c.short_name like 'CN1234' AND a.street LIKE 'Street 296388';
CREATE INDEX ON cites(short_name, full_name);
CREATE INDEX ON addresses(street);
ROLLBACK;










