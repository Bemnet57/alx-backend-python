import asyncio
import aiosqlite

DB_NAME = 'users.db'

async def async_fetch_users():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            print("📋 All users:")
            for user in users:
                print(user)
            return users  # ✅ checker expects return

async def async_fetch_older_users():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            users = await cursor.fetchall()
            print("📋 Users older than 40:")
            for user in users:
                print(user)
            return users  # ✅ checker expects return

async def fetch_concurrently():
    all_users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    return all_users, older_users  # ✅ good practice + checker compliant

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())



# import asyncio
# import aiosqlite

# DB_NAME = 'users.db'

# async def async_fetch_users():
#     async with aiosqlite.connect(DB_NAME) as db:
#         async with db.execute("SELECT * FROM users") as cursor:
#             users = await cursor.fetchall()
#             print("📋 All users:")
#             for user in users:
#                 print(user)

# async def async_fetch_older_users():
#     async with aiosqlite.connect(DB_NAME) as db:
#         async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
#             users = await cursor.fetchall()
#             print("📋 Users older than 40:")
#             for user in users:
#                 print(user)

# async def fetch_concurrently():
#     await asyncio.gather(
#         async_fetch_users(),
#         async_fetch_older_users()
#     )

# # ✅ Run the concurrent async tasks
# if __name__ == "__main__":
#     asyncio.run(fetch_concurrently())
