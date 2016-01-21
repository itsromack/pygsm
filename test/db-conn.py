#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

host = 'localhost'
username = 'root'
passwd = 'secret'
dbname = 'mysql'

try:
	con = mdb.connect(host, username, passwd, dbname)

	cur = con.cursor()
	sql = "SELECT VERSION()"
	cur.execute(sql)
	ver = cur.fetchone()
	print "DB Version: %s " % ver

except mdb.Error, e:
	print "Error %d %s" % (e.args[0], e.args[1])
	sys.exit(1)

finally:
	if con:
		con.close()
