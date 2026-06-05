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


class TestPlanPremium:
    """Regla: premium suma 5% adicional"""

    def test_premium_sin_bonificacion_base_suma_5_pct(self):
        resultado = calcular_recarga(5000, premium=True)
        assert resultado["bonificacion_pct"] == 5

    def test_premium_con_10_pct_base_da_15_pct(self):
        resultado = calcular_recarga(10000, premium=True)
        assert resultado["bonificacion_pct"] == 15

    def test_premium_con_25_pct_base_da_30_pct(self):
        resultado = calcular_recarga(30000, premium=True)
        assert resultado["bonificacion_pct"] == 30

    def test_no_premium_no_suma_extra(self):
        resultado = calcular_recarga(10000, premium=False)
        assert resultado["bonificacion_pct"] == 10