import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt


np.random.seed(42)  # Para reproducibilidad

# Generar datos para el grupo de control
control_group = np.random.normal(loc=150, scale=10, size=100)  # Presión arterial media de 150 con desviación estándar de 10

# Generar datos para el grupo experimental
experimental_group = np.random.normal(loc=140, scale=10, size=100)  # Presión arterial media de 140 con desviación estándar de 10

print('\n--Data frame--\n')
data = pd.DataFrame({
    'Grupo': ['Control'] * 100 + ['Experimental'] * 100,
    'Presion_arterial': np.concatenate([control_group, experimental_group])
})

summary = data.groupby('Grupo').describe()
print(summary)

t_stat, p_value = stats.ttest_ind(control_group, experimental_group)
print(f'T-statistic: {t_stat:.2f}, P-value: {p_value:.4f} \n')


mean_diff = np.mean(control_group) - np.mean(experimental_group)
conf_int = stats.norm.interval(0.95, loc=mean_diff, scale=stats.sem(control_group - experimental_group))
print(f'Intervalo de confianza del 95% para las medias: {conf_int}')


plt.hist(control_group, alpha=0.5, label='Grupo de control')
plt.hist(experimental_group, alpha=0.5, label='Grupo experimental')
plt.legend(loc='upper right')
plt.xlabel('Presion arterial')
plt.ylabel('Frecuencia')
plt.title('Distribucion de presion arterial')
plt.show()


data.boxplot(by='Grupo', column='Presion_arterial', grid=False)
plt.xlabel('Grupo')
plt.ylabel('Presion arterial')
plt.title('Presion arterial por grupo')
plt.suptitle('')
plt.show()


