from datetime import datetime

def sort_numbers(numbers, reverse=False):
    """
    Ordena una lista de números.
    Si reverse=True, los ordena de mayor a menor.
    """
    return sorted(numbers, reverse=reverse)

def main():
    print("======================================")
    print("  Ordenando números con Python")
    print("  (ejecutado desde Jenkins)")
    print("======================================")
    print(f"Fecha y hora de ejecución: {datetime.now()}")
    print()

    numeros = [42, 7, 15, 3, 29, 10]

    print(f"Lista original:     {numeros}")

    ordenados_asc = sort_numbers(numeros)
    print(f"Orden ascendente:   {ordenados_asc}")

    ordenados_desc = sort_numbers(numeros, reverse=True)
    print(f"Orden descendente:  {ordenados_desc}")

    unicos_ordenados = sorted(set(numeros))
    print(f"Números únicos asc: {unicos_ordenados}")

    print("\nScript ejecutado correctamente.")

if __name__ == "__main__":
    main()
