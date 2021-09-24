USE steam;
SELECT * FROM app_id_info_100 A, achievement_percentages AP
WHERE A.appid = AP.appid
ORDER BY A.appid;