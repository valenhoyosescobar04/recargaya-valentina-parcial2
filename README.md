# 📱 RecargaYa - Módulo de Recargas

Módulo de facturación para recargas de celular construido con TDD y BDD.

## Reglas de negocio
- Monto válido: **$1.000 a $50.000** (fuera de rango se rechaza)
- Recarga >= $10.000: **10% de datos de bonificación**
- Recarga >= $30.000: **25% de datos de bonificación**
- Plan premium: **+5% adicional** sobre cualquier bonificación

## Cómo correr las pruebas

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Pruebas unitarias (TDD)
```bash
pytest tests/test_recarga.py -v
```

### Pruebas BDD (Gherkin)
```bash
pytest tests/test_bdd.py -v
```

### Todas las pruebas
```bash
pytest tests/ -v
```

### Seguridad (Bandit)
```bash
bandit -r src/ -ll
```

### API local
```bash
python src/api.py
# Docs en http://localhost:8000/docs
```

### Rendimiento (Locust)
```bash
# Terminal 1
python src/api.py

# Terminal 2
locust -f locustfile.py --host http://localhost:8000
# Abre http://localhost:8089 - usa 30 usuarios
```

## Pipeline CI/CD
- **Todo push**: unitarias + BDD + seguridad
- **Solo main**: también rendimiento con 30 usuarios, P95 < 300ms