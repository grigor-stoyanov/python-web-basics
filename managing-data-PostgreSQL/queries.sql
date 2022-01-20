SELECT CONCAT(e.name,' (',e.job_title,' )') as employee,
CONCAT(m.name,' (',m.job_title,' )') as manager
FROM employees e
    RIGHT JOIN employees m
        ON e.manager_id = m.id