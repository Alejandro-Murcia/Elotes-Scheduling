from maquina import Maquina
from demanda import Demanda

class Planificador:
    def __init__(self):
        self.maquinas = []

    def agregar_maquina(self, maquina):
        self.maquinas.append(maquina)

    def programar_manual(self, demanda, maquina_id):
        for maquina in self.maquinas:
            if maquina.id == maquina_id:
                return maquina.programar(demanda.producto, demanda.cantidad, demanda.fecha_inicio)
        return False, 0

    def desprogramar_manual(self, demanda, maquina_id):
        for maquina in self.maquinas:
            if maquina.id == maquina_id:
                return maquina.desprogramar(demanda.producto, demanda.cantidad, demanda.fecha_inicio)
        return False, 0

    def programar_automatico(self, demandas):
        resultados = []
        for demanda in demandas:
            asignado = False
            for maquina in self.maquinas:
                if maquina.capacidad >= demanda.cantidad:
                    programado, cantidad = maquina.programar(demanda.producto, demanda.cantidad, demanda.fecha_inicio)
                    if programado:
                        resultados.append({
                            'Producto': demanda.producto.nombre,
                            'Maquina': maquina.id,
                            'FechaHoraInicio': demanda.fecha_inicio,
                            'FechaHoraFin': "Desconocido", 
                            'CantidadProgramada': cantidad,
                            'UnidadVentas': "unidades"  
                        })
                        asignado = True
                        break
            if not asignado:
                print(f"No se pudo asignar la demanda de {demanda.cantidad} {demanda.producto.nombre}")
        return resultados
