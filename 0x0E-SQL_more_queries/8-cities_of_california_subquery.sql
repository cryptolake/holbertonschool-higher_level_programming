-- Display Cities of california
SELECT cities.id AS id, cities.name AS name
FROM cities, states
WHERE cities.state_id = states.id AND states.name = "California"; 
