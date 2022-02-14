#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 12:15:26 2020

@author: ifustos
"""
import time
import datetime
import numpy as np
import configparser
# Import module
import jpype as jp

# Enable Java imports
import jpype.imports

# Pull in types
from jpype.types import *
from pyrocko import trace
# Launch the JVM
import os

rutaJAR=os.getcwd()+"/waves/usgs.jar"
rutaGAIN=os.getcwd()+"/waves/Gain_esta.conf"

def read_stations(str_final,st_tiempo,posix_dt1,posix_dt2,station_list,network,comp=['Z','E','N'],server_ip='146.83.206.104',port=29384):
    
    for station in station_list:
        #try:
        str_final,st_tiempo=read_traces(str_final,st_tiempo,posix_dt1,posix_dt2,station,network)
        
   
            
#        except:
#            print("Error en estacion "+station)server_ip
        
    
    return str_final,st_tiempo
def read_traces(str_final, st_tiempo,posix_dt1,posix_dt2,station,network,comp=['Z','E','N'],server_ip='146.83.206.104',port=29384):
    try:
        jp.startJVM(classpath=[rutaJAR])
    except:
        print("JVM running")
    from gov.usgs.winston.server import WWSClient
    wws=WWSClient(server_ip,port);#datos local"localhost",16022
    print("Bajando "+station)
    

    #try:
    junk=wws.getRawData(station+"Z",'HH'+"Z",'TC',network,posix_dt1,posix_dt2)
    time.sleep(0.2)
    value_gain=read_values(station,"Z")
    """ Acomoda la traza"""
    if junk is not None:
        y=java_int2float(junk.buffer,value_gain)
        st=create_trace(station,network,"Z",junk,y)
        st_tiempo=np.linspace(junk.getStartTime(),junk.getEndTime(),len(y))
        str_final.append(st)
    #except:
    #    print('Comp='+i+' in '+station +' not found!')

    return str_final,st_tiempo

def java_int2float(yy,value_gain):
    """ Transforma valores de string de java a flotante"""
    y=np.zeros(len(yy))
    ind=0
    for i in yy:
        if i<-2147483647:
            y[ind]=0.0
        else:
            try:
                y[ind]=float(i)*value_gain
            except:
                print(i,len(yy))
                print(value_gain)
                import sys;sys.exit()
        ind=ind+1
    
    return y
def create_trace(station,network,compo_uniq,junk,y):
    """ Genera tarza desde llamado remoto
    
    Programado por Ivo fustos, 2020"""
    st = trace.Trace(
    station=station,network=network,location=network, channel=compo_uniq, deltat=1/junk.getSamplingRate(), tmin=junk.getStartTime(), ydata=y)
    
    return st

def read_values(esta,comp,file_gain=rutaGAIN):
    """ Programa que lee estaciones y sus ganancias
    Programado por Ivo fustos, 2020
    """
    config = configparser.ConfigParser()
    config.read(file_gain)
    value_gain=float(config[esta][comp])
    
    config=[]
    return value_gain


    
