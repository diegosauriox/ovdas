import pandas as pd
import numpy as np
import mysql.connector
import configparser,string,sys,os
# Inicialización

def executeMain():
    print('entra a algoritmo de alejandro')
    config = configparser.ConfigParser()
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    config.read(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/UpdateEtiqueta/clasi.conf')
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/UpdateEtiqueta/clasi.conf')
    #config.read('./algoritmos/UpdateEtiqueta/clasi.conf')# debe estar en la carpeta de ejecucion
    print('debaeri haber leido los datos')
    fbx = mysql.connector.connect(
    	user=config['Database']['user'],
    	password=config['Database']['password'],
    	host=config['Database']['ip'],
    	port=config['Database']['port'],
    	database=config['Database']['db'])

    t_ini = config['Temporal_request']['t_ini']
    t_fin = config['Temporal_request']['t_fin']
    # Consulta
    #query1 = ('select * from identificacion_senal')
    # example
    #select * from ufro_ovdas_v1.identificacion_senal where ufro_ovdas_v1.identificacion_senal.inicio between 737061.2 and 737061.5;
    query1=('select * from '+config['Database']['db']+'.'+config['Database']['table_iden']+' where '+
            config['Database']['db']+'.'+config['Database']['table_iden']+'.inicio between '+t_ini+' and '+t_fin+';')
    #query1 = ('show columns from identificacion_senal')
    ########################################
    # Ejecición de auror.a
    cursor = fbx.cursor()
    cursor.execute(query1)
    result1 = cursor.fetchall()

    df1 = pd.DataFrame(result1)
    print(df1)
    df1 = df1.iloc[:, [0,3,10,17,18,19,20]]
    df1.columns = ['cod_event','est','label_event','prob_vt','prob_lp','prob_tr','prob_ot']

    query2 = ('select * from avistamiento_registro')

    cursor = fbx.cursor()
    cursor.execute(query2)
    result2 = cursor.fetchall()

    df2 = pd.DataFrame(result2)
    df2 = df2.iloc[:, [2,0]]
    df2.columns = ['code_macroevent','cod_event']

    df = pd.merge(df2,df1)

    """
    Tercero se calcula la confiabilidad y la clasificación.
    Se utilizan las siguientes ponderaciones de las estaciones:
        FRE=0.99, SHG=0.98, LBN=0.97, PTZ=0.96, NBL=0.95, 
        CHS=0.94, FU2=0.93, PHI=0.92, PLA=0.91, ROB=0.90
    """
    print('calcula la confiabilidad')
    FRE = float(config['Confiabilidad_estaciones']['FRE'])
    SHG = float(config['Confiabilidad_estaciones']['SHG'])
    LBN = float(config['Confiabilidad_estaciones']['LBN'])
    PTZ = float(config['Confiabilidad_estaciones']['PTZ'])
    NBL = float(config['Confiabilidad_estaciones']['NBL'])
    CHS = float(config['Confiabilidad_estaciones']['CHS'])
    FU2 = float(config['Confiabilidad_estaciones']['FU2'])
    PHI = float(config['Confiabilidad_estaciones']['PHI'])
    PLA = float(config['Confiabilidad_estaciones']['PLA'])
    ROB = float(config['Confiabilidad_estaciones']['ROB'])

    conf = dict([('FRE',FRE),('SHG',SHG),('LBN',LBN),('PTZ',PTZ),('NBL',NBL),
                 ('CHS',CHS),('FU2',FU2),('PHI',PHI),('PLA',PLA),('ROB',ROB)])

    conf_est = []
    for x in df.est:
        if x in conf.keys():
            conf_est.append(conf[x])
        else:
            conf_est.append(0)

    #Añadir columna de confiabilidad de estaciones
    df['conf_est'] = conf_est

    def ponderacion_est(data):
        p_LP = data['prob_lp']*data['conf_est']
        p_TR = data['prob_tr']*data['conf_est']
        p_VT = data['prob_vt']*data['conf_est']
        p_OT = data['prob_ot']*data['conf_est']
        data.loc[:,'LP'] = p_LP
        data.loc[:,'TR'] = p_TR
        data.loc[:,'VT'] = p_VT
        data.loc[:,'OT'] = p_OT

    #Añadir columnas con ponderación estación*proba_evento
    ponderacion_est(df)

    # clasifica basado en el valor máximo de la ponderación
    df['class_macroevent'] = np.zeros(len(df))

    df['conf'] = np.zeros(len(df))

    df['prob_class'] = np.zeros(len(df))
    for f in df.code_macroevent.unique():
        #Identificamos el macroevento
        me = df.loc[df.loc[:, 'code_macroevent'] == f]
        #Seleccionamos columnas de la ponderación
        col = me.iloc[:,[9,10,11,12]].values
        x = np.where(col == np.max(col))
        cl = x[1][0]
        clases = ['LP','TR','VT','OT']
        df.class_macroevent.loc[df.loc[:, 'code_macroevent'] == f] = clases[cl]
        #Calculamos confiabilidad
        confi = col.max()
        df.conf.loc[df.loc[:, 'code_macroevent'] == f] = confi
        #Seleccionamos columnas de las probabilidades
        col2 = me.iloc[:,[4,5,6,7]]
        prob = col2.values.max()
        df.prob_class.loc[df.loc[:, 'code_macroevent'] == f] = prob

    """
    Finalmente se genera la Tabla5
    """

    dff = df.iloc[:, [0,1,13,14,15]]
    dff.columns = ['code_macroevent','code_event','class_macroevent','conf','prob_class']

    #dff.to_csv('Tabla_5.csv', index=False, header=True, encoding='utf-8')
    # Consulta
    connection = mysql.connector.connect(host=config['Database']['ip'],
                                             database=config['Database']['db'],
                                             user=config['Database']['user'],
                                             password=config['Database']['password'])
    cursor = connection.cursor()
    for row in dff.iloc:
        sql_update_query = """Update identificacion_senal set prob_ge = %s, c_label = %s where cod_event = %s"""
        parametros = (float(row.conf), float(row.prob_class), row.code_event)
        cursor.execute(sql_update_query, parametros)

        sql_update_query2 = """Update evento_macro set clasificacion = %s where evento_macro_id = %s"""
        parametros = (row.class_macroevent, row.code_macroevent)
        cursor.execute(sql_update_query2, parametros)

    connection.commit()

    return True
