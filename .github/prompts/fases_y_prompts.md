# Plan de Desarrollo y Prompts Estratégicos

## Fase 1: Modelado de Datos y Estructura Inicial

**Prompt:**

Actúa como experto en logística y bases de datos. Crea modelos de datos usando SQLAlchemy para una aplicación de transporte de carga. Necesito las tablas: Shipment (con campos para modo: aéreo/marítimo/terrestre, origen, destino, tipo de carga, estado, moneda, peso, volumen), Quote, Entity (clientes y proveedores, con datos fiscales y contacto) y Document (vinculados a un shipment). Incluye relaciones y tipos de datos adecuados para Latinoamérica (moneda, pesos, volúmenes).

---

## Fase 2: Lógica de Cotización y Margen

**Prompt:**

Crea una función en Python que calcule el margen de beneficio de un envío. La función debe recibir 'Costos de Compra' (buy rates), 'Tarifas de Venta' (sell rates) y considerar impuestos locales de importación/exportación comunes en Latinoamérica (IVA, retenciones simples). Devuelve el profit bruto y el porcentaje de margen.

---

## Fase 3: Conversión de Unidades y Multimoneda

**Prompt:**

Implementa utilidades en Python para convertir automáticamente entre kilos y libras, y entre metros cúbicos (CBM) y peso volumétrico. Además, agrega soporte para registrar gastos en USD y moneda local (ejemplo: CLP, COP), permitiendo ingresar una tasa de cambio de referencia.

---

## Fase 4: Gestión de Estados y Tracking de Envíos

**Prompt:**

Genera una clase ShipmentManager que gestione el ciclo de vida de un envío: Draft → Quoted → Booked → In Transit → Delivered → Invoiced. Incluye validaciones para que no se pueda facturar un envío que no ha sido entregado o que no tiene documentos cargados.

---

## Fase 5: Gestión de Documentos Logísticos

**Prompt:**

Crea un sistema en Python para asociar y almacenar documentos logísticos (como BL, AWB, Factura Comercial) a cada envío. Permite cargar, listar y validar la existencia de documentos requeridos antes de avanzar de estado.

---

## Fase 6: Endpoints FastAPI

**Prompt:**

Genera endpoints REST usando FastAPI para gestionar Shipments, Quotes, Entities y Documents. Incluye rutas para crear, listar, actualizar y eliminar cada entidad, y para cambiar el estado de un envío.

---

## Fase 7: Diccionario de Términos Logísticos

**Prompt:**

Crea un archivo Markdown en la carpeta docs/ con un glosario de términos logísticos relevantes para Latinoamérica, incluyendo definiciones de BL, AWB, Incoterms, tipos de carga, etc.

---

## Fase 8: Integración y Pruebas

**Prompt:**

Crea un plan de integración para unir todos los módulos desarrollados (modelos, lógica, endpoints y utilidades) en una aplicación FastAPI funcional. Además, genera ejemplos de pruebas unitarias y de integración para los módulos principales (cálculo de margen, conversión de unidades, gestión de estados y documentos), usando pytest. Incluye instrucciones para ejecutar las pruebas y verificar el correcto funcionamiento del sistema.

---

## Fase 9: Autenticación y Autorización

**Prompt:**

Crea un sistema de autenticación y autorización para la aplicación FastAPI, permitiendo el registro y login de usuarios, así como la asignación de roles (ejemplo: admin, operador, cliente). Implementa protección de endpoints según permisos y roles, usando JWT o similar.

---

## Fase 10: Multi-tenant/SaaS

**Prompt:**

Adapta la arquitectura para soportar múltiples clientes (multi-tenant), asegurando la separación de datos y la gestión de entidades por tenant. Incluye estrategias para identificar el tenant en cada request y proteger la información entre clientes.

---

## Fase 11: Creación de Datos Sintéticos

**Prompt:**

Adapta los modelos de datos y los endpoints principales para soportar multi-tenant real, agregando el campo tenant_id a las tablas relevantes (por ejemplo, Shipment, Entity, Quote, Document). Modifica los endpoints para que filtren, creen y validen los datos usando el tenant_id recibido en el header X-Tenant-ID. Incluye ejemplos de cómo implementar esta lógica en SQLAlchemy y FastAPI, y cómo asegurar que cada cliente solo acceda a sus propios datos.

---

## Fase 12: Despliegue y DevOps

**Prompt:**

Crea archivos de configuración para Docker y un pipeline básico de CI/CD (por ejemplo, usando GitHub Actions) para automatizar el despliegue de la aplicación. Incluye instrucciones para construir la imagen, ejecutar la app en contenedores y desplegar en un entorno cloud o local.

---

## Fase 13: Pruebas de la API

**Prompt:**

Crea pruebas automatizadas para la API usando pytest y httpx o requests, cubriendo endpoints públicos y protegidos (login, obtención de token, acceso a recursos según rol). Incluye ejemplos de cómo simular autenticación y verificar respuestas, así como instrucciones para ejecutar estas pruebas.

---

## Fase 14: Seeders y Fixtures de Datos Sintéticos

**Prompt:**

Crea un script ejecutable (seeder) para poblar la base de datos de desarrollo/demo con datos sintéticos realistas, y además integra la generación de datos sintéticos como fixtures reutilizables en los tests automatizados (pytest). Incluye ejemplos de uso para ambos casos y recomendaciones de buenas prácticas para mantener los datos de prueba consistentes y aislados.

---

## Fase 15: Fixtures de Pytest para Datos Sintéticos

**Prompt:**

Crea un fixture de pytest que inicialice una base de datos temporal en memoria y la pueble con datos sintéticos usando la lógica existente. Asegúrate de que cada test tenga datos limpios y aislados. Incluye ejemplos de uso del fixture en pruebas unitarias y de integración, y recomendaciones para mantener la reproducibilidad y limpieza de los tests.
