import pandas as pd
import matplotlib.pyplot as plt

# Cargar archivo
data = pd.read_csv("TGATE_10_10_C17530_sim.txt", delim_whitespace=True)

# Convertir tiempo de segundos a nanosegundos
data['time_ns'] = data['time'] * 1e9

# Parámetros de visualización para eje x (en ns)
x_min = 0        # mínimo del eje x en ns
x_max = 25       # máximo del eje x en ns

# Crear figura con dos subgráficas verticales
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Primer gráfico: señales de control
ax1.plot(data['time_ns'], data['V(sel)'], label='V(sel)', color='orange')
ax1.plot(data['time_ns'], data['V(selb)'], label='V(selb)', color='green')
ax1.set_ylabel("Voltaje [V]", fontsize=13)
ax1.set_title("Señales de control select y select bar", fontsize=15)
ax1.grid(True)
ax1.legend(fontsize=12, loc='upper right')
ax1.set_xlim(x_min, x_max)

# Segundo gráfico: señales de datos
ax2.plot(data['time_ns'], data['V(ina)'], label='V(ina)', color='red', linewidth=3)
ax2.plot(data['time_ns'], data['V(out_y)'], label='V(out_y)', color='navy')
ax2.set_xlabel("Tiempo [ns]", fontsize=13)
ax2.set_ylabel("Voltaje [V]", fontsize=13)
ax2.set_title("Señales de entrada A y salida Y", fontsize=15)
ax2.grid(True)
ax2.legend(fontsize=12, loc='upper right')
ax2.set_xlim(x_min, x_max)

# Ajustar el diseño
plt.tight_layout()
plt.show()
