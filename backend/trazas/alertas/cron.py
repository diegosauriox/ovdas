from .models import AlertasModel
from datetime import datetime

def subirAlertas():
    today= datetime.today().strftime('%Y-%m-%d')
    alerta= AlertasModel(created_at=d1)
    alerta.save()