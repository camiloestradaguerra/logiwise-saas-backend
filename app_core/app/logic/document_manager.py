import os
from datetime import datetime
from app_core.app.models.models import Document, Shipment

class DocumentManager:
    def __init__(self, shipment: Shipment, storage_dir: str):
        self.shipment = shipment
        self.storage_dir = storage_dir

    def cargar_documento(self, doc_type: str, file_content: bytes, filename: str):
        # Guarda el archivo en el storage_dir y crea el registro Document
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)
        file_path = os.path.join(self.storage_dir, filename)
        with open(file_path, 'wb') as f:
            f.write(file_content)
        doc = Document(
            shipment_id=self.shipment.id,
            doc_type=doc_type,
            file_path=file_path,
            uploaded_at=datetime.utcnow()
        )
        self.shipment.documents.append(doc)
        return doc

    def listar_documentos(self):
        return self.shipment.documents

    def validar_documentos_requeridos(self, requeridos=None):
        if requeridos is None:
            requeridos = ["BL", "AWB", "Factura"]
        tipos_cargados = {doc.doc_type for doc in self.shipment.documents}
        faltantes = [tipo for tipo in requeridos if tipo not in tipos_cargados]
        if faltantes:
            raise Exception(f"Faltan documentos requeridos: {faltantes}")
        return True
