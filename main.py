"""
Sistema de Gestión de Notas
Aplicación de consola para gestionar calificaciones estudiantiles
"""

import json
import os
from pathlib import Path
from sistema_notas import registrar_estudiante, listar_estudiantes

class SistemaNotas:
    """Clase principal para gestionar estudiantes y notas"""
    
    def __init__(self, archivo_datos="data.json"):
        self.archivo_datos = archivo_datos
        self.estudiantes = {}
        self.cargar_datos()
    
    def cargar_datos(self):
        """Carga los datos desde el archivo JSON"""
        if os.path.exists(self.archivo_datos):
            with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                self.estudiantes = json.load(f)
    
    def guardar_datos(self):
        """Guarda los datos en el archivo JSON"""
        with open(self.archivo_datos, 'w', encoding='utf-8') as f:
            json.dump(self.estudiantes, f, indent=2, ensure_ascii=False)


def main():
    """Función principal"""
    sistema = SistemaNotas()
    
    while True:
        print("\n" + "="*40)
        print("   SISTEMA DE GESTIÓN DE NOTAS")
        print("="*40)
        print("1. Registrar estudiante")
        print("2. Ingresar notas")
        print("3. Ver promedio")
        print("4. Generar reporte")
        print("5. Salir")
        print("="*40)
        
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            nombre = input("Nombre del estudiante: ")
            id_est = input("ID del estudiante: ")
            exito, mensaje = registrar_estudiante(sistema, nombre, id_est)
            print(mensaje)
            if exito:
                print(listar_estudiantes(sistema))
        
        elif opcion == "5":
            print("\n¡Hasta luego!")
            break
        
        else:
            print("❌ Opción no válida")


if __name__ == "__main__":
    main()
