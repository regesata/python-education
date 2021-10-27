COPY potential_customers(
    id, email, name, surname, second_name,
    city)
FROM '/usr/src/p_customers.csv'
DELIMITER ',';