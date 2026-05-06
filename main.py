"""
Sistema de Gestión de Notas
Aplicación de consola para gestionar calificaciones estudiantiles
"""

import json
import os
from pathlib import Path
from sistema_notas import registrar_estudiante, listar_estudiantes
from notas import ingresar_nota, obtener_notas
from promedio import obtener_promedio_estudiante, calcular_promedio_general
from reporte import generar_reporte_estudiante, generar_reporte_general
from archivo import guardar_datos_json, cargar_datos_json, exportar_csv, obtener_estadisticas

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
    """Función principal con menú completo"""
    sistema = SistemaNotas()
    
    while True:
        print("\n" + "="*50)
        print("   SISTEMA DE GESTIÓN DE NOTAS - GRUPO 10")
        print("="*50)
        print("1. Registrar estudiante")
        print("2. Ingresar nota")
        print("3. Ver notas de un estudiante")
        print("4. Calcular promedio")
        print("5. Ver promedio general del grupo")
        print("6. Generar reporte de estudiante")
        print("7. Generar reporte general")
        print("8. Exportar a CSV")
        print("9. Ver estadísticas")
        print("10. Listar estudiantes")
        print("11. Salir")
        print("="*50)
        
        opcion = input("Selecciona una opción (1-11): ").strip()
        
        if opcion == "1":
            # Registrar estudiante
            nombre = input("Nombre del estudiante: ")
            id_est = input("ID del estudiante: ")
            exito, mensaje = registrar_estudiante(sistema, nombre, id_est)
            print(mensaje)
        
        elif opcion == "2":
            # Ingresar nota
            id_est = input("ID del estudiante: ")
            asignatura = input("Nombre de la asignatura: ")
            try:
                nota = float(input("Nota (0-5): "))
                exito, mensaje = ingresar_nota(sistema, id_est, asignatura, nota)
                print(mensaje)
            except ValueError:
                print("❌ La nota debe ser un número")
        
        elif opcion == "3":
            # Ver notas de un estudiante
            id_est = input("ID del estudiante: ")
            exito, mensaje = obtener_notas(sistema, id_est)
            print(mensaje)
        
        elif opcion == "4":
            # Calcular promedio
            id_est = input("ID del estudiante: ")
            exito, mensaje = obtener_promedio_estudiante(sistema, id_est)
            print(mensaje)
        
        elif opcion == "5":
            # Promedio general
            promedio_gral = calcular_promedio_general(sistema)
            print(f"\n📊 Promedio general del grupo: {promedio_gral:.2f}")
        
        elif opcion == "6":
            # Reporte de estudiante
            id_est = input("ID del estudiante: ")
            reporte = generar_reporte_estudiante(sistema, id_est)
            print(reporte)
        
        elif opcion == "7":
            # Reporte general
            reporte = generar_reporte_general(sistema)
            print(reporte)
        
        elif opcion == "8":
            # Exportar CSV
            exito, mensaje = exportar_csv(sistema)
            print(mensaje)
        
        elif opcion == "9":
            # Estadísticas
            stats = obtener_estadisticas(sistema)
            print(f"\n📈 ESTADÍSTICAS DEL SISTEMA")
            print(f"  Total de estudiantes: {stats['total_estudiantes']}")
            print(f"  Con notas registradas: {stats['estudiantes_con_notas']}")
            print(f"  Aprobados: {stats['aprobados']}")
            print(f"  Reprobados: {stats['reprobados']}")
            print(f"  Promedio general: {stats['promedio_general']:.2f}\n")
        
        elif opcion == "10":
            # Listar estudiantes
            print(listar_estudiantes(sistema))
        
        elif opcion == "11":
            # Guardar y salir
            guardar_datos_json(sistema)
            print("\n✓ Datos guardados. ¡Hasta luego!")
            break
        
        else:
            print("❌ Opción no válida")


if __name__ == "__main__":
    main()
