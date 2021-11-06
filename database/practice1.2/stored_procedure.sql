create or replace procedure create_rent_order(b_id int, u_id int, c_id int)
as $$
    declare
        is_avlb boolean;
    begin
        select is_available from cars
        where car_id = c_id
        into is_avlb;
        if not is_avlb then
            raise notice 'This car rented to another customer';
            rollback;
        else
            update cars set is_available = false
            where car_id = c_id;
            insert into rent_orders(cars_car_id, customers_customer_id)
            values (c_id, u_id);
            commit;
        end if;
    end;
$$ language plpgsql;


create or replace procedure delete_car(c_id int)
as $$
    declare
        is_avb bool;
        ord_id int;
    begin
        select is_available from cars
        where car_id = c_id
        into is_avb;
        select rent_orders_rent_order_id from return_orders
        join rent_orders ro on ro.rent_order_id = return_orders.rent_orders_rent_order_id
        where ro.cars_car_id = c_id
        into ord_id;
        if is_avb then
            delete from car_options where cars_car_id = c_id;
            delete from return_orders where rent_orders_rent_order_id = ord_id;
            delete from rent_orders where cars_car_id = c_id;
            delete from cars where car_id = c_id;
            commit;
        else
            raise notice 'Cant delete rented car.';
            rollback ;
        end if;
    end;
$$language plpgsql;

call delete_car(1);
call create_rent_order(68508, 10, 36);

