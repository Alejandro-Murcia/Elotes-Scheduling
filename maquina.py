from datetime import datetime, timedelta

class Maquina:
    def __init__(self, id, capacidad):
        self.id = id
        self.capacidad = capacidad
        self.produccion = []

    def programar(self, producto, cantidad, fecha_inicio):
        tiempo_coccion_por_elote = 10  # minutos
        fecha_inicio_dt = datetime.strptime(fecha_inicio, "%Y-%m-%d %H:%M:%S")
        fecha_fin_dt = fecha_inicio_dt + timedelta(minutes=tiempo_coccion_por_elote * cantidad)

        if cantidad <= self.capacidad and self.esta_disponible(fecha_inicio_dt, fecha_fin_dt):
            self.produccion.append({
                'producto': producto,
                'cantidad': cantidad,
                'fecha_inicio': fecha_inicio_dt,
                'fecha_fin': fecha_fin_dt
            })
            self.capacidad -= cantidad
            return True, cantidad, fecha_fin_dt.strftime("%Y-%m-%d %H:%M:%S")
        return False, 0, None

    def desprogramar(self, producto, cantidad, fecha_inicio):
        fecha_inicio_dt = datetime.strptime(fecha_inicio, "%Y-%m-%d %H:%M:%S")
        for p in self.produccion:
            if p['producto'].id == producto.id and p['fecha_inicio'] == fecha_inicio_dt:
                if p['cantidad'] >= cantidad:
                    p['cantidad'] -= cantidad
                    self.capacidad += cantidad
                    return True, cantidad
        return False, 0

    def esta_disponible(self, fecha_inicio, fecha_fin):
        for p in self.produccion:
            if not (fecha_fin <= p['fecha_inicio'] or fecha_inicio >= p['fecha_fin']):
                return False
        return True
