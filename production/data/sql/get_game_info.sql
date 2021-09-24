-- Gets all apps that are games and normalizes column names.

USE steam;
SELECT
    A.appid app_id,
    A.Title title,
    A.Price price,
    A.Release_Date release_date,
    A.Rating rating,
    A.Required_Age required_age,
    A.Is_Multiplayer is_multiplayer
FROM app_id_info A
WHERE A.Type = "Game"
ORDER BY app_id;