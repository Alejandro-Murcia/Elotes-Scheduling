from maquina import Maquina
from maquina_preparacion import MaquinaPreparacion
from demanda import Demanda
from datetime import datetime, timedelta

class Planificador:
    def __init__(self):
        self.maquinas = []
    
    def agregar_maquina(self, maquina):
        self.maquinas.append(maquina)
    
    def programar_manual(self, demanda, maquina_id):
        for maquina in self.maquinas:
            if maquina.id == maquina_id:
                programado, cantidad_programada, fecha_fin = maquina.programar(demanda.producto, demanda.cantidad, demanda.fecha_inicio)
                return programado, cantidad_programada, fecha_fin
        return False, 0, None
    
    def desprogramar_manual(self, demanda, maquina_id):
        for maquina in self.maquinas:
            if maquina.id == maquina_id:
                desprogramado, cantidad_desprogramada = maquina.desprogramar(demanda.producto, demanda.cantidad, demanda.fecha_inicio)
                return desprogramado, cantidad_desprogramada
        return False, 0
    
    def programar_automatico(self, demandas):
        resultados = []
        for demanda in demandas:
            asignado = False
            for maquina in self.maquinas:
                if maquina.capacidad >= demanda.cantidad:
                    tiempo_por_elote = 10 if isinstance(maquina, Maquina) else 5
                    fecha_inicio = datetime.strptime(demanda.fecha_inicio, "%Y-%m-%d %H:%M:%S")
                    fecha_fin = fecha_inicio + timedelta(minutes=demanda.cantidad * tiempo_por_elote)
                    if maquina.esta_disponible(fecha_inicio, fecha_fin):
                        programado, cantidad, fecha_fin_str = maquina.programar(demanda.producto, demanda.cantidad, demanda.fecha_inicio)
                        if programado:
                            resultados.append({
                                'Producto': demanda.producto.nombre,
                                'Maquina': maquina.id,
                                'FechaHoraInicio': demanda.fecha_inicio,
                                'FechaHoraFin': fecha_fin_str,
                                'CantidadProgramada': cantidad,
                                'UnidadVentas': "unidades"
                            })
                            asignado = True
                            break
            if not asignado:
                print(f"No se pudo asignar la demanda de {demanda.cantidad} {demanda.producto.nombre}")
        return resultados
