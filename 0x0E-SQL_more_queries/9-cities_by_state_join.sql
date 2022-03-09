-- Cities by state
SELECT cities.id AS id, cities.name AS name, states.name AS name
FROM 
	cities LEFT JOIN states ON cities.state_id = states.id;

