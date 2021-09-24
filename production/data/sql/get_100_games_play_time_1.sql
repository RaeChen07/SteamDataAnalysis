-- Computes the global playtime for the randomly selected 100 games
-- that have data in `games_1` and have achievements.

USE steam;
SELECT
    A.appid AS appid,
    A.Title AS title,
    A.Is_Multiplayer AS is_multiplayer,
    SUM(G.playtime_forever) AS playtime_forever,
    AVG(AP.Percentage) AS avg_achievement_percentage
FROM app_id_info_100 A, achievement_percentages AP, games_1 G
WHERE A.appid = AP.appid AND A.appid = G.appid
GROUP BY A.appid, A.Title, A.Is_Multiplayer;