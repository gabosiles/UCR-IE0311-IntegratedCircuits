import pandas as pd
import matplotlib.pyplot as plt

# Cargar archivo
data = pd.read_csv("FF_D_SETUP_C17530_sim.txt", delim_whitespace=True)

# Convertir tiempo a nanosegundos
data['time_ns'] = data['time'] * 1e9

# Crear figura con dos subgráficas
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

# Primer gráfico: clk
ax1.plot(data['time_ns'], data['V(clk)'], label='clk', color='black')
ax1.set_ylabel("Voltaje [V]")
ax1.set_title("Reloj: CLK")
ax1.grid(True)
ax1.legend()
ax1.set_xlim(0, 40)  # Ajustá si necesitás más o menos

# Segundo gráfico: ind y outq
ax2.plot(data['time_ns'], data['V(ind)'], label='Input D', color='blue')
ax2.plot(data['time_ns'], data['V(outq)'], label='Output Q', color='red')
ax2.set_xlabel("Tiempo [ns]")
ax2.set_ylabel("Voltaje [V]")
ax2.set_title("Entrada y salida del flip-flop: D y Q")
ax2.grid(True)
ax2.legend()
ax2.set_xlim(0, 40)

# Ajuste final
plt.tight_layout()
plt.show()
