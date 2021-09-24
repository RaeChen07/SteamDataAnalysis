-- Randomly selects 100 games from all apps.
-- Filter out non-game apps, order by random, and pick first 100.

USE steam;
CREATE TABLE app_id_info_100
SELECT *
FROM app_id_info A
WHERE A.type = "game"
ORDER BY rand()
LIMIT 100;