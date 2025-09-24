import matplotlib.pyplot as plt
import numpy as np

# Datos de la tabla
fan_out = np.array([0, 4, 16])
tpdr = np.array([70.12, 236.97, 761.94])
tpdf = np.array([69.64, 238.56, 810.20])

# Ajuste lineal (recta de mejor ajuste)
coeff_tpdr = np.polyfit(fan_out, tpdr, 1)
coeff_tpdf = np.polyfit(fan_out, tpdf, 1)

# Crear funciones de ajuste
fit_tpdr = np.poly1d(coeff_tpdr)
fit_tpdf = np.poly1d(coeff_tpdf)

# Valores para graficar las líneas
x_vals = np.linspace(0, 16, 100)
y_tpdr = fit_tpdr(x_vals)
y_tpdf = fit_tpdf(x_vals)

# Crear gráfica
plt.figure(figsize=(8, 5))
plt.plot(fan_out, tpdr, 'o', color='orange', label='Medidas $t_{pdr}$')
plt.plot(x_vals, y_tpdr, '-', color='orange',
         label=f'Ajuste $t_{{pdr}}$: y = {coeff_tpdr[0]:.2f}x + {coeff_tpdr[1]:.2f}')

plt.plot(fan_out, tpdf, 'o', color='blue', label='Medidas $t_{pdf}$')
plt.plot(x_vals, y_tpdf, '--', color='blue',
         label=f'Ajuste $t_{{pdf}}$: y = {coeff_tpdf[0]:.2f}x + {coeff_tpdf[1]:.2f}')

# Estética
plt.xlabel('Fan-Out')
plt.ylabel('Retardo (ps)')
plt.title('Retardos vs Fan-Out para NAND2 10/10')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
