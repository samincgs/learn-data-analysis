# SQL Notes

Creating example databases in SQLite to become more comfortable with the SQLite command-line terminal and SQL commands. My goal is to build a stronger foundational understanding of how to query and manipulate data to extract meaningful results.

---

## SQLite

- Use `.schema` to view the structure of tables in the current database.
- Use `.mode (table, csv, ascii, list)` to change the output of the tables to a preferred readable format.

---

## 🔍 Querying

The `SELECT` statement is used to **query data from a table**. It returns rows that match the specified criteria.

#

-> Can be used in conjunction with the `WHERE` statement to filter out the table and get back rows where that condition is true.

### Logical Operators

-> Use `AND` to combine multiple conditions that must all be true.  
-> Use `OR` to combine multiple conditions where at least one must be true.  
-> Use `NOT` to negate or invert a condition.

## NULL Values

-> NULL means that the value is not present for that row.
-> Use `IS NULL` or `IS NOT NULL` to find or search for null values.

## LIKE, BETWEEN

-> Use `LIKE` to match for words in a certain row value.
-> Use `%` can match any character around the string and `_` can match a single character in a string.

-> Can use `BETWEEN _ AND _` to find rows between a certain range.

# ORDER BY

-> Use `ORDER BY` to take the results of the query and order them by a column
-> Use `ASC` (default, means least to greatest) or `DESC` (means greatest to smallest)
