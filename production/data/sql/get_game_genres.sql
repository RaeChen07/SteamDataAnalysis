-- Exports the game genres table and normalizes column names.

USE steam;
SELECT G.appid app_id, G.Genre genre
FROM games_genres G
ORDER BY app_id;