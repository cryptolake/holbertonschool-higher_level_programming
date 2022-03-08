-- Number by score
SELECT score, count(score) 'number' 
FROM 
	second_table
GROUP BY score;
