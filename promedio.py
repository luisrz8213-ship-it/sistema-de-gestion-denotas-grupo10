"""
Módulo de Cálculo de Promedios
Funcionalidades para calcular promedios y estados de estudiantes
"""

from typing import Tuple


def calcular_promedio(notas: dict) -> float:
    """
    Calcula el promedio de un estudiante
    
    Args:
        notas: Diccionario con asignaturas y notas
    
    Returns:
        Promedio calculado (0.0 si no hay notas)
    """
    if not notas:
        return 0.0
    
    return round(sum(notas.values()) / len(notas), 2)


def determinar_estado(promedio: float) -> str:
    """
    Determina el estado del estudiante basado en el promedio
    
    Args:
        promedio: Promedio del estudiante
    
    Returns:
        Estado: 'Aprobado' si >= 3.0, 'Reprobado' si < 3.0
    """
    return "✓ Aprobado" if promedio >= 3.0 else "✗ Reprobado"


def obtener_promedio_estudiante(sistema_notas, id_estudiante: str) -> Tuple[bool, str]:
    """
    Obtiene el promedio y estado de un estudiante
    
    Args:
        sistema_notas: Instancia del sistema
        id_estudiante: ID del estudiante
    
    Returns:
        Tupla (éxito, mensaje)
    """
    if id_estudiante not in sistema_notas.estudiantes:
        return False, f"❌ El estudiante con ID {id_estudiante} no existe"
    
    estudiante = sistema_notas.estudiantes[id_estudiante]
    promedio = calcular_promedio(estudiante["notas"])
    estado = determinar_estado(promedio)
    
    # Actualizar en el sistema
    sistema_notas.estudiantes[id_estudiante]["promedio"] = promedio
    sistema_notas.estudiantes[id_estudiante]["estado"] = estado
    sistema_notas.guardar_datos()
    
    mensaje = f"\n📊 PROMEDIO DE {estudiante['nombre'].upper()}\n"
    mensaje += f"  Promedio: {promedio}\n"
    mensaje += f"  Estado: {estado}\n"
    
    return True, mensaje


def calcular_promedio_general(sistema_notas) -> float:
    """Calcula el promedio general de todos los estudiantes"""
    if not sistema_notas.estudiantes:
        return 0.0
    
    promedios = [
        calcular_promedio(est["notas"]) 
        for est in sistema_notas.estudiantes.values()
    ]
    
    return round(sum(promedios) / len(promedios), 2) if promedios else 0.0
