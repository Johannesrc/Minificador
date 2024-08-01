import os
import re
import shutil
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

import csscompressor
import htmlmin
from jsmin import jsmin

# Lista de extensiones compatibles
EXTENSIONES_COMPATIBLES = ['.html', '.css', '.js', '.php']


def minify_html(content):
    """
    Minifica contenido HTML, incluyendo scripts JavaScript embebidos.
    """
    minified_html = htmlmin.minify(content)
    return re.sub(r'<script>(.*?)</script>', lambda m: f'<script>{jsmin(m.group(1))}</script>', minified_html, flags=re.DOTALL)


def minify_php(content):
    """
    Minifica el contenido de un archivo PHP, manejando HTML y JavaScript embebido.
    """
    parts = re.split(r'(<\?php|\?>)', content)
    minified_parts = []
    in_php_block = False

    for part in parts:
        if part == '<?php':
            in_php_block = True
            minified_parts.append(part)
        elif part == '?>':
            in_php_block = False
            minified_parts.append(part)
        else:
            if in_php_block:
                minified_parts.append(minify_php_code(part))
            else:
                minified_parts.append(minify_html(part))

    return "".join(minified_parts)


def minify_php_code(code):
    """
    Minifica el código PHP.
    """
    lines = code.splitlines()
    minified_lines = []
    in_comment = False

    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith("/*"):
            in_comment = True
        if not in_comment and not stripped_line.startswith("//"):
            minified_lines.append(stripped_line)
        if stripped_line.endswith("*/"):
            in_comment = False

    return " ".join(minified_lines)


def minify_file(file_path):
    """
    Minifica el contenido de un archivo según su extensión.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        ext = os.path.splitext(file_path)[1]

        if ext == '.html':
            return minify_html(content)
        elif ext == '.css':
            return csscompressor.compress(content)
        elif ext == '.js':
            return jsmin(content)
        elif ext == '.php':
            return minify_php(content)

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error al acceder al archivo {file_path}: {e}")
    except Exception as e:
        print(f"Error al minificar el archivo {file_path}: {e}")

    return None


def save_minified_file(dest_path, minified_content):
    """
    Guarda el contenido minificado en la ruta de destino.
    """
    try:
        dest_dir = os.path.dirname(dest_path)
        os.makedirs(dest_dir, exist_ok=True)
        with open(dest_path, 'w', encoding='utf-8') as file:
            file.write(minified_content)
    except Exception as e:
        print(f"Error al guardar el archivo minificado en {dest_path}: {e}")


def minify_project(src_dir, dest_dir):
    """
    Minifica todos los archivos compatibles en un proyecto.
    """
    try:
        if os.path.exists(dest_dir):
            shutil.rmtree(dest_dir)
        shutil.copytree(src_dir, dest_dir)

        for root, _, files in os.walk(dest_dir):
            for file in files:
                file_path = os.path.join(root, file)
                ext = os.path.splitext(file)[1]
                if ext in EXTENSIONES_COMPATIBLES:
                    minified_content = minify_file(file_path)
                    if minified_content:
                        save_minified_file(file_path, minified_content)
    except Exception as e:
        print(f"Error al minificar el proyecto: {e}")


def browse_folder(entry):
    """
    Abre un cuadro de diálogo para seleccionar una carpeta y actualiza la entrada.
    """
    folder_path = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, folder_path)


def validate_paths(src_dir, dest_dir):
    """
    Valida que las rutas de origen y destino sean diferentes y existan.
    """
    if not src_dir or not dest_dir:
        messagebox.showerror("Error", "Debe especificar ambas rutas.")
        return False
    if src_dir == dest_dir:
        messagebox.showerror(
            "Error", "Las rutas de origen y destino no pueden ser las mismas.")
        return False
    if not os.path.exists(src_dir):
        messagebox.showerror(
            "Error", f"La ruta del proyecto origen '{src_dir}' no existe.")
        return False
    return True


def minify_action(entry_src, entry_dest):
    """
    Ejecuta la acción de minificación del proyecto.
    """
    src_dir = entry_src.get()
    dest_dir = entry_dest.get()

    if validate_paths(src_dir, dest_dir):
        minify_project(src_dir, dest_dir)
        messagebox.showinfo("Minificación completa",
                            "El proyecto ha sido minificado.")


def main():
    """
    Función principal para ejecutar la interfaz gráfica de usuario.
    """
    app = tk.Tk()
    app.title("Minificador de Proyecto")

    frame_src = tk.Frame(app)
    frame_src.pack(padx=10, pady=5)

    label_src = tk.Label(frame_src, text="Ruta del proyecto origen:")
    label_src.pack(side=tk.LEFT)

    entry_path_src = tk.Entry(frame_src, width=50)
    entry_path_src.pack(side=tk.LEFT, padx=5)

    btn_browse_src = tk.Button(
        frame_src, text="Buscar", command=lambda: browse_folder(entry_path_src))
    btn_browse_src.pack(side=tk.LEFT)

    frame_dest = tk.Frame(app)
    frame_dest.pack(padx=10, pady=5)

    label_dest = tk.Label(frame_dest, text="Ruta del proyecto destino:")
    label_dest.pack(side=tk.LEFT)

    entry_path_dest = tk.Entry(frame_dest, width=50)
    entry_path_dest.pack(side=tk.LEFT, padx=5)

    btn_browse_dest = tk.Button(
        frame_dest, text="Buscar", command=lambda: browse_folder(entry_path_dest))
    btn_browse_dest.pack(side=tk.LEFT)

    btn_minify = tk.Button(app, text="Minificar", command=lambda: minify_action(
        entry_path_src, entry_path_dest))
    btn_minify.pack(pady=10)

    app.mainloop()
    return 0


if __name__ == '__main__':
    sys.exit(main())
