# src/recarga.py

MONTO_MINIMO = 1_000
MONTO_MAXIMO = 50_000
UMBRAL_BONIFICACION_MEDIA = 10_000
UMBRAL_BONIFICACION_ALTA = 30_000
BONIFICACION_MEDIA_PCT = 10
BONIFICACION_ALTA_PCT = 25
BONIFICACION_PREMIUM_PCT = 5


def calcular_recarga(monto: int, premium: bool = False) -> dict:

    if monto < MONTO_MINIMO or monto > MONTO_MAXIMO:
        raise ValueError(
            f"Monto ${monto} inválido. Debe estar entre "
            f"${MONTO_MINIMO} y ${MONTO_MAXIMO}."
        )

    if monto >= UMBRAL_BONIFICACION_ALTA:
        bonificacion_pct = BONIFICACION_ALTA_PCT
    elif monto >= UMBRAL_BONIFICACION_MEDIA:
        bonificacion_pct = BONIFICACION_MEDIA_PCT
    else:
        bonificacion_pct = 0

    if premium:
        bonificacion_pct += BONIFICACION_PREMIUM_PCT

    datos_extra_mb = int(monto * bonificacion_pct / 100)

    return {
        "monto": monto,
        "premium": premium,
        "bonificacion_pct": bonificacion_pct,
        "datos_extra_mb": datos_extra_mb,
    }