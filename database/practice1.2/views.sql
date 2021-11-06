CREATE OR REPLACE VIEW branchs_url AS
    SELECT b.branch_id,  b.phone_number,  bu.url  FROM branches b
    JOIN branch_url bu on b.branch_id = bu.branches_branch_id;
SELECT * FROM branchs_url;

CREATE OR REPLACE VIEW  order_cost AS
    SELECT return_order_id, (period * c.price)total, date_of_returning FROM return_orders
    JOIN rent_orders ro on ro.rent_order_id = return_orders.rent_orders_rent_order_id
    JOIN cars c on c.car_id = ro.cars_car_id
    ORDER BY return_order_id;
SELECT * FROM order_cost;


CREATE MATERIALIZED VIEW car_customers AS
    SELECT trademark, model_name, c.first_name, c.second_name, c.phone_number, c2.full_name,
           a.street, a.building_num FROM cars
    JOIN rent_orders ro on cars.car_id = ro.cars_car_id
    JOIN customers c on c.customer_id = ro.customers_customer_id
    JOIN customer_address ca on c.customer_id = ca.customers_customer_id
    JOIN addresses a on a.address_id = ca.customer_address_id
    JOIN cites c2 on c2.city_id = a.cites_city_id
WITH NO DATA ;

REFRESH MATERIALIZED VIEW car_customers;
SELECT * FROM car_customers;

DROP VIEW branchs_url;
DROP VIEW order_cost;
DROP MATERIALIZED VIEW car_customers;