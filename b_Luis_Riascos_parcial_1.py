class ListaHabitos:
    def __init__(self):
        self.habitos = []
        self.matriz_habitos = []

    def agregar_habito(self, nombre, frecuencia, duracion):
        habito = [nombre, frecuencia, duracion]
        self.habitos.append(habito)
        self.ordenar_habitos()  # Ordenar hábitos automáticamente al agregar uno nuevo
        self.actualizar_matriz()
        print(f"Hábito '{nombre}' agregado.")

    def eliminar_habito(self, nombre):
        for habito in self.habitos:
            if habito[0] == nombre:
                self.habitos.remove(habito)
                self.actualizar_matriz()
                print(f"Hábito '{nombre}' eliminado.")
                return
        print(f"Hábito '{nombre}' no encontrado.")

    def mostrar_habitos(self):
        if self.habitos:
            print("Hábitos:")
            for habito in self.habitos:
                print(f"[Nombre: {habito[0]}, Frecuencia: {habito[1]} veces/semana, Duración: {habito[2]} minutos]")
        else:
            print("No hay hábitos registrados.")

    def actualizar_matriz(self):
        n = len(self.habitos)
        self.matriz_habitos = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    self.matriz_habitos[i][j] = min(self.habitos[i][1], self.habitos[j][1])
                else:
                    self.matriz_habitos[i][i] = self.habitos[i][1]

    def ordenar_habitos(self):
        if self.habitos:
            self.habitos = self.merge_sort(self.habitos)
            print("Hábitos ordenados por nombre:")
            self.mostrar_habitos()
        else:
            print("No hay hábitos registrados para ordenar.")

    def merge_sort(self, lista):
        if len(lista) > 1:
            medio = len(lista) // 2
            izquierda = lista[:medio]
            derecha = lista[medio:]
            self.merge_sort(izquierda)
            self.merge_sort(derecha)
            i = j = k = 0
            while i < len(izquierda) and j < len(derecha):
                if izquierda[i][0] < derecha[j][0]:
                    lista[k] = izquierda[i]
                    i += 1
                else:
                    lista[k] = derecha[j]
                    j += 1
                k += 1
            while i < len(izquierda):
                lista[k] = izquierda[i]
                i += 1
                k += 1
            while j < len(derecha):
                lista[k] = derecha[j]
                j += 1
                k += 1
        return lista

def main():
    lista_habitos = ListaHabitos()

    while True:
        print("\nMenú:")
        print("1. Ingresar hábito")
        print("2. Eliminar hábito")
        print("3. Mostrar hábitos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del hábito: ")
            frecuencia = int(input("Ingrese la frecuencia del hábito (por semana): "))
            duracion = int(input("Ingrese la duración del hábito (en minutos): "))
            lista_habitos.agregar_habito(nombre, frecuencia, duracion)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del hábito a eliminar: ")
            lista_habitos.eliminar_habito(nombre)
        elif opcion == "3":
            lista_habitos.mostrar_habitos()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
