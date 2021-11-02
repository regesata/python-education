--Index reduces Execution time from 0.5 ms to 0.05 ms
--Can be useful because user can changes his last name, but not too often

BEGIN;
SET work_mem TO '4MB';
CREATE INDEX ON users(first_name, last_name);
EXPlAIN (ANALYSE) UPDATE users SET
 last_name = 'New_name'
WHERE users.first_name = 'first_name 1800' AND users.last_name = 'last name 1800';

ROLLBACK;