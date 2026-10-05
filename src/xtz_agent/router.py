import re

ROUTES = {
    "PRODUCT_AUDIT": ("shopee","aliexpress","mercado livre","produto","anúncio","serve","compatível","comprar","carburador"),
    "PHOTO_SCAN": ("foto","imagem","ferrugem","corrosão","vazamento","chicote","fio","conector"),
    "DIAGNOSTIC": ("não pega","falha","morre","barulho","sem força","descarrega","superaquece","freio ruim"),
    "ELECTRICAL": ("cdi","bobina","estator","regulador","bateria","painel","farol","elétrica","tps"),
    "TRANSMISSION": ("pinhão","coroa","corrente","relação","marcha","embreagem"),
    "UPGRADE_ENGINE": ("upgrade","opgreid","potência","desempenho","mais forte","restomod"),
    "MAINTENANCE": ("revisão","óleo","manutenção","trocar","lubrificar"),
}

def route(text: str) -> str:
    t = re.sub(r"\s+", " ", text.lower()).strip()
    scored = [(name, sum(1 for key in keys if key in t)) for name, keys in ROUTES.items()]
    name, score = max(scored, key=lambda item: item[1])
    return name if score else "GENERAL_XTZ"
