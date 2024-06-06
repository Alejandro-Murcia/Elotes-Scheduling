from maquina import Maquina
from maquina_preparacion import MaquinaPreparacion
from producto import Producto
from demanda import Demanda
from planificador import Planificador

def main():
    # Creación de productos
    elote_entero = Producto(15, "Elote Entero")
    elote_vaso = Producto(16, "Elote en Vaso")

    # Creación de máquinas (capacidad de 100 unidades por ejemplo)
    maquina_coccion1 = Maquina(1, 100)
    maquina_coccion2 = Maquina(2, 100)
    maquina_preparacion1 = MaquinaPreparacion(3, 100)  # Persona 1
    maquina_preparacion2 = MaquinaPreparacion(4, 100)  # Persona 2

    # Planificador
    planificador = Planificador()
    planificador.agregar_maquina(maquina_coccion1)
    planificador.agregar_maquina(maquina_coccion2)
    planificador.agregar_maquina(maquina_preparacion1)
    planificador.agregar_maquina(maquina_preparacion2)

    print("\n--- Programación Manual ---")
    
    # Creación de demandas
    demanda1 = Demanda(elote_entero, 30, "2024-05-27 08:00:00")
    demanda2 = Demanda(elote_vaso, 50, "2024-05-27 08:30:00")
    demanda3 = Demanda(elote_entero, 50, "2024-05-27 09:00:00")  # Nueva demanda para probar la capacidad

    # Programación manual
    programado, cantidad_programada, fecha_fin = planificador.programar_manual(demanda1, 1)
    if programado:
        print(f"\nProgramación manual exitosa:")
        print(f"  Producto: {demanda1.producto.nombre}")
        print(f"  Cantidad: {cantidad_programada}")
        print(f"  Fecha de inicio: {demanda1.fecha_inicio}")
        print(f"  Fecha de finalización: {fecha_fin}")
        print(f"  Máquina: {maquina_coccion1.id}")
    else:
        print(f"\nProgramación manual fallida para la demanda de {demanda1.cantidad} unidades de {demanda1.producto.nombre}")

    print("\n--- Desprogramación Manual ---")

    # Desprogramación manual
    desprogramado, cantidad_desprogramada = planificador.desprogramar_manual(demanda1, 1)
    if desprogramado:
        print(f"\nDesprogramación manual exitosa:")
        print(f"  Producto: {demanda1.producto.nombre}")
        print(f"  Cantidad desprogramada: {cantidad_desprogramada}")
        print(f"  Fecha de inicio: {demanda1.fecha_inicio}")
        print(f"  Máquina: {maquina_coccion1.id}")
    else:
        print(f"\nDesprogramación manual fallida para la demanda de {demanda1.cantidad} unidades de {demanda1.producto.nombre}")

    print("\n--- Programación Automática ---")

    # Programación automática
    demandas = [demanda1, demanda2, demanda3]
    resultados = planificador.programar_automatico(demandas)
    print(f"\nResultados de la programación automática:")
    for resultado in resultados:
        print(f"  Producto: {resultado['Producto']}")
        print(f"  Cantidad: {resultado['CantidadProgramada']}")
        print(f"  Fecha de inicio: {resultado['FechaHoraInicio']}")
        print(f"  Fecha de finalización: {resultado['FechaHoraFin']}")
        print(f"  Máquina: {resultado['Maquina']}")
        print()

if __name__ == "__main__":
    main()
