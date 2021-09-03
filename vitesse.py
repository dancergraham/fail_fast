
from math import log, isclose
import numpy as np

def vitesse(vitesse_ref:float, hauteur:float, rugosite:float):
    """Vitesse moyenne du vent selon l'Eurocode EN 1991-1-4:2005"""

    kr = 0.19 * (rugosite / 0.05) ** 0.07
    cr = kr * np.log(hauteur / rugosite)
    vitesse = vitesse_ref * cr
    return vitesse

# Test selon feuille Gradient_Calcul.xlsx
assert isclose(vitesse(24, 20, 1.0), 
               16.85, 
               abs_tol = 0.01)
