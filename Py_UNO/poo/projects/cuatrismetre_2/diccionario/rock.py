class Desencriptador:
    def __init__(self, diccionario_palabras: list[str]) -> None:
        # Este es tu "banco" de palabras conocidas (ej: ["python", "objeto", "codigo"])
        self.diccionario = diccionario_palabras

    def contar_frecuencias(self, palabra: str) -> dict[str, int]:
        """Cuenta la frecuencia de cada letra en una palabra (Tu función anterior)"""
        frecuencias = {}
        for letra in palabra:
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
        return frecuencias

    def descifrar_por_frecuencia(self, palabra_cifrada: str) -> str:
        """
        Busca en el diccionario qué palabra tiene exactamente la misma
        estructura y frecuencia de letras que la palabra cifrada.
        (Útil si la palabra está desordenada o es un anagrama)
        """
        frecuencias_cifrada = self.contar_frecuencias(palabra_cifrada)

        for palabra_real in self.diccionario:
            # Si tienen distinta cantidad de letras, no perdemos tiempo y seguimos
            if len(palabra_real) != len(palabra_cifrada):
                continue

            # Comparamos sus mapas de frecuencias
            if self.contar_frecuencias(palabra_real) == frecuencias_cifrada:
                return f"¡Coincidencia encontrada! La palabra es: '{palabra_real}'"

        return "No se encontró ninguna coincidencia en el diccionario."

    def descifrar_cesar(self, palabra_cifrada: str, desplazamiento: int) -> str:
        """
        Si la palabra está cifrada moviendo sus letras en el abecedario (Cifrado César),
        este método la mueve hacia atrás y busca si el resultado existe en tu diccionario.
        """
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        palabra_intentada = ""

        # Intentamos "mover" cada letra hacia atrás para deshacer el cifrado
        for letra in palabra_cifrada.lower():
            if letra in alfabeto:
                posicion_actual = alfabeto.find(letra)
                # Restamos el desplazamiento (volvemos al original)
                nueva_posicion = (posicion_actual - desplazamiento) % 26
                palabra_intentada += alfabeto[nueva_posicion]
            else:
                palabra_intentada += letra  # Mantiene espacios o símbolos

        # Ahora que "limpiamos" la palabra, miramos si está en nuestro diccionario
        if palabra_intentada in self.diccionario:
            return f"¡Cifrado César resuelto! Desplazamiento {desplazamiento}. Palabra original: '{palabra_intentada}'"

        return f"Intento fallido con desplazamiento {desplazamiento} (Resultado: '{palabra_intentada}')"
