"""
Módulo de Registro de Estudiantes
Funcionalidades para registrar y gestionar estudiantes
"""

import re
from typing import Dict, Tuple


def validar_id_estudiante(id_estudiante: str) -> bool:
    """Valida que el ID del estudiante sea válido (números)"""
    return bool(re.match(r'^\d{6,}$', id_estudiante))


def validar_nombre(nombre: str) -> bool:
    """Valida que el nombre no esté vacío y contenga solo letras y espacios"""
    return bool(nombre.strip()) and all(c.isalpha() or c.isspace() for c in nombre)


def registrar_estudiante(sistema_notas, nombre: str, id_estudiante: str) -> Tuple[bool, str]:
    """
    Registra un nuevo estudiante en el sistema
    
    Args:
        sistema_notas: Instancia del sistema
        nombre: Nombre del estudiante
        id_estudiante: ID único del estudiante
    
    Returns:
        Tupla (éxito, mensaje)
    """
    # Validaciones
    if not validar_nombre(nombre):
        return False, "❌ El nombre debe contener solo letras y espacios"
    
    if not validar_id_estudiante(id_estudiante):
        return False, "❌ El ID debe tener mínimo 6 dígitos"
    
    if id_estudiante in sistema_notas.estudiantes:
        return False, f"❌ El estudiante con ID {id_estudiante} ya está registrado"
    
    # Registrar estudiante
    sistema_notas.estudiantes[id_estudiante] = {
        "nombre": nombre.strip(),
        "notas": {},
        "promedio": 0.0,
        "estado": "pendiente"
    }
    
    sistema_notas.guardar_datos()
    return True, f"✓ Estudiante '{nombre}' registrado con ID {id_estudiante}"


def listar_estudiantes(sistema_notas) -> str:
    """Lista todos los estudiantes registrados"""
    if not sistema_notas.estudiantes:
        return "No hay estudiantes registrados"
    
    resultado = "\n📋 Estudiantes Registrados:\n"
    for id_est, datos in sistema_notas.estudiantes.items():
        resultado += f"  • {datos['nombre']} (ID: {id_est})\n"
    
    return resultado
