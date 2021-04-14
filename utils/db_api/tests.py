from utils.db_api.sqlite import Database

db = Database()


def test():
    db.create_table_tarif()
    db.add_tarif('Start-0', '5', '512', '1', '215', 'start')
    db.add_tarif('Start-1', '10', '1024', '1', '248', 'start')
    db.add_tarif('Start-2', '15', '2048', '2', '590', 'start')
    db.add_tarif('Start-3', '25', '4096', '2', '990', 'start')

    print(db.select_tarif(category='start'))


test()


