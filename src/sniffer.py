from scapy.all import sniff, IP, TCP

def start_sniffing(callback_function):
    """
    Inicia la captura de tráfico.
    callback_function: La función que procesará cada paquete capturado.
    """
    print("[*] Sentinel-Watch: Escuchando tráfico de red...")
    # Capturamos solo tráfico TCP (común en escaneos y fuerza bruta)
    sniff(filter="tcp", prn=callback_function, store=0)