# 🌟 Técnica 5-4-3-2-1 para Manejar la Ansiedad

## ¿Qué es este programa?
Este es un programa interactivo en Python diseñado para ayudar a personas que experimentan ansiedad o ataques de pánico. Implementa la **técica grounding 5-4-3-2-1**, una herramienta de mindfulness que te ayuda a conectar con el presente usando tus cinco sentidos.

## 🧠 ¿Cómo funciona la técnica?
La técnica consiste en identificar:
- **5** cosas que puedes **VER** 👀
- **4** cosas que puedes **TOCAR** ✋  
- **3** cosas que puedes **OÍR** 👂
- **2** cosas que puedes **OLER** 👃
- **1** cosa que puedes **SABOREAR** 👅

## 🛠️ ¿Cómo se construyó este programa?

### Tecnologías utilizadas
- **Python 3.x** - Lenguaje de programación
- **Listas mutables** - Para almacenar las respuestas del usuario
- **Bucles For** - Para repetir las preguntas
- **Condicionales If** - Para mensajes motivacionales
- **Input/Output** - Para interactuar con el usuario

### Conceptos de programación aplicados
```python
# Listas mutables (pueden cambiar)
cosas_ver = []  # Se puede modificar después de creada

# Bucles for con range()
for i in range(5):  # Se repite 5 veces
    cosa = input(f"{i+1}. Nombra algo: ")
    cosas_ver.append(cosa)  # Añade a la lista

# Condicionales para mensajes motivacionales
if i == 2:
    print("¡Vas muy bien! Sigue respirando...")

# Join para unir listas en texto
print(f"Cosas que ves: {', '.join(cosas_ver)}")

🚀 ¿Cómo ejecutar el programa?
Prerrequisitos
Tener Python instalado (puedes descargarlo de python.org)

Pasos para ejecutar:
Abre la terminal en VS Code

Navega a la carpeta del proyecto:

cd "D:\Python\Phyton course\ProgramaAnsiedad"
Ejecuta el programa:

python Programa_ansiedad.py
⚙️ Instalación y configuración
Verifica que tienes Python instalado:

python --version
# Debe mostrar: Python 3.x.x
Si no tienes Python:

Ve a python.org/downloads

Descarga la última versión

Instálalo marcando "Add Python to PATH"

📋 Características del programa
✅ Interfaz amigable con emojis

✅ Mensajes motivacionales personalizados

✅ Validación de entradas de usuario

✅ Resumen final con todas las respuestas

✅ Posibilidad de añadir más elementos al final

✅ Diseñado para ser calmante y no abrumador

🎯 ¿Para quién es este programa?
Personas que experimentan ansiedad

Quienes quieren aprender técnicas de mindfulness

Estudiantes de programación que buscan proyectos prácticos

Terapeutas que quieren herramientas digitales

🔧 Personalización
Puedes modificar los mensajes motivacionales editando las variables de texto en el código. Los mensajes están diseñados para ser positivos y alentadores.

📊 Estructura del código
El programa sigue este flujo:

Presentación - Mensaje de bienvenida

Recolección de datos - 5-4-3-2-1 sentidos

Mensajes motivacionales - Apoyo durante el ejercicio

Resumen final - Muestra todo lo recolectado

Modo extendido - Permite añadir más elementos

🤝 Contribuir
Si quieres mejorar este programa:

Haz fork del proyecto

Crea una rama para tu feature

Haz commit de tus cambios

Push a la rama

Abre un Pull Request

📄 Licencia
Este proyecto es de código abierto y está disponible para cualquiera que necesite ayuda con la ansiedad.

💖 Agradecimientos
A todas las personas que bravamente enfrentan la ansiedad cada día. Este programa fue creado con mucho cariño para ti.

Recuerda: La ansiedad es temporal, pero tu fuerza es permanente. 💫