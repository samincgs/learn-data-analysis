# SQL Notes

Creating example databases in SQLite to become more comfortable with the SQLite command-line terminal and SQL commands. My goal is to build a stronger foundational understanding of how to query and manipulate data to extract meaningful results.

---

## SQLite CLI

-> Use `.schema` to view the structure of tables in the current database.
-> Use `.mode (table, csv, ascii, list)` to change the output of the tables to a preferred readable format.  
-> Use `.tables` to quickly get a glimpse of all the availables tables in the database.

---

## 🔍 Querying

The `SELECT` statement is used to **query data from a table**. It returns rows that match the specified criteria.

-> Can be used in conjunction with the `WHERE` statement to filter out the table and get back rows where that condition is true.  
-> Use the `AS` keyword to change the alias of a column or computation to a different name

### Logical Operators

-> Use `AND` to combine multiple conditions that must all be true.  
-> Use `OR` to combine multiple conditions where at least one must be true.  
-> Use `NOT` to negate or invert a condition.

### NULL Values

-> NULL means that the value is not present for that row.  
-> Use `IS NULL` or `IS NOT NULL` to find or search for null values.

### LIKE, BETWEEN, IN

-> Use `LIKE` to match for words in a certain row value.  
-> Use `%` can match any character around the string and `_` can match a single character in a string.
-> Use `IN` can obtain multiple values from a SELECT statement.

-> Can use `BETWEEN _ AND _` to find rows between a certain range.

### ORDER BY

-> Use `ORDER BY` to take the results of the query and order them by a column.  
-> Use `ASC` (default, means least to greatest) or `DESC` (means greatest to smallest).

### Aggregate Functions

Aggregate functions allow us to take a whole set of rows and return computations about the values of the row.

-> `COUNT` gives us the number of rows that are available in the table (does not count NULL values).  
-> `AVG` allows us to find the average of a certain row.  
-> `MIN` we can find the minimum value of a row.  
-> `MAX` we can find the maximum value of a row.  
-> `SUM` calculate the sum of values in a row.

### DISTINCT

-> We can use the `DISTINCT` keyword to find unique records in a column.

### SUBQUERIES (Nested Query)

-> A subquery is a query inside another query. It helps us use the result of one query as input for another.

-> Subqueries are written in parentheses () and can be placed in:

-SELECT
-FROM
-WHERE clauses
