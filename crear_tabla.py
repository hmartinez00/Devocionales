from ManageDB.sqlite_on_db import *

database = r"2tim4_1.db"
table = 'aguas_vivas_pasajes'

dict = {}
dict['Id'] = 'PRIMARY'
dict['Fecha'] = 'TEXT'
dict['Versiculo'] = 'TEXT'
dict['Subtitulo'] = 'TEXT'
dict['Texto'] = 'TEXT'

# create_connection(database)
drop_table(database, table)
create_table(database, table, dict)
# print(get_column_names(database, table))
# insert(database, table, val)
print(selectall(database, table))