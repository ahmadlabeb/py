from cars import Bmw as bmw
import pyodbc
import json
import unicodedata
def num(x):
    global z
    def num(y):
        return x*y
    return num
print(num(5)(5))
conn=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=AHMAD_ABU_LABEB\ABULABEB;DATABASE=Mne_IntranetContext;UID=sa;PWD=root;Trusted_Connection=yes;')
def insert():
    cursor.execute("insert into unit_st(unit_desc)values('pcs')")
    com=conn.commit()
    print(com)
if conn:
    print('connect')
    cursor=conn.cursor()
    cursor.execute('select * from unit_st')
    row = cursor.fetchall()
    print(row)
    insert()
    for a in row:
        # print('id ==> {0} \n name => {1}'.format(a.id,a.unit_desc))
        # name= unicodedata.category(a.unit_desc)
        print(json.dumps({'id':a.id,'name': '{0}'.format(a.unit_desc)}))
else:
    print('error')
b=bmw()
print('ahmad')