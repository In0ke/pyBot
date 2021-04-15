from utils.db_api.sqlite import Database

db = Database()


def test():
    print(db.select_all_os())
    print(db.select_all_aps())


test()
