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


#! /usr/bin/python
import sys, localconfig, platform, time
start_time = time.time()
#OS Runtime comments
if platform.system() == "Windows":
        sys.path.append(localconfig.winpath)
        print "You are running DeltaQuadBot UAA Module for Windows."
else:
        sys.path.append(localconfig.linuxpath)
        print "You are running DeltaQuadBot UAA Module for Linux."
import globalfunc as globe
override = False
if not globe.startAllowed(override):
        print "Fatal - System Access Denied."
        sys.exit(1)
        print "System Alert - Program Still running."
globe.checkWait()
print("--- Time elapsed: %s seconds ---" % (time.time() - start_time))