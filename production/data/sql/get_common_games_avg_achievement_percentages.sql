-- Computes the global average achievement percentages for
-- all common games, using a left join to preserve any games
-- without achievements.

USE steam;
SELECT CG.app_id app_id, avg(AP.Percentage) average_achievement_percentage
FROM common_games CG
LEFT JOIN achievement_percentages AP
ON CG.app_id = AP.appid
GROUP BY CG.app_id;