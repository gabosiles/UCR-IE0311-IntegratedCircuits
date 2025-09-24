import pandas as pd
import matplotlib.pyplot as plt

# Cargar archivo
data = pd.read_csv("LATCH_D_C17530_sim.txt", delim_whitespace=True)

# Convertir tiempo a nanosegundos
data['time_ns'] = data['time'] * 1e9

# Crear figura con dos subgráficas
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Primer gráfico: reloj y su inverso
ax1.plot(data['time_ns'], data['V(clk)'], label='V(clk)', color='black')
ax1.plot(data['time_ns'], data['V(clkb)'], label='V(clkb)', color='gray', linestyle='--')
ax1.set_ylabel("Voltaje [V]")
ax1.set_title("Señales de reloj: V(clk) y V(clkb)")
ax1.legend()
ax1.grid(True)
ax1.set_xlim(0, 20)  # Límite opcional, ajustalo si es necesario

# Segundo gráfico: entrada y salida del latch
ax2.plot(data['time_ns'], data['V(ind)'], label='V(ind)', color='blue')
ax2.plot(data['time_ns'], data['V(outq)'], label='V(outq)', color='red')
ax2.set_xlabel("Tiempo [ns]")
ax2.set_ylabel("Voltaje [V]")
ax2.set_title("Entrada y salida del latch: V(ind) y V(outq)")
ax2.legend()
ax2.grid(True)
ax2.set_xlim(0, 20)

# Ajuste final
plt.tight_layout()
plt.show()
