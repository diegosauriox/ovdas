from criterioAlerta.models import CriterioAlertaModel

def getUmbralVT(volcan_id):
    criterio = CriterioAlertaModel.objects.get(volcan_id=volcan_id)
    #datos = {"umbral_vt": criterio.umbral_vt}
    return criterio.umbral_vt

def getUmbralDR(volcan_id):
    criterio = CriterioAlertaModel.objects.get(volcan_id=volcan_id)
    #datos = {"umbral_vt": criterio.umbral_vt}
    return criterio.umbral_dr