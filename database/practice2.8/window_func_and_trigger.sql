--Finds difference between average price of category and each product in this category
SELECT c.category_title, product_title, price,
    price - AVG(price)  OVER (PARTITION BY category_title) AS diff,
    AVG(price) OVER (PARTITION BY category_title) AS avg
FROM products p
JOIN categories c on c.category_id = p.category_id
ORDER BY c.category_id;


--Function for trigger that checks in_stock cant be negative
create or replace function check_in_stock()
returns trigger

as
$$
    begin
        if NEW.in_stock < 0 then
            raise exception 'Cant sold more then in stock';
        end if;
        return NEW;
    end;
$$ language plpgsql;


create or replace function collect_stat()
returns trigger
as
$$
    begin
        if NEW.in_stock < 4  then
            insert into running_out_goods(product_title, quantity)
            values (NEW.product_title, NEW.in_stock);
        end if;
        return NEW;
    end;
$$ language plpgsql;



BEGIN;
CREATE TABLE IF NOT EXISTS running_out_goods(
    id serial PRIMARY KEY ,
    product_title varchar(255),
    quantity integer,
    create_at timestamp DEFAULT timeofday()::timestamp
);

create trigger product_in_stock_check
    before update
    on products
    for each row
    execute procedure check_in_stock();

create trigger stat_grabber
    after update
    on products
    for each row
    execute procedure collect_stat();
--in_stock equals 11 for id = 2
UPDATE products SET in_stock = 1
WHERE product_id = 13;

SELECT * FROM running_out_goods;

UPDATE products SET in_stock = in_stock - 20
WHERE product_id = 2;

ROLLBACK;
