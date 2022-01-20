# sql conventions  all keywords are with capital letters and
# everything else with small letters
# single quotes are used for string laterals
# double quotes are used for escaping reserved words e.g. column named "select"
# inserting data:
# making table from existing source
# CREATE TABLE customer_contacts
# AS
# SELECT customer_id,first_name,email,phone
# FROM customers;
# Adds new data to table
# INSERT INTO projects(name,start_date)
# SELECT CONCAT(name,' ',' Restructuring'), NOW()
# FROM departments;
# leaving out the where clause will result in all the data being updated!
# UPDATE employees
#   SET last_name = 'Brown'
# WHERE employee_id = 1;
# DELETE deletes individual rows while TRUNCATE works faster when clearing whole table
# when a department is deleted all related employee records will be removed
# CREATE TABLE department(
# dep_id SERIAL PRIMARY KEY,
# name VARCHAR(20),
# ALTER TABLE employee
# ADD dep_fk REFERENCES department ON DELETE CASCADE
# joining 2 different tables via foreign/primary key
# SELECT *
# FROM cities
# JOIN countries
# ON cities.country_id = countries.id
# LEFT AND RIGHT joins also attach rows which dont meet the condition for the left or right table respectively
# there are 8 types of join
# COCAT(a,' ',b) CONCAT_WS('',...) like join in python
# DISTINCT gives only unique values
# select distinct country_id
# from cities
# ORDER BY country_id ASC;
# NOT,AND,OR,BETWEEN,IN(),NOT IN()
# NULL = NULL returns null
# NULL IS NULL returns true
# joins can be executed in views which are function for generating a dynamic table
