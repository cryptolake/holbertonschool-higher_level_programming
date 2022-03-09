-- Cities of california
SELECT cities.id as id, cities.name as name
FROM cities, states
WHERE cities.state_id = states.id AND states.name = "California"; 
