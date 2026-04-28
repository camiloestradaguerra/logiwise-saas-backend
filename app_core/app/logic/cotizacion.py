def calcular_margen_envio(buy_rate, sell_rate, iva=0.19, retencion=0.0):
    """
    Calcula el margen de beneficio de un envío considerando impuestos comunes en Latam.
    :param buy_rate: Costo de compra (float o Decimal)
    :param sell_rate: Tarifa de venta (float o Decimal)
    :param iva: Porcentaje de IVA (ejemplo: 0.19 para 19%)
    :param retencion: Porcentaje de retención (ejemplo: 0.015 para 1.5%)
    :return: (profit_bruto, margen_pct)
    """
    # Cálculo de impuestos sobre la venta
    impuestos = sell_rate * iva + sell_rate * retencion
    profit_bruto = sell_rate - buy_rate - impuestos
    margen_pct = (profit_bruto / sell_rate) * 100 if sell_rate else 0
    return float(profit_bruto), float(margen_pct)

# Ejemplo de uso:
# profit, margen = calcular_margen_envio(1000, 1500, iva=0.19, retencion=0.015)
# print(f"Profit: {profit}, Margen: {margen:.2f}%")
