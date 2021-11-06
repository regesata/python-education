create or replace function get_city_branches(city_short_name varchar)
returns text as
    $$
        declare
            return_text text;
            branch_rec record;
            branch_cur cursor(city_short_name varchar)
                        for select branch_id, c.full_name , a.street,
                        a.building_num, phone_number, url
                        from branches
                        join addresses a on branches.addresses_address_id = a.address_id
                        join cites c on c.city_id = a.cites_city_id
                        join branch_url bu on branches.branch_id = bu.branches_branch_id
                        where c.short_name like city_short_name;
        begin
            open branch_cur(city_short_name);
            return_text := '';
            loop
                fetch branch_cur into branch_rec;
                exit when not found;
                return_text := return_text ||'branc number: '||branch_rec.branch_id||' street: '||branch_rec.street||' building: '
                || branch_rec.building_num||' phone: '||branch_rec.phone_number||' web-site: '||branch_rec.url||E'\n';
            end loop;
        close branch_cur;
        return return_text;
        end;
$$language  plpgsql;

create or replace function get_cars_from_branch(id int)
returns table(mark varchar, model varchar, cost money, can_rent bool)
as
$$
    begin
        return QUERY
            SELECT c.trademark, c.model_name, c.price, c.is_available FROM cars c
            WHERE branches_branch_id = id;
    end;
$$language plpgsql;
select * from get_cars_from_branch(275);
select get_city_branches('CN110')