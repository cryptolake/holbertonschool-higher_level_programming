-- average temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDE
R BY avg_temp DESC;
