# Análisis Comparativo de Clases IP para Infraestructura en AWS

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5%2B-orange)

Este repositorio contiene un análisis visual de la efectividad de las direcciones IP Clase A, B y C para entornos masivos en AWS, específicamente para alojar 6.27 millones de hosts.

## 📊 Gráficos Generados

El script produce dos gráficos comparativos:
1. **Capacidad por Red**: Muestra hosts disponibles por clase IP
2. **Redes Requeridas**: Calcula cuántas redes se necesitarían para 6.27M hosts

## 🛠 Requisitos

```bash
pip install matplotlib numpy
```

## 🚀 Uso

Ejecutar el script:
```bash
python ip_class_comparison.py
```

## 📌 Resultados Clave

- **Clase A**: Solo requiere 1 red (con división /9)
- **Clase B**: Necesita 96 redes separadas
- **Clase C**: Totalmente inviable (24,685 redes)

## 💡 Aplicación Práctica

Este análisis demuestra por qué AWS utiliza:
- Bloques Clase A (10.0.0.0/8) para VPC
- Jerarquía /16 por región y /20 por AZ
- NAT Gateway compartidos para eficiencia

## 📝 Notas Técnicas

El código:
- Usa escala logarítmica para mejor visualización
- Incluye anotaciones explicativas
- Es personalizable para otros escenarios

## 📄 Licencia

MIT License - Libre para uso y modificación
