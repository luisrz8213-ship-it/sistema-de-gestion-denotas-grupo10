## Cambios Recientes

### v1.0.0 - Release Inicial

**Funcionalidades Implementadas:**

1. **Módulo de Registro** (feature/registro)
   - Registrar estudiantes con validación de ID y nombre
   - Listado de estudiantes registrados

2. **Módulo de Notas** (feature/notas)
   - Ingresar notas por asignatura (0-5)
   - Validación de datos
   - Visualización de notas por estudiante

3. **Módulo de Promedios** (feature/promedio)
   - Cálculo de promedio individual
   - Determinación de estado (Aprobado/Reprobado)
   - Promedio general del grupo

4. **Módulo de Reportes** (feature/reporte)
   - Reporte detallado por estudiante
   - Reporte general con tabla formateada
   - Exportación de reportes a texto

5. **Módulo de Archivos** (feature/archivo)
   - Persistencia en JSON
   - Exportación a CSV
   - Estadísticas del sistema

**Commits por Rama:**
- feature/registro: 2 commits
- feature/notas: 1 commit
- feature/promedio: 1 commit  
- feature/reporte: 1 commit
- feature/archivo: 1 commit
- main: 4 commits (inicial + 3 integraciones)

**Total: 13 commits**

**Pull Requests Mergeados:**
- PR #1: feature/registro → main ✓
- PR #2: feature/archivo → main ✓

**Archivos Principales:**
- `main.py` - Interfaz de usuario
- `sistema_notas.py` - Gestión de estudiantes
- `notas.py` - Gestión de calificaciones
- `promedio.py` - Cálculos estadísticos
- `reporte.py` - Generación de reportes
- `archivo.py` - Persistencia de datos
- `.gitignore` - Archivos ignorados
- `requirements.txt` - Dependencias
- `README.md` - Documentación
- `CHANGES.md` - Este archivo
