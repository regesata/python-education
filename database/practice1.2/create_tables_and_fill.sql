--BEGIN;
CREATE TABLE IF NOT EXISTS cites(
    city_id serial PRIMARY KEY,
    short_name varchar(10) NOT NULL,
    full_name varchar(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS addresses(
    address_id serial PRIMARY KEY,
    cites_city_id integer NOT NULL,
    street varchar(100),
    building_num integer
);

CREATE TABLE IF NOT EXISTS customer_address(
    customer_address_id serial PRIMARY KEY,
    customers_customer_id integer,
    addresses_address_id integer
);

CREATE TABLE IF NOT EXISTS branch_url(
    branch_url_id serial PRIMARY KEY,
    branches_branch_id integer,
    url varchar(255)
);

CREATE TABLE IF NOT EXISTS branches(
    branch_id serial PRIMARY KEY,
    addresses_address_id integer,
    phone_number varchar(20)
);

CREATE TABLE IF NOT EXISTS customers(
    customer_id serial PRIMARY KEY,
    first_name varchar(50) NOT NULL,
    second_name varchar(50) NOT NULL,
    phone_number varchar(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS cars(
    car_id serial PRIMARY KEY,
    trademark varchar(50) NOT NULL,
    model_name varchar(50) NOT NULL,
    price money NOT NULL,
    licence_plate varchar(20) NOT NULL,
    branches_branch_id integer,
    is_available bool
);

CREATE TABLE IF NOT EXISTS rent_orders(
    rent_order_id serial PRIMARY KEY,
    cars_car_id integer,
    customers_customer_id integer,
    date_of_order timestamp DEFAULT timeofday()::timestamp
);

CREATE TABLE IF NOT EXISTS return_orders(
    return_order_id serial PRIMARY KEY,
    rent_orders_rent_order_id integer,
    date_of_returning timestamp DEFAULT timeofday()::timestamp,
    period integer
);

CREATE TABLE IF NOT EXISTS additional_options(
    option_id serial PRIMARY KEY,
    option_name varchar(255),
    option_description text
);

CREATE TABLE IF NOT EXISTS car_options(
    cars_options_id serial PRIMARY KEY,
    cars_car_id integer,
    additional_options_option_id integer
);

--Filling tables
--customers

do
$$
    declare
      i int;
    begin
        for i in 1..500000 loop
            insert into customers(first_name, second_name, phone_number)
            values ('First name '||i::varchar, 'Second name '||i::varchar, '+1'
                    ||ROUND((random()+1) * 1000000)::varchar);
        end loop;

    end;
$$ language plpgsql;
--cities
do
$$
    declare
      i int;
    begin
        for i in 1..200000 loop
            insert into cites(short_name, full_name)
            values ('CN'||i::varchar, 'City '||i::varchar);
            end loop;
    end;
$$ language plpgsql;

--addresses
do
$$
    declare
      i int;
    begin
        for i in 1..500000 loop
        insert into addresses(cites_city_id, street, building_num)
        values ((trunc(random()*20000) + 1)::int, 'Street '||i::varchar, trunc(random()*1000) + 1);
        end loop;
    end;
$$ language plpgsql;

--customer_address
do
$$
    declare
      i int;
    begin
        for i in 1..350000 loop
            insert into customer_address(customers_customer_id, addresses_address_id)
            values (i, trunc(random()*350000) + 1);
            end loop;
    end;
$$ language plpgsql;

--branches
do
$$
    declare
        i int;
    begin
        for i in 1..250000 loop
            insert into branches(addresses_address_id, phone_number)
            values (trunc(250000+random()*250000), '+1'
                    ||trunc((random()+1) * 1000000)::varchar );
            end loop;
    end;
$$ language plpgsql;

--branch url

do
$$
    declare
        i int;
    begin
        for i in 1..250000 loop
            insert into branch_url(branches_branch_id, url)
            values (i, substr(md5(i::text),1, 10)||'.com');
            end loop;
    end;
$$ language plpgsql;

--cars
do
$$
    declare
        i int;
        j int;
        t_marks text[];
    begin
        t_marks := ARRAY ['Chrysler', 'Dodge', 'Jeep', 'Ford', 'Lincoln'];
        for i in 1..500000 loop
            j := (i % 5) + 1;
            insert into cars(trademark, model_name, price, licence_plate, branches_branch_id, is_available)
            values (t_marks[j], substr(md5(i::varchar), 1, 4), round(random()*350 + 100)::int, substr(md5((i*35)::text),
                1, 10), round(random()*249999 + 1), true);
            end loop;
    end;
$$ language plpgsql;

--additional options
do
$$
    declare
        i int;
    begin
        for i in 1..1000000 loop
        insert into additional_options(option_name, option_description)
        values('Option name '||i::text, 'Option description '||i::text);
        end loop;
    end;
$$ language plpgsql;

--car option
do
$$
    declare
        i int;
        m int;
        n int;
    begin
        m := 1;
        n := 2;
        for i in 1..500000 loop
            insert into car_options(cars_car_id, additional_options_option_id)
            values (i, m),
                   (i, n);
            m := m + 2;
            n := n + 2;
        end loop;
    end;
$$ language plpgsql;

--rent order
do
$$    declare
        d timestamp;
        i int;
        c text;
    begin
        d := '2018-01-05 08:00:00';

        for i in 1..500000 loop
            c:= (trunc(random()*10)+1)::text ||' minutes' ;
            d:= d + c::interval;
            insert into rent_orders(cars_car_id, customers_customer_id, date_of_order)
            values (trunc(random()*500000)+1, trunc(random()*500000)+1, d );
            end loop;
    end;
$$ language plpgsql;

--return order
do
$$
    declare
        order_date timestamp;
        c int;
        offs text;
        res record;
    begin
        for res in select * from rent_orders loop
            c := (trunc(random()*10)+1)::int;
            offs := (c)::text ||' days' ;

        insert into return_orders(rent_orders_rent_order_id, date_of_returning, period)
        values (res.rent_order_id, res.date_of_order +offs::interval, c);
        end loop;
    end;
$$ language plpgsql;


ALTER TABLE branches
ADD CONSTRAINT branches_address_fk
FOREIGN KEY (addresses_address_id) REFERENCES addresses(address_id);

ALTER TABLE branch_url
ADD CONSTRAINT url_branch_fk
FOREIGN KEY (branches_branch_id) REFERENCES branches(branch_id);

ALTER TABLE addresses
ADD CONSTRAINT address_city_fk
FOREIGN KEY (cites_city_id) REFERENCES cites(city_id);

ALTER TABLE customer_address
ADD CONSTRAINT customer_address_customer_fk
FOREIGN KEY (customers_customer_id) REFERENCES customers(customer_id),
ADD CONSTRAINT customer_address_address_fk
FOREIGN KEY (customer_address_id) REFERENCES addresses(address_id);

ALTER TABLE cars
ADD CONSTRAINT cars_branches_fk
FOREIGN KEY (branches_branch_id) REFERENCES branches(branch_id);

ALTER TABLE car_options
ADD CONSTRAINT  car_options_car_fk
FOREIGN KEY (cars_car_id) REFERENCES cars(car_id),
ADD CONSTRAINT car_options_additional_option_fk
FOREIGN KEY (additional_options_option_id) REFERENCES additional_options(option_id);

ALTER TABLE rent_orders
ADD CONSTRAINT rent_order_customer_fk
FOREIGN KEY (customers_customer_id) REFERENCES customers(customer_id),
ADD CONSTRAINT rent_orders_car_fk
FOREIGN KEY (cars_car_id) REFERENCES cars(car_id);

ALTER TABLE return_orders
ADD CONSTRAINT return_orders_rent_order_fk
FOREIGN KEY (rent_orders_rent_order_id) REFERENCES rent_orders(rent_order_id);









