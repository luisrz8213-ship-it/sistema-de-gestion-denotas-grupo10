"""
Módulo de Persistencia de Datos
Funcionalidades para guardar y cargar datos en JSON
"""

import json
import os
from typing import Tuple


def guardar_datos_json(sistema_notas, archivo: str = "data.json") -> Tuple[bool, str]:
    """
    Guarda todos los datos a un archivo JSON
    
    Args:
        sistema_notas: Instancia del sistema
        archivo: Ruta del archivo JSON
    
    Returns:
        Tupla (éxito, mensaje)
    """
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(sistema_notas.estudiantes, f, indent=2, ensure_ascii=False)
        return True, f"✓ Datos guardados en {archivo}"
    except Exception as e:
        return False, f"❌ Error al guardar: {str(e)}"


def cargar_datos_json(sistema_notas, archivo: str = "data.json") -> Tuple[bool, str]:
    """
    Carga datos desde un archivo JSON
    
    Args:
        sistema_notas: Instancia del sistema
        archivo: Ruta del archivo JSON
    
    Returns:
        Tupla (éxito, mensaje)
    """
    try:
        if not os.path.exists(archivo):
            return True, f"Archivo {archivo} no existe. Sistema vacío."
        
        with open(archivo, 'r', encoding='utf-8') as f:
            datos = json.load(f)
            sistema_notas.estudiantes = datos
        
        return True, f"✓ Datos cargados desde {archivo}"
    except json.JSONDecodeError:
        return False, f"❌ Archivo JSON corrupto: {archivo}"
    except Exception as e:
        return False, f"❌ Error al cargar: {str(e)}"


def exportar_csv(sistema_notas, archivo: str = "reporte.csv") -> Tuple[bool, str]:
    """
    Exporta datos a formato CSV
    
    Args:
        sistema_notas: Instancia del sistema
        archivo: Ruta del archivo CSV
    
    Returns:
        Tupla (éxito, mensaje)
    """
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            # Header
            f.write("ID,Nombre,Promedio,Estado\n")
            
            # Datos
            for id_est, est in sistema_notas.estudiantes.items():
                nombre = est['nombre']
                promedio = f"{est['promedio']:.2f}" if est['promedio'] > 0 else "N/A"
                estado = est['estado']
                f.write(f"{id_est},{nombre},{promedio},{estado}\n")
        
        return True, f"✓ Datos exportados a {archivo}"
    except Exception as e:
        return False, f"❌ Error al exportar CSV: {str(e)}"


def obtener_estadisticas(sistema_notas) -> dict:
    """
    Calcula estadísticas del sistema
    
    Returns:
        Diccionario con estadísticas
    """
    total = len(sistema_notas.estudiantes)
    con_notas = sum(1 for est in sistema_notas.estudiantes.values() if est['notas'])
    aprobados = sum(1 for est in sistema_notas.estudiantes.values() if "Aprobado" in est['estado'])
    reprobados = sum(1 for est in sistema_notas.estudiantes.values() if "Reprobado" in est['estado'])
    
    promedios = [est['promedio'] for est in sistema_notas.estudiantes.values() if est['promedio'] > 0]
    promedio_general = sum(promedios) / len(promedios) if promedios else 0
    
    return {
        "total_estudiantes": total,
        "estudiantes_con_notas": con_notas,
        "aprobados": aprobados,
        "reprobados": reprobados,
        "promedio_general": round(promedio_general, 2)
    }
