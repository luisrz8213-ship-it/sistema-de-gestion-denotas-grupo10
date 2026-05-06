"""
Módulo de Reportes
Funcionalidades para generar reportes formateados de estudiantes y notas
"""

from typing import List, Tuple


def generar_reporte_estudiante(sistema_notas, id_estudiante: str) -> str:
    """Genera un reporte detallado de un estudiante"""
    if id_estudiante not in sistema_notas.estudiantes:
        return f"❌ El estudiante con ID {id_estudiante} no existe"
    
    est = sistema_notas.estudiantes[id_estudiante]
    
    reporte = f"\n{'='*50}\n"
    reporte += f"  REPORTE ACADÉMICO\n"
    reporte += f"  {'='*50}\n"
    reporte += f"  Nombre: {est['nombre']}\n"
    reporte += f"  ID: {id_estudiante}\n"
    reporte += f"  {'='*50}\n\n"
    
    if est['notas']:
        reporte += f"  NOTAS POR ASIGNATURA:\n"
        reporte += f"  {'-'*48}\n"
        for asig, nota in est['notas'].items():
            reporte += f"  {asig:<35} {nota:>5.1f}\n"
        reporte += f"  {'-'*48}\n"
        reporte += f"  Promedio: {est['promedio']:>32.2f}\n"
        reporte += f"  Estado: {est['estado']:>35}\n"
    else:
        reporte += f"  ⚠️  Sin notas registradas\n"
    
    reporte += f"  {'='*50}\n\n"
    return reporte


def generar_reporte_general(sistema_notas) -> str:
    """Genera un reporte general de todos los estudiantes"""
    if not sistema_notas.estudiantes:
        return "❌ No hay estudiantes registrados"
    
    reporte = f"\n{'='*60}\n"
    reporte += f"  REPORTE GENERAL DEL SISTEMA\n"
    reporte += f"  {'='*60}\n\n"
    
    reporte += f"  {'ID':<12} {'NOMBRE':<25} {'PROMEDIO':<12} {'ESTADO':<12}\n"
    reporte += f"  {'-'*60}\n"
    
    for id_est, est in sistema_notas.estudiantes.items():
        promedio_str = f"{est['promedio']:.2f}" if est['promedio'] > 0 else "N/A"
        estado_str = est['estado'] if est['estado'] != 'pendiente' else "Pendiente"
        
        reporte += f"  {id_est:<12} {est['nombre']:<25} {promedio_str:<12} {estado_str:<12}\n"
    
    reporte += f"  {'-'*60}\n"
    
    # Calcular promedio general
    promedios = [est['promedio'] for est in sistema_notas.estudiantes.values() if est['promedio'] > 0]
    if promedios:
        promedio_general = sum(promedios) / len(promedios)
        reporte += f"  Promedio General del Grupo: {promedio_general:.2f}\n"
    
    total_estudiantes = len(sistema_notas.estudiantes)
    reprobados = sum(1 for est in sistema_notas.estudiantes.values() if "Reprobado" in est['estado'])
    aprobados = sum(1 for est in sistema_notas.estudiantes.values() if "Aprobado" in est['estado'])
    
    reporte += f"  Total de Estudiantes: {total_estudiantes}\n"
    reporte += f"  Aprobados: {aprobados}  |  Reprobados: {reprobados}\n"
    
    reporte += f"  {'='*60}\n\n"
    return reporte


def exportar_reporte_texto(sistema_notas, archivo: str = "reporte.txt") -> Tuple[bool, str]:
    """Exporta el reporte general a un archivo de texto"""
    try:
        reporte = generar_reporte_general(sistema_notas)
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(reporte)
        return True, f"✓ Reporte exportado a {archivo}"
    except Exception as e:
        return False, f"❌ Error al exportar reporte: {str(e)}"
"""
Módulo de Reportes
Funcionalidades para generar reportes formateados de estudiantes y notas
"""

from typing import List, Tuple


def generar_reporte_estudiante(sistema_notas, id_estudiante: str) -> str:
    \"\"\"Genera un reporte detallado de un estudiante\"\"\"
    if id_estudiante not in sistema_notas.estudiantes:
        return f\"❌ El estudiante con ID {id_estudiante} no existe\"
    
    est = sistema_notas.estudiantes[id_estudiante]
    
    reporte = f\"\\n{'='*50}\\n\"
    reporte += f\"  REPORTE ACADÉMICO\\n\"
    reporte += f\"  {'='*50}\\n\"
    reporte += f\"  Nombre: {est['nombre']}\\n\"
    reporte += f\"  ID: {id_estudiante}\\n\"
    reporte += f\"  {'='*50}\\n\\n\"
    
    if est['notas']:
        reporte += f\"  NOTAS POR ASIGNATURA:\\n\"
        reporte += f\"  {'-'*48}\\n\"
        for asig, nota in est['notas'].items():
            reporte += f\"  {asig:<35} {nota:>5.1f}\\n\"
        reporte += f\"  {'-'*48}\\n\"
        reporte += f\"  Promedio: {est['promedio']:>32.2f}\\n\"
        reporte += f\"  Estado: {est['estado']:>35}\\n\"
    else:
        reporte += f\"  ⚠️  Sin notas registradas\\n\"
    
    reporte += f\"  {'='*50}\\n\\n\"
    return reporte


def generar_reporte_general(sistema_notas) -> str:
    \"\"\"Genera un reporte general de todos los estudiantes\"\"\"
    if not sistema_notas.estudiantes:
        return \"❌ No hay estudiantes registrados\"
    
    reporte = f\"\\n{'='*60}\\n\"
    reporte += f\"  REPORTE GENERAL DEL SISTEMA\\n\"
    reporte += f\"  {'='*60}\\n\\n\"
    
    reporte += f\"  {'ID':<12} {'NOMBRE':<25} {'PROMEDIO':<12} {'ESTADO':<12}\\n\"
    reporte += f\"  {'-'*60}\\n\"
    
    for id_est, est in sistema_notas.estudiantes.items():
        promedio_str = f\"{est['promedio']:.2f}\" if est['promedio'] > 0 else \"N/A\"
        estado_str = est['estado'] if est['estado'] != 'pendiente' else \"Pendiente\"
        
        reporte += f\"  {id_est:<12} {est['nombre']:<25} {promedio_str:<12} {estado_str:<12}\\n\"
    
    reporte += f\"  {'-'*60}\\n\"
    
    # Calcular promedio general
    promedios = [est['promedio'] for est in sistema_notas.estudiantes.values() if est['promedio'] > 0]
    if promedios:
        promedio_general = sum(promedios) / len(promedios)
        reporte += f\"  Promedio General del Grupo: {promedio_general:.2f}\\n\"
    
    total_estudiantes = len(sistema_notas.estudiantes)
    reprobados = sum(1 for est in sistema_notas.estudiantes.values() if \"Reprobado\" in est['estado'])
    aprobados = sum(1 for est in sistema_notas.estudiantes.values() if \"Aprobado\" in est['estado'])
    
    reporte += f\"  Total de Estudiantes: {total_estudiantes}\\n\"
    reporte += f\"  Aprobados: {aprobados}  |  Reprobados: {reprobados}\\n\"
    
    reporte += f\"  {'='*60}\\n\\n\"
    return reporte


def exportar_reporte_texto(sistema_notas, archivo: str = \"reporte.txt\") -> Tuple[bool, str]:
    \"\"\"Exporta el reporte general a un archivo de texto\"\"\"
    try:
        reporte = generar_reporte_general(sistema_notas)
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(reporte)
        return True, f\"✓ Reporte exportado a {archivo}\"
    except Exception as e:
        return False, f\"❌ Error al exportar reporte: {str(e)}\"


from typing import Tuple
