import time
import datetime
import numpy as np

# Import module
import jpype

# Enable Java imports
import jpype.imports

# Pull in types
from jpype.types import *

# Launch the JVM
jpype.startJVM(classpath=['usgs.jar'])
#jpype.startJVM()
#jpype.addClassPath('usgs.jar')

date1='2020-02-08 00:06:00'
date2='2020-02-08 00:10:00'
dt1=datetime.datetime.strptime(date1,'%Y-%m-%d %H:%M:%S')
dt2=datetime.datetime.strptime(date2,'%Y-%m-%d %H:%M:%S')
posix_dt1 = time.mktime(dt1.timetuple())
posix_dt2 = time.mktime(dt2.timetuple())
posix_dt1
posix_dt2




from gov.usgs.winston.server import WWSClient

wws=WWSClient('localhost', 16022)
#wws=WWSClient('190.160.164.51',81);
wws.getRawData('FREZ','HHZ','TC','99',posix_dt1,posix_dt2)

