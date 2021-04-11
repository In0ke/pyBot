from utils.db_api.sqlite import Database

db = Database()


def test():
    db.create_table_users()
    users = db.select_all_user()
    print(f'До добавления пользователей: {users=}')
    db.add_user(1, '1', 'email_1')
    db.add_user(2, '2', 'email_2')
    db.add_user(3, '3', 'email_3')
    db.add_user(4, '4', 'email_4')
    db.add_user(5, '5', 'email_5')
    users = db.select_all_user()
    print(f'После добавления пользователей: {users=}')
    user = db.select_user(Name="3", id=3)
    print(f'Получил пользователя {user}')


test()


