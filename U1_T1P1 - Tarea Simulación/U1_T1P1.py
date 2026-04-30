# =========================================
# SIMULACIÓN DE BACKLOG - SaaS
# =========================================

import random
import matplotlib.pyplot as plt

# -------------------------------
# PARÁMETROS DEL MODELO
# -------------------------------

DIAS = 30

DEMANDA_MIN = XX
DEMANDA_MAX = XXX

CAPACIDAD_FIJA = 10

CAPACIDAD_VAR_MIN = 7
CAPACIDAD_VAR_MAX = 13

# -------------------------------
# FUNCIÓN: generar demanda diaria
# -------------------------------

def generar_demanda():
    # TODO: retornar un número entero aleatorio entre DEMANDA_MIN y DEMANDA_MAX
    pass


# -------------------------------
# FUNCIÓN: generar capacidad variable
# -------------------------------

def generar_capacidad_variable():
    # TODO: retornar un número entero aleatorio entre CAPACIDAD_VAR_MIN y CAPACIDAD_VAR_MAX
    pass


# -------------------------------
# FUNCIÓN PRINCIPAL DE SIMULACIÓN
# -------------------------------

def simular(capacidad_fija=True):
    
    backlog = 0
    historial_backlog = []

    for dia in range(1, DIAS + 1):

        # TODO: generar demanda del día
        demanda = None

        # TODO: definir capacidad según el escenario
        if capacidad_fija:
            capacidad = None
        else:
            capacidad = None

        # TODO: calcular nuevo backlog
        # fórmula: backlog = backlog + demanda - capacidad
        
        # TODO: evitar backlog negativo

        # TODO: guardar backlog en historial
        historial_backlog.append(backlog)

        # (opcional) imprimir día a día
        print(f"Día {dia}: Demanda={demanda}, Capacidad={capacidad}, Backlog={backlog}")

    return backlog, historial_backlog


# -------------------------------
# EJECUCIÓN DE ESCENARIOS
# -------------------------------

print("\n--- ESCENARIO 1: CAPACIDAD FIJA ---")
resultado_fijo, historial_fijo = simular(capacidad_fija=True)

print("\n--- ESCENARIO 2: CAPACIDAD VARIABLE ---")
resultado_variable, historial_variable = simular(capacidad_fija=False)

# -------------------------------
# COMPARACIÓN FINAL
# -------------------------------

print("\nRESULTADOS FINALES:")
print(f"Backlog final (fijo): {resultado_fijo}")
print(f"Backlog final (variable): {resultado_variable}")

# -------------------------------
# GRÁFICO DE HISTORIAL DE BACKLOG 
# -------------------------------

# TODO: Gráfico de comparación

plt.figure(figsize=(12, 6))
plt.plot(historial_fijo, label="Capacidad Fija")
plt.plot(historial_variable, label="Capacidad Variable")
plt.title("Historial de Backlog")
plt.xlabel("Día")
plt.ylabel("Backlog")
plt.legend()
plt.grid()
plt.show()

# TODO: imprimir conclusión simple
if resultado_fijo > resultado_variable:
    print("XXXXXXX")
elif resultado_variable > resultado_fijo:
    print("XXXXXXX")
else:
    print("XXXXXXX")