import pandas as pd
import numpy as np
n_filas = 100
sino = [np.random.choice(["Si", "No"]) for i in range(n_filas)]
siemprenunca = [np.random.choice(["Siempre", "Nunca", "Frecuentemente"]) for i in range(n_filas)]
unos = [1]*n_filas
ceros = [0]*n_filas
numeros = [np.random.random() for i in range(n_filas)]
df = pd.DataFrame(dict(
    unos = unos,
    rand = numeros,
    de_acuerdo = sino,
    ceros = ceros,
    frecuencia = siemprenunca))

df.head()