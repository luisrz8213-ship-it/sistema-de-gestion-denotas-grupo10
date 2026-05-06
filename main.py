"""
Sistema de Gestión de Notas
Aplicación de consola para gestionar calificaciones estudiantiles
"""

import json
import os
from pathlib import Path

# Importan módulos internos (se crearán según la rama)
# from sistema_notas import *

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
    print("=== Sistema de Gestión de Notas ===")
    print("Bienvenido")


if __name__ == "__main__":
    main()
