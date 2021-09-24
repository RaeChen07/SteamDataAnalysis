USE steam;
SELECT *
FROM app_id_info_100 A, games_genres G
WHERE A.appid = G.appid
ORDER BY A.appid;