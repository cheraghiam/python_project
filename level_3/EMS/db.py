from tinydb import TinyDB, Query


db = TinyDB('db.json')

user_table = db.table('users')
profile_user_table = db.table('profile_users')
template_table = db.table('templates')
schedule_table = db.table('schedules')

User = Query()