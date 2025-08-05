import streamlit as st

# Diccionario con las descripciones de los comandos
COMMAND_DESCRIPTIONS = {
    "ls": "Lista el contenido de un directorio.",
    "cd": "Cambia de directorio.",
    "mkdir": "Crea un nuevo directorio.",
    "rm": "Elimina archivos o directorios.",
    "mv": "Mueve o renombra archivos y directorios.",
    "cp": "Copia archivos y directorios.",
    "pwd": "Muestra el directorio de trabajo actual.",
    "cat": "Muestra el contenido de un archivo.",
    "echo": "Imprime texto en la terminal.",
    "grep": "Busca patrones de texto en archivos.",
    "find": "Busca archivos y directorios.",
    "chmod": "Cambia los permisos de un archivo o directorio.",
    "sudo": "Ejecuta un comando con permisos de superusuario.",
    "top": "Muestra información sobre los procesos en ejecución.",
    "ps": "Muestra información sobre los procesos en ejecución.",
    "kill": "Termina un proceso en ejecución.",
    "clear": "Limpia la pantalla de la terminal.",
    "history": "Muestra el historial de comandos ejecutados.",
    "man": "Muestra la página de manual de un comando.",
    "exit": "Cierra la sesión de la terminal."
}

def get_command_description(command):
    if command in COMMAND_DESCRIPTIONS:
        return COMMAND_DESCRIPTIONS[command]
    else:
        return f"El comando '{command}' no existe o no tiene una descripción disponible."

def main():
    st.title("Aprende Bash")

    while True:
        # Obtener la entrada del usuario
        user_input = st.text_input("Escribe un comando de Bash:", value="", key="user_input")

        # Procesar la entrada del usuario
        if st.button("Enviar"):
            try:
                # Dividir el comando y los argumentos
                command_parts = shlex.split(user_input)
                command = command_parts[0]

                # Obtener la descripción del comando
                command_description = get_command_description(command)

                # Mostrar la descripción del comando
                st.write(f"**Comando:** {command}")
                st.write(f"**Descripción:** {command_description}")

            except Exception as e:
                # Mostrar el error
                st.write(f"**Error:** {e}")

        # Agregar la opción de guardar el historial del chat
        if st.button("Guardar historial"):
            with open("command_history.txt", "w") as f:
                f.write(f"Historial de comandos:\n\n")
                for command, description in COMMAND_DESCRIPTIONS.items():
                    f.write(f"Comando: {command}\nDescripción: {description}\n\n")
            st.success("Historial de comandos guardado en command_history.txt")

if __name__ == "__main__":
    main()
