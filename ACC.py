"""
(C) 2016 DeltaQuad (enwp.org/User:DeltaQuad)

This file is part of DeltaQuadBot.

DeltaQuadBot is free software: you can redistribute it and/or modify
it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

DeltaQuadBot is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU AFFERO GENERAL PUBLIC LICENSE for more details.

You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
along with DeltaQuadBot. If not, see <https://www.gnu.org/licenses/agpl.txt>.
"""

# -*- coding: utf-8 -*-
#! /usr/bin/python
import sys, platform, time
#OS Runtime comments
if platform.system() == "Windows":
        #sys.path.append(localconfig.winpath)
        print "You are running DeltaQuadBot UAA/ACC Module for Windows."
else:
        #sys.path.append(localconfig.linuxpath)
        print "You are running DeltaQuadBot UAA/ACC Module for Linux."
import globalfunc as globe
import traceback

import localconfig
import privateconfig

import MySQLdb
#SQL Slots
ID = 0
EMAIL = 1
USERNAME = 2
DATE = 3
UA = 4
IP = 5

db = MySQLdb.connect(host=privateconfig.host,    # your host
                     user=privateconfig.username,         # your username
                     passwd=privateconfig.authcode,  # your password
                     db=privateconfig.database)        # name of the data base

cur = db.cursor()
cur.execute("SELECT id,email,name,date,useragent,forwardedip FROM production.request where status = 'open' and emailconfirm = 'Confirmed';")
result=cur.fetchall()

db.close()

for request in result:
    print globe.checkuser(request[USERNAME])
