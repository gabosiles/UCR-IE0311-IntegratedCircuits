import pandas as pd
import matplotlib.pyplot as plt

# Cargar archivo
data = pd.read_csv("MUXES2_1_C17530_sim.txt", delim_whitespace=True)

# Convertir tiempo de segundos a nanosegundos
data['time_ns'] = data['time'] * 1e9

# Crear figura con tres subgráficas
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10), sharex=True)

# Primer gráfico: entradas ina e inb
ax1.plot(data['time_ns'], data['V(ina)'], label='V(ina)', color='red')
ax1.plot(data['time_ns'], data['V(inb)'], label='V(inb)', color='blue')
ax1.set_ylabel("Voltaje [V]")
ax1.set_title("Entradas MUX2:1 -> A y B")
ax1.legend()
ax1.grid(True)
ax1.set_xlim(0, 20)  # Límite del eje X

# Segundo gráfico: señales de control sel y selb
ax2.plot(data['time_ns'], data['V(sel)'], label='V(sel)', color='orange', linestyle='--')
ax2.plot(data['time_ns'], data['V(selb)'], label='V(selb)', color='green', linestyle='--')
ax2.set_ylabel("Voltaje [V]")
ax2.set_title("Señales Control MUX2:1 -> SEL y SEL_B")
ax2.legend()
ax2.grid(True)
ax1.set_xlim(0, 20)  # Límite del eje X

# Tercer gráfico: salidas yout1 y yout2
ax3.plot(data['time_ns'], data['V(yout1)'], label='V(yout1)', color='navy')
ax3.plot(data['time_ns'], data['V(yout2)'], label='V(yout2)', color='brown')
ax3.set_xlabel("Tiempo [ns]")
ax3.set_ylabel("Voltaje [V]")
ax3.set_title("Salidas MUX2:1 -> Y1 [NANDs] y Y2 [TGATE]")
ax3.legend()
ax3.grid(True)
ax1.set_xlim(0, 20)  # Límite del eje X

# Ajustar el diseño
plt.tight_layout()
plt.show()
