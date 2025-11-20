# -*- coding: utf-8 -*-
"""
launcher.py - Selector de interfaz (GUI o Web)
Permite elegir entre la interfaz gráfica o la web de Django
"""

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
import os

BG_COLOR = "#1e1e2e"
PRIMARY_COLOR = "#00ff88"
SECONDARY_COLOR = "#ff006e"
TEXT_COLOR = "#f0f0f0"
ACCENT_COLOR = "#00d9ff"


class LauncherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lengua de Señas - Selector de Interfaz")
        self.geometry("700x500")
        self.configure(bg=BG_COLOR)
        self.create_widgets()

    def create_widgets(self):
        """Crea la interfaz del launcher"""
        frame = tk.Frame(self, bg=BG_COLOR)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Header.TLabel', background=BG_COLOR,
                        foreground=PRIMARY_COLOR, font=('Arial', 24, 'bold'))
        style.configure('Normal.TLabel', background=BG_COLOR,
                        foreground=TEXT_COLOR, font=('Arial', 11))

        title = ttk.Label(frame, text="LENGUA DE SEÑAS",
                          style='Header.TLabel')
        title.pack(pady=(0, 10))

        subtitle = ttk.Label(frame, text="Elige una interfaz",
                             style='Normal.TLabel', font=('Arial', 14))
        subtitle.pack(pady=(0, 30))

        # Opción GUI
        gui_frame = tk.Frame(frame, bg=SECONDARY_COLOR,
                             highlightthickness=2,
                             highlightbackground=ACCENT_COLOR)
        gui_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        gui_title = tk.Label(gui_frame, text="INTERFAZ DE ESCRITORIO",
                             bg=SECONDARY_COLOR, fg="white",
                             font=('Arial', 14, 'bold'), pady=10)
        gui_title.pack(fill=tk.X)

        gui_info = tk.Label(gui_frame, text=(
            "• Interfaz gráfica moderna\n"
            "• Captura, entrenamiento y predicción\n"
            "• Sin necesidad de navegador"),
                            bg=SECONDARY_COLOR, fg=TEXT_COLOR,
                            font=('Arial', 11), justify=tk.LEFT, padx=15, pady=10)
        gui_info.pack(fill=tk.BOTH, expand=True)

        gui_btn = tk.Button(gui_frame, text="ABRIR GUI",
                            bg=PRIMARY_COLOR, fg="black",
                            font=('Arial', 12, 'bold'),
                            command=self.launch_gui,
                            cursor="hand2", padx=20, pady=10)
        gui_btn.pack(pady=10)

        # Opción Web
        web_frame = tk.Frame(frame, bg=SECONDARY_COLOR,
                             highlightthickness=2,
                             highlightbackground=ACCENT_COLOR)
        web_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        web_title = tk.Label(web_frame, text="INTERFAZ WEB",
                             bg=SECONDARY_COLOR, fg="white",
                             font=('Arial', 14, 'bold'), pady=10)
        web_title.pack(fill=tk.X)

        web_info = tk.Label(web_frame, text=(
            "• Interfaz web en el navegador\n"
            "• Acceso desde cualquier dispositivo\n"
            "• Gestión de usuarios y datos"),
                            bg=SECONDARY_COLOR, fg=TEXT_COLOR,
                            font=('Arial', 11), justify=tk.LEFT, padx=15, pady=10)
        web_info.pack(fill=tk.BOTH, expand=True)

        web_btn = tk.Button(web_frame, text="ABRIR WEB",
                            bg=PRIMARY_COLOR, fg="black",
                            font=('Arial', 12, 'bold'),
                            command=self.launch_web,
                            cursor="hand2", padx=20, pady=10)
        web_btn.pack(pady=10)

    def launch_gui(self):
        """Inicia la interfaz gráfica"""
        self.destroy()
        import gui_app
        app = gui_app.SignLanguageApp()
        app.mainloop()

    def launch_web(self):
        """Inicia la interfaz web Flask del proyecto ML"""
        self.destroy()
        try:
            import webbrowser
            import time
            
            # Iniciar Flask app del proyecto ML
            env = os.environ.copy()
            env['PYTHONIOENCODING'] = 'utf-8'
            subprocess.Popen(
                [sys.executable, "web_app/app.py"],
                cwd=os.path.dirname(os.path.abspath(__file__)),
                env=env
            )
            time.sleep(2)
            webbrowser.open("http://127.0.0.1:5000")
        except Exception as e:
            messagebox.showerror("Error", f"Error al iniciar web:\n{e}")


def main():
    app = LauncherApp()
    app.mainloop()


if __name__ == "__main__":
    main()
