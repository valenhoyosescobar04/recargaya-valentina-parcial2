# tests/test_recarga.py
import pytest
from src.recarga import calcular_recarga


class TestValidacionMonto:

    def test_monto_menor_al_minimo_es_rechazado(self):
        with pytest.raises(ValueError):
            calcular_recarga(999)

    def test_monto_cero_es_rechazado(self):
        with pytest.raises(ValueError):
            calcular_recarga(0)

    def test_monto_negativo_es_rechazado(self):
        with pytest.raises(ValueError):
            calcular_recarga(-1000)

    def test_monto_mayor_al_maximo_es_rechazado(self):
        with pytest.raises(ValueError):
            calcular_recarga(50001)

    def test_monto_minimo_es_aceptado(self):
        resultado = calcular_recarga(1000)
        assert resultado["monto"] == 1000

    def test_monto_maximo_es_aceptado(self):
        resultado = calcular_recarga(50000)
        assert resultado["monto"] == 50000


class TestBonificacionDatos:

    def test_menos_de_10000_no_tiene_bonificacion(self):
        resultado = calcular_recarga(5000)
        assert resultado["bonificacion_pct"] == 0

    def test_exactamente_9999_no_tiene_bonificacion(self):
        resultado = calcular_recarga(9999)
        assert resultado["bonificacion_pct"] == 0

    def test_exactamente_10000_tiene_10_pct(self):
        resultado = calcular_recarga(10000)
        assert resultado["bonificacion_pct"] == 10

    def test_entre_10000_y_29999_tiene_10_pct(self):
        resultado = calcular_recarga(20000)
        assert resultado["bonificacion_pct"] == 10

    def test_exactamente_29999_tiene_10_pct(self):
        resultado = calcular_recarga(29999)
        assert resultado["bonificacion_pct"] == 10

    def test_exactamente_30000_tiene_25_pct(self):
        resultado = calcular_recarga(30000)
        assert resultado["bonificacion_pct"] == 25

    def test_mas_de_30000_tiene_25_pct(self):
        resultado = calcular_recarga(50000)
        assert resultado["bonificacion_pct"] == 25

class TestDatosBonificados:
    """Verifica que los MB extra se calculen correctamente"""

    def test_sin_bonificacion_datos_extra_es_cero(self):
        resultado = calcular_recarga(5000)
        assert resultado["datos_extra_mb"] == 0

    def test_10000_con_10_pct_da_1000_mb(self):
        resultado = calcular_recarga(10000)
        assert resultado["datos_extra_mb"] == 1000

    def test_30000_con_25_pct_da_7500_mb(self):
        resultado = calcular_recarga(30000)
        assert resultado["datos_extra_mb"] == 7500

    def test_10000_premium_15_pct_da_1500_mb(self):
        resultado = calcular_recarga(10000, premium=True)
        assert resultado["datos_extra_mb"] == 1500

    def test_resultado_contiene_todos_los_campos(self):
        resultado = calcular_recarga(10000)
        assert "monto" in resultado
        assert "premium" in resultado
        assert "bonificacion_pct" in resultado
        assert "datos_extra_mb" in resultado

class TestValoresLimite:

    @pytest.mark.parametrize("monto,premium,bonificacion_pct,datos_extra_mb,valido", [
        (999,   False, None, None,  False),  # límite inferior rechazado
        (1000,  False, 0,    0,     True),   # límite inferior aceptado
        (9999,  False, 0,    0,     True),   # justo antes del 10%
        (10000, False, 10,   1000,  True),   # exactamente umbral 10%
        (29999, False, 10,   2999,  True),   # justo antes del 25%
        (30000, False, 25,   7500,  True),   # exactamente umbral 25%
        (50000, False, 25,   12500, True),   # límite superior aceptado
        (50001, False, None, None,  False),  # límite superior rechazado
        (10000, True,  15,   1500,  True),   # premium + 10%
        (30000, True,  30,   9000,  True),   # premium + 25%
    ])
    def test_tabla_equivalencia(self, monto, premium, bonificacion_pct, datos_extra_mb, valido):
        if not valido:
            with pytest.raises(ValueError):
                calcular_recarga(monto, premium)
        else:
            resultado = calcular_recarga(monto, premium)
            assert resultado["bonificacion_pct"] == bonificacion_pct
            assert resultado["datos_extra_mb"] == datos_extra_mb