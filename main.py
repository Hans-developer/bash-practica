import streamlit as st

# Diccionario de comandos de Bash y sus descripciones
bash_commands = {
    "ls": "Lista los archivos y directorios en el directorio actual.",
    "cd": "Cambia el directorio actual a otro directorio.",
    "pwd": "Muestra el directorio de trabajo actual.",
    "mkdir": "Crea un nuevo directorio.",
    "rmdir": "Elimina un directorio vacío.",
    "rm": "Elimina archivos o directorios.",
    "cp": "Copia archivos o directorios.",
    "mv": "Mueve o renombra archivos o directorios.",
    "touch": "Crea un archivo vacío o actualiza la fecha de acceso de un archivo.",
    "echo": "Muestra una línea de texto o variable en la salida estándar.",
    "cat": "Concatena y muestra el contenido de archivos.",
    "man": "Muestra el manual de un comando.",
    "grep": "Busca patrones en el texto.",
    "find": "Busca archivos y directorios en una jerarquía de directorios.",
    "chmod": "Cambia los permisos de acceso de archivos o directorios.",
    "chown": "Cambia el propietario y grupo de archivos o directorios.",
    "ps": "Muestra información sobre los procesos en ejecución.",
    "kill": "Envía una señal a un proceso, comúnmente para terminarlo.",
    "top": "Muestra información en tiempo real sobre los procesos del sistema.",
    "df": "Muestra información sobre el espacio en disco utilizado y disponible.",
    "du": "Muestra el uso del espacio en disco de archivos y directorios.",
    # Agrega más comandos según sea necesario
}

# Título de la aplicación
st.title("Práctica de Bash Scripting")

# Entrada de texto para el comando
command = st.text_input("Ingresa un comando de Bash:")

# Mostrar la descripción del comando
if command:
    description = bash_commands.get(command.strip(), "Comando no encontrado. Intenta con otro.")
    st.write(description)
