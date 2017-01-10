SELECT DISTINCT mobile 
FROM data
WHERE age>18 
GROUP_BY company HAVING sum(salary) >100000
ORDER BY skill
 
