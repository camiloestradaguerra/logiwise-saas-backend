from ..models.models import ShipmentState, Shipment

class ShipmentManager:
    def __init__(self, shipment: Shipment):
        self.shipment = shipment

    def avanzar_estado(self):
        orden = [
            ShipmentState.DRAFT,
            ShipmentState.QUOTED,
            ShipmentState.BOOKED,
            ShipmentState.IN_TRANSIT,
            ShipmentState.DELIVERED,
            ShipmentState.INVOICED,
        ]
        idx = orden.index(self.shipment.state)
        if idx < len(orden) - 1:
            # Validaciones antes de avanzar
            if orden[idx + 1] == ShipmentState.INVOICED:
                if self.shipment.state != ShipmentState.DELIVERED:
                    raise Exception("No se puede facturar un envío no entregado.")
                if not self._tiene_documentos():
                    raise Exception("No se puede facturar sin documentos cargados.")
            self.shipment.state = orden[idx + 1]
        else:
            raise Exception("El envío ya está en el estado final.")

    def _tiene_documentos(self):
        return bool(self.shipment.documents)

    def set_estado(self, nuevo_estado: ShipmentState):
        # Permite cambiar el estado manualmente con validaciones
        if nuevo_estado == ShipmentState.INVOICED:
            if self.shipment.state != ShipmentState.DELIVERED:
                raise Exception("No se puede facturar un envío no entregado.")
            if not self._tiene_documentos():
                raise Exception("No se puede facturar sin documentos cargados.")
        self.shipment.state = nuevo_estado
