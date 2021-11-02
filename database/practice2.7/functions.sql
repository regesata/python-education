create or replace function free_shipping(city_x varchar(255)) returns int
as $$
declare
    i int;
    j int;
    res int := 0;
begin
    create temporary table carts_city(
        t_cart_id int);
    <<out>>
    for i in
        select c.cart_id from users u
        join carts c on u.user_id = c.users_user_id
        where u.city = city_x
        order by c.cart_id
    loop
        <<inner>>
        for j in select carts_cart_id from m_order
            loop
            if i = j then
                update m_order set shipping_total = 0 where carts_cart_id = j;
                res := res + 1;
            end if;
            end loop inner;
    end loop out;
    drop table carts_city;
    return  res;
end;
$$ language plpgsql;

-- creates cart and adds product in it, reduce product in_stock, calculate total sum of cart
-- adds cart into carts table and adds pair cart_id and product_id into carts_products table

create or replace procedure add_cart_with_product(id_user int, int[])
as $$
declare
    cartid int;
    total_s decimal := 0;
    curr_sum decimal;
    prod_qnt int;
    i int;
begin
    select count(*) from carts
    into cartid;
    cartid := cartid + 1;
    insert into carts(cart_id, users_user_id, subtotal, total, timestamp)
    values (cartid, id_user, 0, 0, timeofday()::timestamp);
    commit;
    foreach i in array $2
        loop
            select in_stock from products where product_id = i
            into prod_qnt;
            if prod_qnt > 0 then
                update products set in_stock = in_stock - 1 where product_id = i;
                select price from products where product_id = i
                into curr_sum;
                total_s := total_s + curr_sum;
                insert into carts_product(carts_cart_id, products_product_id)
                values (cartid, i);
            else
                continue;
            end if;
        end loop;
    if total_s = 0 then
        rollback;
    else
        update carts  set subtotal = total_s, total = total_s
        where cart_id = cartid;
        commit;
    end if;

end;
$$language plpgsql;

--creates order using cart and calculate shipping, if total more than 300
-- or user lives in city 1 shipping is for free, in other cases shipping costs 65
create or replace procedure create_order(cart_ind int)
as $$
    declare
        user_city varchar;
        cart_total decimal;
        order_num int;
        shipping decimal;
    begin
        select u.city from carts c
        join users u on u.user_id = c.users_user_id
        where c.cart_id = cart_ind
        into user_city;

        select count(*) from m_order
        into order_num;
        order_num := order_num +1;

        select total from carts where cart_id = cart_ind
        into cart_total;
        if cart_total = 0 then
            rollback;
        end if;
        if user_city = 'city 1' or cart_total > 300 then
            shipping := 0;
        else
            shipping = 65;
        end if;
         insert into m_order(order_id, carts_cart_id, order_status_order_status_id,
                                shipping_total, total, created_at, updated_at)
            values (order_num, cart_ind, 1, shipping, cart_total, timeofday()::timestamp,
                    timeofday()::timestamp);
    end;
$$language plpgsql;

-- BEGIN;
-- call add_cart_with_product(100, array[100, 250, 300]);
-- call create_order(2001);
-- ROLLBACK;