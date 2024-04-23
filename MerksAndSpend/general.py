# ====================================================================
# FUNCIONES DE USO GENERAL
# Funcion para centrar una ventana en la pantalla
def CentraVentana(ventana, ancho, alto):
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    x = (screen_width - ancho) // 2
    y = (screen_height - alto) // 2
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')