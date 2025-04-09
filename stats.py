import matplotlib.pyplot as plt
import numpy as np

# Configuración
classes = ['Clase A (10.0.0.0/8)', 'Clase B (172.16.0.0/12)', 'Clase C (192.168.0.0/16)']
hosts_per_network = [16777214, 65534, 254]  # Hosts útiles por red
networks_needed = np.ceil(6270000 / np.array(hosts_per_network))  # Redes requeridas para 6.27M hosts

# Gráfico comparativo
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Efectividad de Clases IP para 6.27M hosts en AWS', fontweight='bold')

# Gráfico 1: Hosts por red
ax1.bar(classes, hosts_per_network, color=['#4CAF50', '#FFC107', '#F44336'])
ax1.set_title('Capacidad por Red', pad=20)
ax1.set_ylabel('Hosts disponibles')
ax1.set_yscale('log')
ax1.grid(axis='y', linestyle='--')

# Añadir etiquetas exactas
for i, v in enumerate(hosts_per_network):
    ax1.text(i, v*1.1, f"{v:,}", ha='center')

# Gráfico 2: Redes necesarias
ax2.bar(classes, networks_needed, color=['#4CAF50', '#FFC107', '#F44336'])
ax2.set_title('Redes Requeridas para 6.27M hosts', pad=20)
ax2.set_ylabel('Número de redes')
ax2.grid(axis='y', linestyle='--')

# Añadir etiquetas
for i, v in enumerate(networks_needed):
    ax2.text(i, v*1.1, f"{int(v):,}", ha='center')

plt.tight_layout()
plt.show()