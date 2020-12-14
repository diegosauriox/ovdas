import time
import datetime
import numpy as np
from traces_ufro import *
from pyrocko import trace
import pyrocko.gui as gui
import pyrocko

station_list=['FRE']

stattion=pyrocko.model.station.load_stations('Estaciones_Pyrocko.pf')
network='99'





""" Define tiempo """
date1='2020-02-18 00:06:00'
date1='2020-03-25 11:57:59'
#date2='2020-02-18 00:10:00'
dt1=datetime.datetime.strptime(date1,'%Y-%m-%d %H:%M:%S')
#dt2=datetime.datetime.strptime(date2,'%Y-%m-%d %H:%M:%S')
posix_dt1 = time.mktime(dt1.timetuple())-30
posix_dt2 = posix_dt1+240 #time.mktime(dt2.timetuple())

st_final=[]
""" Carga trazas de forma remota """
st_final=read_stations(st_final,posix_dt1,posix_dt2,station_list,network)
datosx=[]
datosY=[]
#datosX=st_final[0].get_xdata()
#datosY=st_final[0].get_ydata()
print(st_final[0])






""" Carga visualizador para picar """
#[ret, mark]=trace.snuffle(st_final,want_markers=True,stations=stattion)   

#mark_file='MarkRemote_'+datetime.datetime.strftime(dt1,'E%Y%m%d%H%M%S')+datetime.datetime.strftime(datetime.datetime.now(),'G%Y%m%d%H%M%S')
#if len(mark)>0:
#    gui.marker.PhaseMarker.save_markers(mark,mark_file)
#else:
#    print("No guarda para "+mark_file)
