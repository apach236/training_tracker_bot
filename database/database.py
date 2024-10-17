
import aiosqlite

from datetime import date


async def create_table():
    async with aiosqlite.connect('training.db') as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS training 
                         (training_id integer generated always as identity primary key, 
                         user_id integer not null, 
                         date text not null, 
                         category text not null)''')
        await db.commit()


async def save_to_db(user_id, category):
    async with aiosqlite.connect('training.db') as db:
        await db.execute('INSERT INTO requests VALUES (?, ?, ?)',
                         (user_id, str(date.today()), category))
        await db.commit()


async def check_last_trainig(user_id):
    async with aiosqlite.connect('training.db') as db:
        async with db.execute('''select date from training
                            where user_id = (?)
                            order by date desc limit 1''',
                              (user_id)) as cursor:
            last_date = cursor
    return last_date
