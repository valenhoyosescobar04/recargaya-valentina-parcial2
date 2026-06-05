# features/steps/recarga_steps.py
from pytest_bdd import given, when, then, parsers
from src.recarga import calcular_recarga


@given(parsers.parse("un monto de recarga de {monto:d} pesos"), target_fixture="contexto")
def monto_normal(monto):
    return {"monto": monto, "premium": False}


@given(parsers.parse("un usuario premium con recarga de {monto:d} pesos"), target_fixture="contexto")
def monto_premium(monto):
    return {"monto": monto, "premium": True}


@when("se procesa la recarga", target_fixture="contexto")
def procesar(contexto):
    try:
        contexto["resultado"] = calcular_recarga(contexto["monto"], contexto["premium"])
        contexto["error"] = None
    except ValueError as e:
        contexto["resultado"] = None
        contexto["error"] = str(e)
    return contexto


@then("la recarga es rechazada")
def recarga_rechazada(contexto):
    assert contexto["error"] is not None


@then(parsers.parse("la bonificacion es {bonificacion:d} por ciento"))
def verificar_bonificacion(contexto, bonificacion):
    assert contexto["resultado"]["bonificacion_pct"] == bonificacion