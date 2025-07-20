###  Decorators
Decorators are functions that **wrap other functions** to extend their behavior without modifying their code directly.

- Implemented with nested functions and `functools.wraps`
- Useful for cross-cutting concerns like logging, transactions, retries, and caching


##  Decorator Tasks

###  Task 1 – Log Queries
`@log_queries` logs the SQL query with a timestamp before execution.

###  Task 2 – Handle Connections
`@with_db_connection` opens and closes a connection automatically for DB functions.

###  Task 3 – Manage Transactions
`@transactional` ensures queries are run inside a transaction block. Commits if successful; rolls back on error.

###  Task 4 – Retry on Failure
`@retry_on_failure(retries=3, delay=2)` retries the DB operation if a transient error occurs.

###  Task 5 – Query Caching
`@cache_query` caches results of SQL queries using the query string as the key to avoid redundant DB access.

---