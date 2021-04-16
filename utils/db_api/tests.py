from utils.db_api.sqlite import Database

db = Database()


def test():
    os_list = db.select_all_os()
    print(os_list[0][0])


test()
