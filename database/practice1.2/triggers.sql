create or replace function gather_order_deleted_cars()
returns trigger
as
$$
    declare
        car int;
    begin
        select cars_car_id from rent_orders
        where rent_order_id = new.rent_orders_rent_order_id
        into car;
        update cars set is_available = true
        where car_id = car;
        return NEW;
    end;
$$ language plpgsql;

CREATE TRIGGER  car_upd
AFTER INSERT
ON return_orders
FOR EACH ROW
EXECUTE PROCEDURE  gather_order_deleted_cars();

create or replace function chek_period_of_rent()
returns trigger
as
$$  declare
    rent_date timestamp;

    begin
    select date_of_order from rent_orders
    where rent_order_id = NEW.rent_orders_rent_order_id
    into rent_date;

        if NEW.date_of_returning < rent_date then
            raise  exception 'Date of returning cant be less than date of rent';
        end if;
        return new;
    end;
$$ language plpgsql;

CREATE TRIGGER date_check
BEFORE INSERT
ON return_orders
FOR EACH ROW
EXECUTE PROCEDURE chek_period_of_rent();




