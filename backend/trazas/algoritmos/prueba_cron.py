import configparser,string,sys,os
from django.utils import timezone
import datetime
from algoritmoDetec.models import AlgortimoDeteccionModel
from .views import executeAlgoEtiqueta

def holi():

    AlgortimoDeteccionModel.objects.create(nombre='test',descripcion='prueba de crontab')
    print('holi test '+ str(timezone.now()))
    print('holi test ' + str(timezone.now()+datetime.timedelta(minutes=5)))
    # Leer Hora de archivo de configuracion

    # Aplicar suma de Tiempo, editar

    # LLamar todos los algoritmos para modificar

    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ '/algoritmos/')
    #os.path.join(BASE_DIR, 'log/debug7.log')
    cfgfile = open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/algoritmos/' + "prueba.conf", 'w+')

    Config = configparser.ConfigParser()
    Config.add_section('Temporal_request')
    Config.set('Temporal_request', 't_ini', 'as')
    Config.set('Temporal_request', 't_fin', str(timezone.now()))

    Config.write(cfgfile)
    cfgfile.close()

def updateConfig():
    #incrementa la hora en 15 min ---TIEMPO REAL---
    config = configparser.ConfigParser()
    config.read(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/algoritmos/' + 'configAll.conf')
    tiempo_inicial = config['Temporal_request']['t_ini']
    #tiempo_inicial = datetime.datetime.fromordinal(int(tiempo_inicial))
    tiempo_delta = datetime.timedelta(hours=1)
    tiempo_inicial
    tiempo_delta = '0.'+ str(secondsToDay(tiempo_delta.total_seconds())).replace('.', '')
    fechaIncio = float(tiempo_delta) + float(tiempo_inicial)
    print(fechaIncio)
    fechaFin = float(tiempo_delta)*2 + float(tiempo_inicial)

    #Actualiza el fichero general



    # add the settings to the structure of the file, and lets write it out...i
    saveConfigAll(fechaIncio, fechaFin)

    if executeAlgoEtiqueta(fechaIncio, fechaFin):
        print ('corrio')
    else:
        print('se cae')

def secondsToDay(segundos):
    dia = 86400/segundos
    return dia

def saveConfigAll(t_ini, t_fin):

    ip = '127.0.0.1'
    port = '3306'
    user = 'benja'
    password = ''
    db = 'ufro_ovdas_v1'
    table_iden = 'identificacion_senal'

    # [Confiabilidad_estaciones]
    FRE = '0.99'
    SHG = '0.98'
    LBN = '0.97'
    PTZ = '0.96'
    NBL = '0.95'
    CHS = '0.94'
    FU2 = '0.93'
    PHI = '0.92'
    PLA = '0.91'
    ROB = '0.90'


    cfgfile = open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/algoritmos/' + 'configAll.conf', 'w+')

    # add the settings to the structure of the file, and lets write it out...i
    Config = configparser.ConfigParser()
    Config.add_section('Database')
    Config.set('Database', 'ip', ip)
    Config.set('Database', 'port', port)
    Config.set('Database', 'user', user)
    Config.set('Database', 'password', password)
    Config.set('Database', 'db', db)
    Config.set('Database', 'table_iden', table_iden)

    Config.add_section('Temporal_request')
    Config.set('Temporal_request', 't_ini', str(t_ini))
    Config.set('Temporal_request', 't_fin', str(t_fin))

    Config.add_section('Confiabilidad_estaciones')
    Config.set('Confiabilidad_estaciones', 'FRE', FRE)
    Config.set('Confiabilidad_estaciones', 'SHG', SHG)
    Config.set('Confiabilidad_estaciones', 'LBN', LBN)
    Config.set('Confiabilidad_estaciones', 'PTZ', PTZ)
    Config.set('Confiabilidad_estaciones', 'NBL', NBL)
    Config.set('Confiabilidad_estaciones', 'CHS', CHS)
    Config.set('Confiabilidad_estaciones', 'FU2', FU2)
    Config.set('Confiabilidad_estaciones', 'PHI', PHI)
    Config.set('Confiabilidad_estaciones', 'PLA', PLA)
    Config.set('Confiabilidad_estaciones', 'ROB', ROB)

    Config.write(cfgfile)
    cfgfile.close()



