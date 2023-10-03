# Arquivo de testes
import numpy as np
import RobPy as rp

ang = 30.5*np.pi/180

m = rp.matriz_rotacao_x(ang)

print(np.linalg.det(m))