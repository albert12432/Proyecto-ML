# -*- coding: utf-8 -*-
"""
main.py - Sistema de Reconocimiento de Lengua de Señas
Punto de entrada principal del sistema con interfaz dual (GUI/Web)
"""

import sys
import os

# Asegurar que el directorio actual esté en el path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def print_banner():
    """Muestra un banner de bienvenida en consola"""
    banner = """
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║       🤟  SISTEMA DE LENGUA DE SEÑAS CON IA  🤟          ║
    ║                                                           ║
    ║       Reconocimiento en Tiempo Real con Deep Learning    ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    
    Iniciando selector de interfaz...
    """
    print(banner)


def check_dependencies():
    """Verifica que las dependencias principales estén instaladas"""
    required = ['flask', 'cv2', 'mediapipe', 'tensorflow']
    missing = []
    
    for module in required:
        try:
            __import__(module)
        except ImportError:
            missing.append(module)
    
    if missing:
        print(f"\n⚠️  Dependencias faltantes: {', '.join(missing)}")
        print("Instala con: pip install -r requirements.txt\n")
        return False
    return True


def main():
    """Inicia el selector de interfaz del sistema"""
    print_banner()
    
    # Verificar dependencias
    if not check_dependencies():
        input("\nPresiona Enter para salir...")
        sys.exit(1)
    
    print("✓ Todas las dependencias están instaladas")
    print("✓ Abriendo selector de interfaz...\n")
    
    try:
        from launcher import LauncherApp
        app = LauncherApp()
        app.mainloop()
    except ImportError as e:
        print(f"\n❌ Error: No se pudo importar el launcher: {e}")
        input("\nPresiona Enter para salir...")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error al iniciar la aplicacion: {e}")
        import traceback
        traceback.print_exc()
        input("\nPresiona Enter para salir...")
        sys.exit(1)


if __name__ == '__main__':
    main()
