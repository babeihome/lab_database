__author__ = 'beibeihome'
import MySQLdb


def InsertData(conn, TableName, dic):
    try:
        cur = conn.cursor()
        COLstr = ''
        ROWstr = ''

        for key in dic.keys():
            value_copy = '"' + dic[key] + '"'
            COLstr = ','.join([COLstr, key])
            ROWstr = ','.join([ROWstr, value_copy])
        COLstr = COLstr.lstrip(',')
        ROWstr = ROWstr.lstrip(',')
        order = 'INSERT INTO %s(%s) VALUES (%s)' % (TableName, COLstr, ROWstr)
        cur.execute(order)
        conn.commit()
        cur.close()
    except MySQLdb.Error, e:
        print order
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
