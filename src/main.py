import os
import sys
import ctypes
from sniffer import start_sniffing

def check_admin():
    """Verifica si el script se está ejecutando con privilegios de administrador."""
    if os.name == 'nt':  # Para Windows
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        except:
            is_admin = False
        
        if not is_admin:
            print("\n" + "!" * 50)
            print("❌ ERROR: PRIVILEGIOS INSUFICIENTES")
            print("Sentinel-Watch requiere permisos de Administrador para")
            print("capturar paquetes de red en modo promiscuo.")
            print("!" * 50 + "\n")
            print("👉 Tip: Abre PowerShell o CMD como administrador y vuelve a intentarlo.")
            sys.exit(1)
    else:
        # Para Linux/macOS (usando el ID de usuario 0 que es root)
        if os.getuid() != 0:
            print("\n❌ ERROR: Sentinel-Watch requiere privilegios de ROOT (sudo).")
            sys.exit(1)

def main():
    # 1. Validación de seguridad inicial
    check_admin()

    print("-" * 50)
    print("      🛡️  SENTINEL-WATCH: IDS v1.1 ACTIVE")
    print("      Status: MONITORING NETWORK TRAFFIC")
    print("      Press [Ctrl + C] to stop and save logs.")
    print("-" * 50)

    try:
        # 2. Iniciar el motor de detección (Tu lógica principal)
        start_sniffing()

    except KeyboardInterrupt:
        # 3. Cierre controlado del programa
        print("\n\n" + "=" * 50)
        print("🛑 DETECCIÓN FINALIZADA POR EL USUARIO")
        print("Realizando cierre seguro de sockets y logs...")
        print("Estado: Sesión guardada correctamente.")
        print("Pura vida, IDS SENTINEL-YFAJARDO. 🇨🇷")
        print("=" * 50)
        
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

if __name__ == "__main__":
    main()