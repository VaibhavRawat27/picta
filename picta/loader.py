import os

ICON_PATH = os.path.join(os.path.dirname(__file__), "icons")

def get_svg(name):
    """
    Load SVG content by icon name.
    """
    path = os.path.join(ICON_PATH, f"{name}.svg")
    if not os.path.exists(path):
        raise ValueError(f"Icon '{name}' not found in Picta icons.")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def list_icons():
    """
    Return a list of all available icon names.
    """
    icons = []
    for file in os.listdir(ICON_PATH):
        if file.endswith(".svg"):
            icons.append(file.replace(".svg", ""))
    return sorted(icons)
