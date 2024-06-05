from maquina import Maquina
from producto import Producto
from demanda import Demanda
from planificador import Planificador

def main():
    # Creación de productos
    elote_entero = Producto(15, "Elote entero")
    elote_vaso = Producto(16, "Elote en vaso")

    # Creación de máquinas (100 unidades como ejemplo)
    maquina1 = Maquina(1, 100)
    maquina2 = Maquina(2, 100)  # Añadimos una segunda máquina

    # Creación de demandas
    demanda1 = Demanda(elote_entero, 30, "2024-05-27")
    demanda2 = Demanda(elote_vaso, 50, "2024-05-27")
    demanda3 = Demanda(elote_entero, 50, "2024-05-27")  # Nueva demanda para probar la capacidad

    # Planificador
    planificador = Planificador()
    planificador.agregar_maquina(maquina1)
    planificador.agregar_maquina(maquina2)

    # Programación manual
    programado, cantidad_programada = planificador.programar_manual(demanda1, 1)
    print(f"Programado: {programado}, Cantidad: {cantidad_programada}")

    # Desprogramación manual
    desprogramado, cantidad_desprogramada = planificador.desprogramar_manual(demanda1, 1)
    print(f"Desprogramado: {desprogramado}, Cantidad: {cantidad_desprogramada}")

    # Programación automática
    demandas = [demanda1, demanda2, demanda3]
    resultados = planificador.programar_automatico(demandas)
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()
