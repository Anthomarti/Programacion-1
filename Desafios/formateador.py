# formateador.py

"""
0m: Restaura el estilo de texto predeterminado
1m: Negrita
2m: Debilita el texto (no es compatible con todas las terminales)
3m: Cursiva
4m: Subrayado
5m: Parpadeo lento
6m: Parpadeo rápido
7m: Inversión de colores (fondo y texto)
8m: Oculta el texto (no es compatible con todas las terminales)
9m: Tachado (no es compatible con todas las terminales)
"""

def texto_negrita(texto):
    return f"\033[1m{texto}\033[0m"

def texto_italica(texto):
    return f"\033[3m{texto}\033[0m"

def texto_subrayado(texto):
    return f"\033[4m{texto}\033[0m"