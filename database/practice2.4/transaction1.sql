
BEGIN;
do
$$
    declare
        pro_id int;
    begin
        for pro_id in select product_id
                      from products
                      where in_stock < 10
            loop
                raise notice '%', pro_id;
                UPDATE products
                SET in_stock = (in_stock + 10)
                WHERE product_id = pro_id;
            end loop;
    end;
$$ language plpgsql;

do
$$
    declare
        j int := 123456;
        i int;
    begin
        for i in 1..25
            loop
                insert into products(product_id, product_title, product_description,
                                     in_stock, price, slug, category_id)
                values (j, 'Product_' || j, 'Product' || j, i + 10, i + 5, 'Prod_' || j, 10);
                j := j + 1;
            end loop;
    end ;
$$ language plpgsql;

do
$$
    declare
        id record;
    begin
        select product_id
        from products
        where product_id = 1234567
        into id;
        if FOUND then
            DELETE
            FROM products
            WHERE product_id = id.product_id;
        else
            raise notice 'Not found';
        end if;
    end
$$ language plpgsql;
COMMIT;










