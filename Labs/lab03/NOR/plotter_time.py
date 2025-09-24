import matplotlib.pyplot as plt
import numpy as np

# Datos para NOR2 (20/05)
fan_out = np.array([0, 4, 16])
tpdr_nor2 = np.array([72.05, 197.69, 592.16])
tpdf_nor2 = np.array([278.11, 714.94, 2172.09])

# Ajuste lineal
coeff_tpdr_nor2 = np.polyfit(fan_out, tpdr_nor2, 1)
coeff_tpdf_nor2 = np.polyfit(fan_out, tpdf_nor2, 1)

# Funciones ajustadas
fit_tpdr_nor2 = np.poly1d(coeff_tpdr_nor2)
fit_tpdf_nor2 = np.poly1d(coeff_tpdf_nor2)

# Valores para graficar las líneas de ajuste
x_vals = np.linspace(0, 16, 100)
y_tpdr_nor2 = fit_tpdr_nor2(x_vals)
y_tpdf_nor2 = fit_tpdf_nor2(x_vals)

# Crear gráfica
plt.figure(figsize=(8, 5))
plt.plot(fan_out, tpdr_nor2, 'o', color='blue', label='Medidas $t_{pdr}$')
plt.plot(x_vals, y_tpdr_nor2, '-', color='blue',
         label=f'Ajuste $t_{{pdr}}$: y = {coeff_tpdr_nor2[0]:.2f}x + {coeff_tpdr_nor2[1]:.2f}')

plt.plot(fan_out, tpdf_nor2, 'o', color='red', label='Medidas $t_{pdf}$')
plt.plot(x_vals, y_tpdf_nor2, '--', color='red',
         label=f'Ajuste $t_{{pdf}}$: y = {coeff_tpdf_nor2[0]:.2f}x + {coeff_tpdf_nor2[1]:.2f}')

# Estética
plt.xlabel('Fan-Out')
plt.ylabel('Retardo (ps)')
plt.title('Retardos vs Fan-Out para NOR2 20/05')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
