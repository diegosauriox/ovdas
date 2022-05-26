from .models import AlertasModel
from datetime import datetime
from alertas.views import crearAlertaVT, crearAlertasMlDr, crearTodasAlertasMlDr
import sys

def subirAlertas():
    today= datetime.today().strftime('%Y-%m-%d')
    alerta= AlertasModel(created_at=d1)
    alerta.save()

def cargarAlertaVT():
    crearAlertaVT()

def cargarAlertaMlDr(t1,t2):
    crearAlertasMlDr(t1,t2)

def cargarTodasAlertasMlDr():
    crearTodasAlertasMlDr()

cargarAlertaMlDr(sys.argv[0],sys.argv[1])