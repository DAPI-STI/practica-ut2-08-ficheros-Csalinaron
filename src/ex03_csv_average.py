"""
EX03 (CSV) · Calcular la media de una columna

Objetivo:
- Leer un CSV con cabecera (primera línea).
- Usar la librería estándar `csv` (recomendado: csv.DictReader).
- Convertir datos a float y calcular una media.

Ejemplo típico:
- Un CSV de calificaciones con columnas: name, average
"""

from __future__ import annotations

from pathlib import Path


def csv_average(path: str | Path, column: str) -> float:
    """
    Calcula y devuelve la media de la columna numérica `column` en el CSV `path`.

    Reglas:
    - El CSV tiene cabecera.
    - `column` debe existir en la cabecera. Si no, ValueError.
    - Todos los valores de esa columna deben poder convertirse a float. Si no, ValueError.
    - Si no hay filas de datos (CSV vacío tras la cabecera), ValueError.
    - Si el fichero no existe, FileNotFoundError.

    Ejemplo:
    name,average
    Ana,10
    Luis,6

    csv_average(..., "average") -> 8.0
    """
    if not column or column.strip() == "":
        raise ValueError("El nombre de la columna no puede estar vacío ni solo contener espacios.")

    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"No existe el fichero: {path}")

    with path.open("r", encoding="utf-8", newline="") as fichero:
        lector = csv.DictReader(fichero)
        if lector.fieldnames is None or column not in lector.fieldnames:
            raise ValueError(f"La columna '{column}' no existe en el CSV.")

        valores = []
        for fila in lector:
            valor_crudo = fila.get(column, "").strip()
            try:
                valor = float(valor_crudo)
            except ValueError:
                raise ValueError(f"Valor no numérico en la columna '{column}': {valor_crudo!r}")
            valores.append(valor)

        if not valores:
            raise ValueError("El CSV no contiene filas de datos.")

    return sum(valores) / len(valores)
    raise NotImplementedError("Implementa csv_average(path, column)")
