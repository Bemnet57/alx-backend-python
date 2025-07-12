#  Python Advanced Generators & Decorators Project

This repository contains solutions for a milestone project focused on the **advanced usage of Python generators and decorators**, using a SQLite database.

##  Project Overview

The project is divided into two main parts:

- **Generators**: Used to stream, batch, and lazily process data from a SQL database with minimal memory usage.
- **Decorators**: Custom Python decorators that manage database connections, logging, transactions, retries, and caching.

---

##  Python Concepts Summary

###  Generators
Generators allow **lazy iteration** by yielding one item at a time. They're memory-efficient and ideal for processing large datasets.

- Defined using the `yield` keyword
- Resume state between iterations
- Perfect for streaming DB records or paginated data

###  Decorators
Decorators are functions that **wrap other functions** to extend their behavior without modifying their code directly.

- Implemented with nested functions and `functools.wraps`
- Useful for cross-cutting concerns like logging, transactions, retries, and caching

---

##  Generator Tasks

###  Task 1 – Stream Users One by One
Created a generator `stream_users()` that connects to a MySQL DB and yields rows from the `user_data` table one by one.

###  Task 2 – Batch Streaming
`stream_users_in_batches(batch_size)` yields users in groups.  
`batch_processing(batch_size)` filters users over age 25.

###  Task 3 – Lazy Pagination
`lazy_paginate(page_size)` uses `yield` to simulate page-by-page loading using an offset.

###  Task 4 – Average Age Generator
`stream_user_ages()` yields user ages. A separate function uses it to compute the **average age** efficiently (no SQL AVG used).

---

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

##  Requirements

- Python 3.8+
- `sqlite3` installed (usually bundled with Python)
- `users.db` database with a `users` table
- Local test data seeded using `create_db.py`

---


---

##  Author

Created by **Bemnet57** for the ALX Backend Program.

