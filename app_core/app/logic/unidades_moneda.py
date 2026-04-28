"""
Utilidades para conversión de unidades y manejo multimoneda en logística Latam.
"""

# Conversión de unidades
KILOS_A_LIBRAS = 2.20462
CBM_A_PESO_VOLUMETRICO_AEREO = 167  # 1 CBM = 167 kg (aéreo)
CBM_A_PESO_VOLUMETRICO_MARITIMO = 1000  # 1 CBM = 1000 kg (marítimo)


def kilos_a_libras(kg):
    return kg * KILOS_A_LIBRAS

def libras_a_kilos(lb):
    return lb / KILOS_A_LIBRAS

def cbm_a_peso_volumetrico(cbm, modo="aereo"):
    if modo == "aereo":
        return cbm * CBM_A_PESO_VOLUMETRICO_AEREO
    elif modo == "maritimo":
        return cbm * CBM_A_PESO_VOLUMETRICO_MARITIMO
    else:
        raise ValueError("Modo no soportado para conversión volumétrica")

# Multimoneda

def convertir_moneda(monto, tasa_cambio):
    """
    Convierte un monto usando la tasa de cambio proporcionada.
    :param monto: Monto en moneda origen
    :param tasa_cambio: Tasa de cambio (moneda destino / moneda origen)
    :return: Monto en moneda destino
    """
    return monto * tasa_cambio

# Ejemplo de uso:
# print(kilos_a_libras(100))
# print(cbm_a_peso_volumetrico(2.5, modo="aereo"))
# print(convertir_moneda(1000, 950))  # 1000 USD a CLP si 1 USD = 950 CLP
