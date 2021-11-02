--Index reduces time from 6.0 to 5.5
--Deletion of carts without orders
BEGIN;
CREATE INDEX IF NOT EXISTS cart_ind ON carts_product using hash(carts_cart_id);
EXPlAIN (ANALYSE) DELETE FROM carts_product
    WHERE carts_cart_id in (SELECT cart_id FROM carts
        LEFT JOIN m_order mo on carts.cart_id = mo.carts_cart_id
        WHERE mo.carts_cart_id is NULL);
ROLLBACK;