import qdarkstyle
from variables import (DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR, PRIMARY_COLOR)

qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""

def setupTheme(app):
    # Carregar o estilo qdarkstyle
    dark_stylesheet = qdarkstyle.load_stylesheet_pyside6()

    # Combinar o qdarkstyle com o QSS personalizado
    combined_stylesheet = dark_stylesheet + qss

    # Aplicar o estilo combinado ao aplicativo
    app.setStyleSheet(combined_stylesheet)

