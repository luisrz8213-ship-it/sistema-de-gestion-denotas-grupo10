# Sistema de Gestión de Notas - Grupo 10

## Descripción
Aplicación de consola en Python para gestionar calificaciones estudiantiles. Permite registrar estudiantes, ingresar notas, calcular promedios y generar reportes.

## Funcionalidades
- **Registro**: Registrar estudiantes con nombre e ID
- **Notas**: Ingresar notas por asignatura (0–5)
- **Promedio**: Calcular promedio y estado (aprobado/reprobado)
- **Reporte**: Generar reporte en consola con tabla formateada
- **Archivo**: Guardar y cargar datos en archivo .json

## Instalación

```bash
git clone https://github.com/luisrz8213-ship-it/sistema-de-gestion-denotas-grupo10.git
cd sistema-de-gestion-denotas-grupo10
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Uso

```bash
python3 main.py
```

## Estructura del Proyecto

```
├── main.py              # Archivo principal
├── sistema_notas.py     # Módulo principal
├── data.json            # Datos persistentes
├── requirements.txt     # Dependencias
└── .gitignore
```

## Integrantes del Grupo
- Tech Lead (Configuración, revisión)
- Dev Backend (Funcionalidades core)
- Dev Integración (Reporte y archivo)

## Notas de Desarrollo
- Cada funcionalidad está en su propia rama
- Mínimo 2 Pull Requests mergeados
- Mensajes de commit con formato: `feat:`, `fix:`, `chore:`
