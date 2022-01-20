# python connects to the postgreSQL using Psycopg2 module
import psycopg2

connection = psycopg2.connect(
    host='localhost',
    database='db_demos',
    user='postgres',
    password='1123QwER'
)
cursor = connection.cursor()
cursor.execute('''
SELECT CONCAT(e.name,' (',e.job_title,')') as employee,
CONCAT(m.name, ' (', m.job_title, ' )') as manager
FROM employees e
RIGHT JOIN employees m
    ON e.manager_id = m.id
''')


# for row in cursor.fetchall():
#     print(row)

# we usually use ORM to get the data
# Object-relational mapping
class Employee:
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager

    def __repr__(self):
        return f'{self.name}, {self.manager}'


employees = [Employee(*row) for row in cursor.fetchall()]
print(employees)
connection.close()
# Django has a built-in orm with psycopg as dependency Employee.objects.all()
