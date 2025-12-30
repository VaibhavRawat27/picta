from .loader import get_svg

def icon(name, size=24, color="currentColor"):
    """
    Return SVG string with optional size and color.
    Fully dependency-free.
    """
    svg = get_svg(name)
    svg = svg.replace('width="24"', f'width="{size}"')
    svg = svg.replace('height="24"', f'height="{size}"')
    svg = svg.replace('currentColor', color)
    return svg
