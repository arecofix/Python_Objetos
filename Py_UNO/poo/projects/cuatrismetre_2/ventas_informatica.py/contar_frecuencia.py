def contar_frecuencias(palabra: list[str]) -> dict[str, int]:
    frecuencias: dict[str, int] = {}

    for p in palabra:  # Corregido a 'palabra' (singular)
        if p not in frecuencias.keys():
            value = 1
        else:
            value = frecuencias[p] + 1

        # Guardamos el valor asignándolo directamente a la clave 'p'
        frecuencias[p] = value

    return frecuencias
