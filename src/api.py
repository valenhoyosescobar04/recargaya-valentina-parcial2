# src/api.py
from fastapi import FastAPI, HTTPException, Query
from src.recarga import calcular_recarga

app = FastAPI(title="RecargaYa API")


@app.get("/recarga")
def recarga(
    monto: int = Query(..., description="Monto de recarga en pesos"),
    premium: bool = Query(False, description="True si el usuario es premium")
):
    try:
        return calcular_recarga(monto, premium)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)  # nosec B104