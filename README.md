🚀 Sistema de Reconocimiento Facial UTPL - IA
Este proyecto implementa una solución avanzada de visión por computadora para la identificación de estudiantes, desarrollada para la materia de Fundamentos de Inteligencia Artificial. El sistema utiliza DeepFace para la extracción de rasgos faciales y MongoDB para la gestión dinámica de datos y descripciones personalizadas.

📋 Guía de Instalación y Uso
Sigue estos pasos para configurar el proyecto en tu máquina local.

1. Clonar el repositorio
Primero, descarga el código desde GitHub:

Bash

git clone https://github.com/TU_USUARIO/Funda.IA.git
cd Funda.IA
2. Entrar al Entorno Virtual (VENV)
Es obligatorio activar el entorno virtual para que las librerías funcionen correctamente. Ejecuta el comando según tu terminal:

Si usas PowerShell (VS Code):

PowerShell

.\venv\Scripts\Activate.ps1
Si usas Símbolo del Sistema (CMD):

DOS

venv\Scripts\activate
3. Instalar las dependencias (PIP)
Una vez que veas el prefijo (venv) en tu terminal, instala las librerías necesarias:

Bash

pip install deepface tf-keras opencv-python pymongo
🚀 Ejecución del Proyecto
Sincronizar la Base de Datos: Ejecuta este script para cargar las fotos de la carpeta /fotos y los datos del jsons.json hacia MongoDB:

Bash

python registrar_caras.py
Iniciar la Cámara: Lanza el reconocimiento en tiempo real:

Bash

python reconocer_camara.py
Nota: Presiona la tecla ESC para cerrar la cámara y finalizar el programa.

🛠️ Detalles Técnicos
Modelo de IA: Utiliza FaceNet para generar embeddings de 128 dimensiones.

Base de Datos: MongoDB almacena el nombre, código UTPL y descripciones personalizadas (ej. "Muy Cruceta", "Príncipe de la sirenita").

Detección: Se utiliza el backend de OpenCV para optimizar la velocidad de procesamiento en video en vivo.

📂 Estructura del Git
Para mantener el repositorio limpio, el archivo .gitignore está configurado para excluir las carpetas de los entornos virtuales (venv/).

Comandos útiles de Git:

git status: Ver archivos modificados.

git add .: Preparar cambios para subir.

git commit -m "Descripción del cambio": Guardar avance local.

git push origin main: Subir cambios a la nube.
