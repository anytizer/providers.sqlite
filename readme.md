# providers.sqlite
User defined functions for SQLite Database Connections written in Python.

## Available SQLite Functions

### GUID()

    SELECT GUID();

### NOW()

    SELECT NOW();

### SHA256(?)

    SELECT SHA256("something");

### CONCAT_WS(_JOINER, *values)

    SELECT CONCAT_WS(',', 'First Name', NULL, 'Last Name');


 * [W3Schools](https://www.w3schools.com/sql/func_mysql_concat_ws.asp)
 * [MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_concat-ws)
 * [Advanced Parameter Handling For Functions](https://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch15s09.html)
