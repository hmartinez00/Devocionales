from ManageDB.sqlite_on_db import *

database = r"2tim4_1.db"
table = 'aguas_vivas_comentarios'

dict = {}
dict['Id'] = 'PRIMARY'
dict['Fecha'] = 'TEXT'
dict['Versiculo'] = 'TEXT'
dict['Subtitulo'] = 'TEXT'
# dict['Pasaje'] = 'TEXT'
dict['Texto'] = 'TEXT'

# val = ('1','1','3','1','1',)

# create_connection(database)
drop_table(database, table)
create_table(database, table, dict)
# print(get_column_names(database, table))
# insert(database, table, val)
print(selectall(database, table))