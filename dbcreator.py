import sqlite3
from sqlite3 import Error
import pandas as pd

def create_connection(__db__):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(__db__)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_table(__db__, __table__, __dict__):

    sql = f" CREATE TABLE {__table__}("
    for i in range(len(dict.keys())):
        if i == 0:
            sql = sql + f"\t{list(dict.keys())[i]} INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
        elif i < len(dict.keys()) - 1:
            sql = sql + f"\t{list(dict.keys())[i]} {dict[list(dict.keys())[i]]}, "
        else:
            sql = sql + f"\t{list(dict.keys())[i]} {dict[list(dict.keys())[i]]});"

    conn = sqlite3.connect(__db__)
    try:
        conn.execute(sql)
        print(f"se creo la tabla {__table__}")                        
    except sqlite3.OperationalError:
        print(f"La tabla {__table__} ya existe!")                    
    conn.close()

def selectall(__db__, __table__):
	conn=sqlite3.connect(__db__)
	sql="select * from " + __table__
	cursor=conn.execute(sql)	
	cabeceras = get_column_names(__db__, __table__)
	capturador=[]
	for fila in cursor:
		capturador.append(fila)
	conn.close()
	__dict__ = {
		cabeceras: capturador
	}
	df = pd.DataFrame(__dict__)
	print(df)
	return(capturador)
	
def selectone(__db__, __table__, __condition__):
	con=sqlite3.connect(__db__)
	sql="select * from " + __table__ + \
	" where " + __condition__
	cursor=con.execute(sql)	
	filas=cursor.fetchall()
	capturador=[]
	for fila in filas:
		capturador.append(fila)
	con.close()
	return(capturador)
	
def get_column_names(__db__, __table__):
	conn = sqlite3.connect(__db__)
	sql = "select * from " + __table__
	cursor = conn.execute(sql)
	conn.close()
	column_names = [desc[0] for desc in cursor.description]
	return(tuple(column_names))

def insert(__db__, __table__, __val__):
	cabeceras=get_column_names(__db__, __table__)
	val_cab='('
	for i in cabeceras:
		val_cab=val_cab + ',?'
	val_cab=val_cab + ')'
	val_cab=val_cab.replace('(,?,','(')
	con=sqlite3.connect(__db__)
	sql="insert into " + __table__ + \
	str(cabeceras[1:]) + ' values ' + \
	val_cab #'(?,?)' #str(val_cab)
	con.execute(sql, __val__)
	con.commit()
	con.close()




database = r"2tim4_1.db"
table = 'aguas_vivas'

dict = {}
dict['Id'] = 'PRIMARY'
dict['Fecha'] = 'TEXT'
dict['Versiculo'] = 'TEXT'
dict['Subtitulo'] = 'TEXT'
dict['Pasaje'] = 'TEXT'
dict['Comentario'] = 'TEXT'

# sql = f'create table {table}(\n'
# for i in range(len(dict.keys())):
# 	if i == 0:
# 		sql = sql + f"\t{list(dict.keys())[i]} primary key autoincrement,\n"
# 	elif i < len(dict.keys()) - 1:
# 		sql = sql + f"\t{list(dict.keys())[i]} {dict[list(dict.keys())[i]]},\n"
# 	else:
# 		sql = sql + f"\t{list(dict.keys())[i]} {dict[list(dict.keys())[i]]}\n"
# sql = sql + '\n);'

# print(sql)


# create_connection(database)
create_table(database, table, dict)
# selectall(database, table)