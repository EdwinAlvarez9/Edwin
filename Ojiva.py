import pandas as pd

# Crear DataFrame de ejemplo
data = pd.DataFrame({
    'LimInf': [0, 10, 20, 30, 40],
    'LimSup': [10, 20, 30, 40, 50],
    'Frecuencia': [5, 10, 15, 20, 10]
})

data['FrecAcum'] = data['Frecuencia'].cumsum()

plt.figure(figsize=(10, 6))
plt.plot(data['LimSup'], data['FrecAcum'], 'o-', label='Ojiva')
plt.plot([data['LimInf'].iloc[0]] + data['LimSup'].tolist(), 
         [0] + data['FrecAcum'].tolist(), 'o-')
plt.title('Ojiva de Frecuencias Acumuladas')
plt.xlabel('Límites de Clase')
plt.ylabel('Frecuencia Acumulada')
plt.grid(True)
plt.legend()
plt.show()