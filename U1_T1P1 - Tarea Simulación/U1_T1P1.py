# =========================================
# SIMULACIÓN DE BACKLOG - SaaS
# =========================================

import random
import matplotlib.pyplot as plt

# -------------------------------
# PARÁMETROS DEL MODELO
# -------------------------------

DIAS = 30

DEMANDA_MIN = 5
DEMANDA_MAX = 15

CAPACIDAD_FIJA = 10

CAPACIDAD_VAR_MIN = 7
CAPACIDAD_VAR_MAX = 13

# -------------------------------
# FUNCIÓN: generar demanda diaria
# -------------------------------


def generar_demanda() -> int:
    '''
    Retorna un número entero aleatorio
    entre DEMANDA_MIN y DEMANDA_MAX
    '''
    return random.randint(DEMANDA_MIN, DEMANDA_MAX)


# -------------------------------
# FUNCIÓN: generar capacidad variable
# -------------------------------

def generar_capacidad_variable() -> int:
    '''
    Retorna un número entero aleatorio entre
    CAPACIDAD_VAR_MIN y CAPACIDAD_VAR_MAX
    '''
    return random.randint(CAPACIDAD_VAR_MIN, CAPACIDAD_VAR_MAX)


# -------------------------------
# FUNCIÓN PRINCIPAL DE SIMULACIÓN
# -------------------------------

def simular(capacidad_fija=True):

    backlog = 0
    historial_backlog = []

    for dia in range(0, DIAS):

        # TODO: generar demanda del día
        demanda = generar_demanda()

        # TODO: definir capacidad según el escenario
        if capacidad_fija:
            capacidad = CAPACIDAD_FIJA
        else:
            capacidad = generar_capacidad_variable()

        # TODO: calcular nuevo backlog
        # fórmula: backlog = backlog + demanda - capacidad
        if historial_backlog is not None and dia > 0:
            backlog_anterior = historial_backlog[dia - 1]
        else:
            backlog_anterior = backlog

        backlog = backlog_anterior + demanda - capacidad

        # TODO: evitar backlog negativo
        backlog = max(0, backlog)

        # TODO: guardar backlog en historial
        historial_backlog.append(backlog)

        # (opcional) imprimir día a día
        print(f"Día {dia}: Demanda={demanda}, \
            Capacidad={capacidad}, \
            Backlog={backlog}")

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
    print("La capacidad variable es más eficiente")
elif resultado_variable > resultado_fijo:
    print("La capacidad fija es más eficiente")
else:
    print("Ambas tienen la misma eficiencia")
