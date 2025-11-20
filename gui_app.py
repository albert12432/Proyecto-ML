# -*- coding: utf-8 -*-
"""
gui_app.py - Interfaz Gráfica para Lengua de Señas
Aplicación visual amigable para capturar, entrenar y predecir señas
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import subprocess
import sys
import os
import time

BG_COLOR = "#1e1e2e"
PRIMARY_COLOR = "#00ff88"
SECONDARY_COLOR = "#ff006e"
TEXT_COLOR = "#f0f0f0"
ACCENT_COLOR = "#00d9ff"
CARD_BG = "#2a2a3e"


class SignLanguageApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lengua de Señas - Reconocimiento en Tiempo Real")
        self.geometry("1100x750")
        self.configure(bg=BG_COLOR)
        self.setup_styles()
        self.create_widgets()
        self.training_process = None

    def setup_styles(self):
        """Configura los estilos de la aplicación"""
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Header.TLabel', background=BG_COLOR,
                        foreground=PRIMARY_COLOR, font=('Arial', 24, 'bold'))
        style.configure('Title.TLabel', background=BG_COLOR,
                        foreground=ACCENT_COLOR, font=('Arial', 14, 'bold'))
        style.configure('Normal.TLabel', background=BG_COLOR,
                        foreground=TEXT_COLOR, font=('Arial', 11))

    def create_widgets(self):
        """Crea la interfaz principal"""
        # Header con botón de volver
        header_frame = tk.Frame(self, bg=BG_COLOR)
        header_frame.pack(fill=tk.X, padx=20, pady=15)

        # Botón volver a selector
        back_btn = tk.Button(header_frame, text="← VOLVER AL SELECTOR",
                            bg=CARD_BG, fg=ACCENT_COLOR,
                            font=('Arial', 10, 'bold'),
                            command=self.back_to_launcher,
                            cursor="hand2", padx=15, pady=8,
                            relief=tk.FLAT)
        back_btn.pack(side=tk.LEFT)

        # Título centrado
        title_frame = tk.Frame(header_frame, bg=BG_COLOR)
        title_frame.pack(expand=True)
        
        title = ttk.Label(title_frame, text="LENGUA DE SEÑAS",
                          style='Header.TLabel')
        title.pack()

        subtitle = ttk.Label(title_frame,
                             text="Reconocimiento de Gestos con IA",
                             style='Title.TLabel')
        subtitle.pack()

        # Frame principal con cards mejoradas
        main_frame = tk.Frame(self, bg=BG_COLOR)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

        self.create_section(main_frame, 0, "CAPTURAR",
                            "Graba nuevas secuencias\nde señas para entrenar",
                            self.show_capture_section)

        self.create_section(main_frame, 1, "ENTRENAR",
                            "Entrena el modelo LSTM\ncon los datos capturados",
                            self.show_train_section)

        self.create_section(main_frame, 2, "PREDECIR",
                            "Reconoce señas en\ntiempo real con la cámara",
                            self.show_predict_section)

        # Footer mejorado
        footer_frame = tk.Frame(self, bg=CARD_BG)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

        footer_text = ttk.Label(footer_frame,
                                text="📁 Datos: data/secuencias/ | "
                                     "🧠 Modelo: models/modelo_lstm.h5",
                                style='Normal.TLabel')
        footer_text.pack(pady=12)

    def create_section(self, parent, column, title, description, command):
        """Crea una sección de botón principal mejorada"""
        btn_frame = tk.Frame(parent, bg=CARD_BG,
                             highlightthickness=3,
                             highlightbackground=ACCENT_COLOR,
                             relief=tk.RAISED, bd=2)
        btn_frame.grid(row=0, column=column, padx=15, pady=15,
                       sticky="nsew", ipadx=15, ipady=15)
        parent.grid_columnconfigure(column, weight=1)
        parent.grid_rowconfigure(0, weight=1)

        # Card interior con gradiente simulado
        inner_frame = tk.Frame(btn_frame, bg=SECONDARY_COLOR)
        inner_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        btn = tk.Button(inner_frame, text=title,
                        font=('Arial', 18, 'bold'),
                        bg=SECONDARY_COLOR, fg="white", border=0,
                        cursor="hand2", relief=tk.FLAT,
                        command=command, activebackground=PRIMARY_COLOR,
                        activeforeground="black")
        btn.pack(fill=tk.BOTH, expand=True, padx=25, pady=25)

        desc = tk.Label(btn_frame, text=description,
                        bg=CARD_BG, fg=TEXT_COLOR,
                        font=('Arial', 10), justify=tk.CENTER)
        desc.pack(pady=(0, 15))

    def show_capture_section(self):
        """Muestra la sección de captura"""
        self.show_section(
            "CAPTURAR SECUENCIAS",
            [("Nombre de la seña:", self.create_capture_input),
             (None, self.create_capture_buttons)]
        )

    def create_capture_input(self, frame):
        """Crea el input de nombre para captura"""
        ttk.Label(frame, text="Ingresa el nombre de la seña",
                  style='Normal.TLabel').pack(anchor=tk.W, pady=(0, 10))
        self.capture_input = tk.Entry(frame, font=('Arial', 12), width=30)
        self.capture_input.pack(anchor=tk.W, pady=(0, 20))

    def create_capture_buttons(self, frame):
        """Crea los botones de captura"""
        btn_frame = tk.Frame(frame, bg=BG_COLOR)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="INICIAR CAPTURA",
                  bg=PRIMARY_COLOR, fg="black",
                  font=('Arial', 12, 'bold'),
                  command=self.start_capture,
                  cursor="hand2", padx=20, pady=10).pack(side=tk.LEFT, padx=10)

        tk.Button(btn_frame, text="VOLVER",
                  bg=ACCENT_COLOR, fg="black",
                  font=('Arial', 11, 'bold'),
                  command=self.show_main,
                  cursor="hand2", padx=15, pady=10).pack(side=tk.LEFT, padx=10)

    def show_train_section(self):
        """Muestra la sección de entrenamiento"""
        self.show_section(
            "ENTRENAR MODELO",
            [(None, self.create_train_widgets)]
        )

    def create_train_widgets(self, frame):
        """Crea los widgets de entrenamiento mejorados"""
        info = ("El modelo LSTM aprenderá de las secuencias.\n"
                "Esto puede tardar varios minutos.\n\n"
                "Características:\n"
                "• Aumento de datos\n"
                "• Arquitectura profunda (128→64→32)\n"
                "• Validación automática")

        info_label = tk.Label(frame, text=info, bg=BG_COLOR, fg=TEXT_COLOR,
                              font=('Arial', 11), justify=tk.LEFT)
        info_label.pack(anchor=tk.W, pady=20)

        # Frame para progreso
        progress_frame = tk.Frame(frame, bg=CARD_BG, relief=tk.SUNKEN, bd=2)
        progress_frame.pack(fill=tk.BOTH, expand=True, pady=20)

        # Etiqueta de estado
        self.train_status = tk.Label(progress_frame,
                                     text="Listo para entrenar",
                                     bg=CARD_BG, fg=PRIMARY_COLOR,
                                     font=('Arial', 12, 'bold'))
        self.train_status.pack(pady=15)

        # Barra de progreso determinada
        self.train_progress = ttk.Progressbar(progress_frame,
                                              mode='determinate',
                                              maximum=100)
        self.train_progress.pack(fill=tk.X, padx=20, pady=10)

        # Área de log
        self.train_log = tk.Text(progress_frame, height=8, bg="#1a1a2e",
                                fg=TEXT_COLOR, font=('Consolas', 9),
                                relief=tk.FLAT)
        self.train_log.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        btn_frame = tk.Frame(frame, bg=BG_COLOR)
        btn_frame.pack(pady=20)

        self.train_btn = tk.Button(btn_frame, text="INICIAR ENTRENAMIENTO",
                                   bg=PRIMARY_COLOR, fg="black",
                                   font=('Arial', 12, 'bold'),
                                   command=self.start_training,
                                   cursor="hand2", padx=25, pady=12)
        self.train_btn.pack(side=tk.LEFT, padx=10)

        tk.Button(btn_frame, text="VOLVER",
                  bg=ACCENT_COLOR, fg="black",
                  font=('Arial', 11, 'bold'),
                  command=self.show_main,
                  cursor="hand2", padx=15, pady=10).pack(side=tk.LEFT, padx=10)

    def show_predict_section(self):
        """Muestra la sección de predicción"""
        self.show_section(
            "RECONOCER SEÑAS",
            [(None, self.create_predict_widgets)]
        )

    def create_predict_widgets(self, frame):
        """Crea los widgets de predicción"""
        info = ("Inicia la cámara para reconocer en tiempo real.\n"
                "Asegúrate de que el modelo esté entrenado.\n\n"
                "Controles:\n"
                "• 'Q' para salir\n"
                "• Muestra la seña detectada en pantalla")

        ttk.Label(frame, text=info, style='Normal.TLabel',
                  justify=tk.LEFT).pack(anchor=tk.W, pady=20)

        btn_frame = tk.Frame(frame, bg=BG_COLOR)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="INICIAR PREDICCION",
                  bg=PRIMARY_COLOR, fg="black",
                  font=('Arial', 12, 'bold'),
                  command=self.start_prediction,
                  cursor="hand2", padx=20, pady=10).pack(side=tk.LEFT, padx=10)

        tk.Button(btn_frame, text="VOLVER",
                  bg=ACCENT_COLOR, fg="black",
                  font=('Arial', 11, 'bold'),
                  command=self.show_main,
                  cursor="hand2", padx=15, pady=10).pack(side=tk.LEFT, padx=10)

    def show_section(self, title, widgets_list):
        """Muestra una sección genérica"""
        for widget in list(self.winfo_children()):
            if isinstance(widget, tk.Frame):
                widget.destroy()

        frame = tk.Frame(self, bg=BG_COLOR)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        title_label = ttk.Label(frame, text=title,
                                style='Header.TLabel')
        title_label.pack(pady=(0, 20))

        for label, widget_func in widgets_list:
            if label:
                ttk.Label(frame, text=label,
                          style='Title.TLabel').pack(anchor=tk.W, pady=(10, 5))
            if widget_func:
                widget_func(frame)

    def start_capture(self):
        """Inicia el script de captura"""
        nombre = self.capture_input.get().strip()
        if not nombre:
            messagebox.showerror("Error", "Ingresa un nombre para la seña")
            return

        # Minimizar la ventana de la GUI
        self.iconify()

        def run():
            try:
                # Configurar encoding UTF-8
                env = os.environ.copy()
                env['PYTHONIOENCODING'] = 'utf-8'
                
                # Crear script que inyecta el nombre
                script = f"""
import sys
# Inyectar el nombre directamente
class FakeInput:
    def __init__(self, value):
        self.value = value
        self.called = False
    def __call__(self, *args, **kwargs):
        if not self.called:
            self.called = True
            return self.value
        return input(*args, **kwargs)
__builtins__.input = FakeInput('{nombre}')
import capturar_secuencias
capturar_secuencias.main()
"""
                result = subprocess.run(
                    [sys.executable, "-c", script],
                    capture_output=False,
                    timeout=None,
                    cwd=os.path.dirname(os.path.abspath(__file__)),
                    env=env
                )
                self.deiconify()
                if result.returncode == 0:
                    messagebox.showinfo("Éxito",
                                        f"Captura completada para '{nombre}'")
                else:
                    messagebox.showerror("Error", "La captura fue cancelada")
            except Exception as e:
                self.deiconify()
                messagebox.showerror("Error", f"Error en captura: {str(e)}")

        threading.Thread(target=run, daemon=True).start()

    def start_training(self):
        """Inicia el entrenamiento con progreso en tiempo real"""
        self.train_btn.config(state=tk.DISABLED, bg="#555555")
        self.train_status.config(text="Entrenando...", fg="#ffaa00")
        self.train_log.delete(1.0, tk.END)
        self.train_progress['value'] = 0

        def update_ui(action, data=None):
            """Actualiza UI desde el thread principal"""
            if action == "log":
                self.train_log.insert(tk.END, data)
                self.train_log.see(tk.END)
            elif action == "progress":
                self.train_progress['value'] = data
            elif action == "status":
                self.train_status.config(text=data)
            elif action == "complete":
                self.train_progress['value'] = 100
                self.train_status.config(text="Completado!", fg=PRIMARY_COLOR)
                self.train_log.insert(tk.END,
                                     "\n=== ENTRENAMIENTO EXITOSO ===\n")
                self.train_btn.config(state=tk.NORMAL, bg=PRIMARY_COLOR)
                messagebox.showinfo("Exito",
                                   "Modelo entrenado correctamente")
            elif action == "error":
                self.train_status.config(text="Error", fg="#ff0000")
                self.train_btn.config(state=tk.NORMAL, bg=PRIMARY_COLOR)
                if data:
                    self.train_log.insert(tk.END, f"\nERROR: {data}\n")
                messagebox.showerror("Error", data or "Error entrenando")

        def run():
            try:
                env = os.environ.copy()
                env['PYTHONIOENCODING'] = 'utf-8'
                
                self.training_process = subprocess.Popen(
                    [sys.executable, "entrenar_modelo_simple.py"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    env=env,
                    bufsize=1
                )

                max_epochs = 150
                
                for line in iter(self.training_process.stdout.readline, ''):
                    if line:
                        self.after(0, update_ui, "log", line)
                        
                        if "Epoch" in line and "/" in line:
                            try:
                                parts = line.split()
                                epoch_info = parts[1].split('/')
                                epoch_count = int(epoch_info[0])
                                progress = (epoch_count / max_epochs) * 100
                                self.after(0, update_ui, "progress", progress)
                                status = f"Epoca {epoch_count}/{max_epochs}"
                                self.after(0, update_ui, "status", status)
                            except Exception:
                                pass

                self.training_process.wait()
                
                if self.training_process.returncode == 0:
                    self.after(0, update_ui, "complete", None)
                else:
                    self.after(0, update_ui, "error",
                              "Error durante el entrenamiento")
            except Exception as e:
                self.after(0, update_ui, "error", str(e))

        threading.Thread(target=run, daemon=True).start()

    def start_prediction(self):
        """Inicia la predicción"""
        try:
            import os
            env = os.environ.copy()
            env['PYTHONIOENCODING'] = 'utf-8'
            subprocess.Popen(
                [sys.executable, "predecir_secuencias.py"],
                env=env
            )
            messagebox.showinfo("Predicción Iniciada",
                                "Presiona 'Q' en la ventana de cámara "
                                "para salir")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def show_main(self):
        """Vuelve a la pantalla principal"""
        self.destroy()
        app = SignLanguageApp()
        app.mainloop()

    def back_to_launcher(self):
        """Vuelve al selector de interfaz"""
        respuesta = messagebox.askyesno(
            "Volver al Selector",
            "¿Deseas volver al selector de interfaz (GUI/Web)?"
        )
        if respuesta:
            self.destroy()
            import launcher
            app = launcher.LauncherApp()
            app.mainloop()


def main():
    root = SignLanguageApp()
    root.mainloop()


if __name__ == "__main__":
    main()
