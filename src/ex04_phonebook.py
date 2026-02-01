"""
EX04 (Texto) · Listín telefónico en fichero

Vas a implementar un pequeño "CRUD" (Crear/Leer/Actualizar/Borrar) de contactos,
guardados en un fichero de texto.

Formato del fichero (una línea por contacto):
nombre,telefono

Ejemplo:
Ana,600123123
Luis,600000000

Para que el ejercicio sea más limpio, se proponen dos funciones "privadas":
- _load_phonebook(): lee el fichero y lo convierte en dict
- _save_phonebook(): guarda el dict en el fichero

Luego, las funciones públicas usan esas helpers:
- add_contact(): alta/actualización
- get_phone(): consulta
- remove_contact(): baja
"""

from __future__ import annotations

from pathlib import Path


def _load_phonebook(path: str | Path) -> dict[str, str]:
    path = Path(path)
    if not path.exists():
        return {}

    phonebook: dict[str, str] = {}

    with path.open("r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 2:
                raise ValueError
            name = parts[0].strip()
            phone = parts[1].strip()
            phonebook[name] = phone

    return phonebook


def _save_phonebook(path: str | Path, phonebook: dict[str, str]) -> None:
    path = Path(path)
    with path.open("w", encoding="utf-8", newline="") as f:
        for name, phone in phonebook.items():
            f.write(f"{name},{phone}\n")


def add_contact(path: str | Path, name: str, phone: str) -> None:
    name_clean = name.strip()
    phone_clean = phone.strip()
    if not name_clean or not phone_clean:
        raise ValueError

    pb = _load_phonebook(path)
    pb[name_clean] = phone_clean
    _save_phonebook(path, pb)


def get_phone(path: str | Path, name: str) -> str | None:
    name_clean = name.strip()
    pb = _load_phonebook(path)
    return pb.get(name_clean)


def remove_contact(path: str | Path, name: str) -> bool:
    path = Path(path)
    if not path.exists():
        return False

    name_clean = name.strip()
    pb = _load_phonebook(path)

    if name_clean not in pb:
        return False

    del pb[name_clean]
    _save_phonebook(path, pb)
    return True

    raise NotImplementedError("Implementa remove_contact(path, name)")
