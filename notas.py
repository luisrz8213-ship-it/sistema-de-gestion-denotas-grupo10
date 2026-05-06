"""
Módulo de Gestión de Notas
Funcionalidades para ingresar y gestionar notas de estudiantes
"""

from typing import Tuple, List


def validar_nota(nota: float) -> bool:
    """Valida que la nota esté entre 0 y 5"""
    try:
        nota_float = float(nota)
        return 0 <= nota_float <= 5
    except ValueError:
        return False


def validar_asignatura(asignatura: str) -> bool:
    """Valida que el nombre de la asignatura no esté vacío"""
    return bool(asignatura.strip())


def ingresar_nota(sistema_notas, id_estudiante: str, asignatura: str, nota: float) -> Tuple[bool, str]:
    """
    Ingresa una nota para un estudiante en una asignatura
    
    Args:
        sistema_notas: Instancia del sistema
        id_estudiante: ID del estudiante
        asignatura: Nombre de la asignatura
        nota: Calificación (0-5)
    
    Returns:
        Tupla (éxito, mensaje)
    """
    if id_estudiante not in sistema_notas.estudiantes:
        return False, f"❌ El estudiante con ID {id_estudiante} no existe"
    
    if not validar_asignatura(asignatura):
        return False, "❌ El nombre de la asignatura no puede estar vacío"
    
    if not validar_nota(nota):
        return False, "❌ La nota debe estar entre 0 y 5"
    
    # Guardar nota
    sistema_notas.estudiantes[id_estudiante]["notas"][asignatura] = float(nota)
    sistema_notas.guardar_datos()
    
    return True, f"✓ Nota {nota} registrada en {asignatura} para {sistema_notas.estudiantes[id_estudiante]['nombre']}"


def obtener_notas(sistema_notas, id_estudiante: str) -> Tuple[bool, str]:
    """Obtiene todas las notas de un estudiante"""
    if id_estudiante not in sistema_notas.estudiantes:
        return False, f"❌ El estudiante con ID {id_estudiante} no existe"
    
    notas = sistema_notas.estudiantes[id_estudiante]["notas"]
    
    if not notas:
        return True, f"📋 {sistema_notas.estudiantes[id_estudiante]['nombre']} no tiene notas registradas"
    
    resultado = f"\n📋 Notas de {sistema_notas.estudiantes[id_estudiante]['nombre']}:\n"
    for asignatura, nota in notas.items():
        resultado += f"  • {asignatura}: {nota}\n"
    
    return True, resultado
