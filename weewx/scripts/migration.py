import sqlite3

conn = sqlite3.connect('/mnt/ssd/weewx/storage/weewx.sdb')
c = conn.cursor()

def tableFilter(name):
    count = c.execute("select count(*) from %s;"%(name)).fetchall()
    return count[0][0] < 100 and count[0][0] > 3

def getInsertStatement(tableName):
    if tableName.find("_") > -1:
        statement = "insert into %s select * from orig.%s where dateTime < 1610690400;"%(tableName, tableName)
    else:
        return None;
    return statement

def doTransaction(x):
    insertStatement = getInsertStatement(x[0])
    if insertStatement == None:
        return
    c.execute(insertStatement)
    conn.commit()

def main():
    tables = c.execute('''SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';''').fetchall()
    filteredTables = filter(tableFilter, tables)
    c.execute("attach '/mnt/ssd/weewx/storage/weewx.bak.sdb' as orig;")
    map(doTransaction, filteredTables)
    c.execute('detach orig;')
    conn.close()
    
main()
