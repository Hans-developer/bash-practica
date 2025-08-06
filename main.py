import streamlit as st

# Diccionario de comandos de Linux
comandos_linux = {
    "ls": {
        "descripcion": "Lista los archivos y directorios en el directorio actual.",
        "uso": [
            "ls",
            "ls -l  # Muestra detalles en formato largo",
            "ls -a  # Muestra archivos ocultos"
        ]
    },
    "cd": {
        "descripcion": "Cambia el directorio actual a otro directorio.",
        "uso": [
            "cd nombre_del_directorio  # Cambia al directorio especificado",
            "cd ..                     # Regresa al directorio padre",
            "cd ~                      # Cambia al directorio home del usuario"
        ]
    },
    "pwd": {
        "descripcion": "Muestra el directorio de trabajo actual.",
        "uso": [
            "pwd"
        ]
    },
    "mkdir": {
        "descripcion": "Crea un nuevo directorio.",
        "uso": [
            "mkdir nombre_del_directorio"
        ]
    },
    "rmdir": {
        "descripcion": "Elimina un directorio vacío.",
        "uso": [
            "rmdir nombre_del_directorio"
        ]
    },
    "rm": {
        "descripcion": "Elimina archivos o directorios.",
        "uso": [
            "rm nombre_del_archivo           # Elimina un archivo",
            "rm -r nombre_del_directorio      # Elimina un directorio y su contenido"
        ]
    },
    "cp": {
        "descripcion": "Copia archivos o directorios.",
        "uso": [
            "cp archivo_origen archivo_destino  # Copia un archivo",
            "cp -r directorio_origen directorio_destino  # Copia un directorio"
        ]
    },
    "mv": {
        "descripcion": "Mueve o renombra archivos o directorios.",
        "uso": [
            "mv archivo_origen archivo_destino  # Renombra o mueve un archivo",
            "mv directorio_origen directorio_destino  # Mueve un directorio"
        ]
    },
    "touch": {
        "descripcion": "Crea un archivo vacío o actualiza la fecha de acceso de un archivo.",
        "uso": [
            "touch nombre_del_archivo"
        ]
    },
    "echo": {
        "descripcion": "Muestra una línea de texto o variable en la salida estándar.",
        "uso": [
            "echo 'Hola, mundo'",
            "echo $VARIABLE  # Muestra el valor de una variable"
        ]
    },
    "cat": {
        "descripcion": "Concatena y muestra el contenido de archivos.",
        "uso": [
            "cat nombre_del_archivo",
            "cat archivo1 archivo2  # Muestra el contenido de varios archivos"
        ]
    },
    "man": {
        "descripcion": "Muestra el manual de un comando.",
        "uso": [
            "man nombre_del_comando"
        ]
    },
    "grep": {
        "descripcion": "Busca patrones en el texto.",
        "uso": [
            "grep 'texto_a_buscar' nombre_del_archivo",
            "grep -r 'texto_a_buscar' directorio  # Busca recursivamente en un directorio"
        ]
    },
    "find": {
        "descripcion": "Busca archivos y directorios en una jerarquía de directorios.",
        "uso": [
            "find /ruta/a/buscar -name 'nombre_del_archivo'"
        ]
    },
    "chmod": {
        "descripcion": "Cambia los permisos de acceso de archivos o directorios.",
        "uso": [
            "chmod 755 nombre_del_archivo  # Cambia los permisos a rwxr-xr-x"
        ]
    },
    "chown": {
        "descripcion": "Cambia el propietario y grupo de archivos o directorios.",
        "uso": [
            "chown nuevo_propietario:nuevo_grupo nombre_del_archivo"
        ]
    },
    "ps": {
        "descripcion": "Muestra información sobre los procesos en ejecución.",
        "uso": [
            "ps",
            "ps aux  # Muestra todos los procesos en detalle"
        ]
    },
    "kill": {
        "descripcion": "Envía una señal a un proceso, comúnmente para terminarlo.",
        "uso": [
            "kill PID  # Reemplaza PID con el ID del proceso",
            "kill -9 PID  # Fuerza la terminación del proceso"
        ]
    },
    "top": {
        "descripcion": "Muestra información en tiempo real sobre los procesos del sistema.",
        "uso": [
            "top"
        ]
    },
    "df": {
        "descripcion": "Muestra información sobre el espacio en disco utilizado y disponible.",
        "uso": [
            "df -h  # Muestra el uso del disco en un formato legible"
        ]
    },
    "du": {
        "descripcion": "Muestra el uso del espacio en disco de archivos y directorios.",
        "uso": [
            "du -h nombre_del_directorio  # Muestra el tamaño del directorio",
            "du -sh *  # Muestra el tamaño de cada archivo y directorio en el directorio actual"
        ]
    }
}

# Título de la aplicación
st.title("Buscador de Comandos de Linux")

# Campo de entrada para buscar el comando
comando_buscado = st.text_input("Ingresa un comando de Linux:")

# Buscar el comando en el diccionario
if comando_buscado:
    if comando_buscado in comandos_linux:
        st.subheader(f"Comando: {comando_buscado}")
        st.write("**Descripción:**")
        st.write(comandos_linux[comando_buscado]["descripcion"])
        st.write("**Ejemplos de uso:**")
        for ejemplo in comandos_linux[comando_buscado]["uso"]:
            st.write(f"- {ejemplo}")
    else:
        st.write("Comando no encontrado. Intenta con otro comando.")
