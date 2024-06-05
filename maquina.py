class Maquina:
    def __init__(self, id, capacidad):
        self.id = id
        self.capacidad = capacidad
        self.produccion = []

    def programar(self, producto, cantidad, fecha_inicio):
        if cantidad <= self.capacidad:
            self.produccion.append({
                'producto': producto,
                'cantidad': cantidad,
                'fecha_inicio': fecha_inicio
            })
            self.capacidad -= cantidad
            return True, cantidad
        return False, 0

    def desprogramar(self, producto, cantidad, fecha_inicio):
        for p in self.produccion:
            if p['producto'].id == producto.id and p['fecha_inicio'] == fecha_inicio:
                if p['cantidad'] >= cantidad:
                    p['cantidad'] -= cantidad
                    self.capacidad += cantidad
                    return True, cantidad
        return False, 0