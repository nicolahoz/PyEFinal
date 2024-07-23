import pandas as pd
import numpy as np
import os

# Configuración de la generación de datos
np.random.seed(42)  # Para reproducibilidad

# Número de muestras
n_samples = 200

# Generación de datos
sexo = np.random.choice(['Masculino', 'Femenino'], size=n_samples)
edad = np.random.randint(30, 80, size=n_samples)
grupo = np.random.choice(['Control', 'Experimental'], size=n_samples)
historial_presion = np.random.choice([True, False], size=n_samples)
dosis_medicamento = np.random.choice([10, 20, 30], size=n_samples)  # en mg
duracion_tratamiento = np.random.randint(1, 12, size=n_samples)  # en semanas

# Presión arterial antes del tratamiento
presion_arterial_antes = np.random.normal(loc=150, scale=10, size=n_samples)

# Presión arterial después del tratamiento con diferentes medias y desviaciones estándar
presion_arterial_despues_control = presion_arterial_antes[:int(n_samples/2)] - np.random.normal(loc=0, scale=5, size=int(n_samples/2))
presion_arterial_despues_experimental = presion_arterial_antes[int(n_samples/2):] - np.random.normal(loc=10, scale=5, size=int(n_samples/2))

presion_arterial_despues = np.concatenate([presion_arterial_despues_control, presion_arterial_despues_experimental])
np.random.shuffle(presion_arterial_despues)

# Creación del DataFrame
data = pd.DataFrame({
    'Sexo': sexo,
    'Edad': edad,
    'Grupo': grupo,
    'Historial_presion_alta': historial_presion,
    'Dosis_medicamento': dosis_medicamento,
    'Duracion_tratamiento': duracion_tratamiento,
    'Presion_arterial_antes': presion_arterial_antes,
    'Presion_arterial_despues': presion_arterial_despues
})

# Guardar el DataFrame en un archivo CSV
csv_path = os.path.dirname(__file__) + '/DataSet.csv'
data.to_csv(csv_path, index=False)