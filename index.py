from flask import Flask, render_template_string
from picta import icon, list_icons

app = Flask(__name__)

@app.route("/")
def home():
    # List all icons
    icons = list_icons()

    # Generate icon cards
    icon_cards = ""
    for name in icons:
        svg_code = icon(name, size=48, color="#1e40af")  # blue color
        icon_cards += f"""
        <div class="icon-card">
            {svg_code}
            <p>{name}</p>
        </div>
        """

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Picta Icon Library</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f8fafc;
                margin: 0;
                padding: 0;
            }}
            header {{
                background-color: #1e3a8a;
                color: white;
                padding: 2rem;
                text-align: center;
            }}
            header h1 {{
                margin: 0;
                font-size: 2.5rem;
            }}
            header p {{
                font-size: 1.1rem;
                margin-top: 0.5rem;
            }}
            .install {{
                text-align: center;
                margin: 2rem 0;
                font-size: 1.2rem;
            }}
            .install code {{
                background-color: #e0e7ff;
                padding: 0.2rem 0.5rem;
                border-radius: 4px;
            }}
            .icons-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
                gap: 1rem;
                padding: 2rem;
            }}
            .icon-card {{
                background-color: white;
                border-radius: 12px;
                padding: 1rem;
                text-align: center;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                transition: transform 0.2s, box-shadow 0.2s;
            }}
            .icon-card:hover {{
                transform: translateY(-4px);
                box-shadow: 0 6px 12px rgba(0,0,0,0.15);
            }}
            .icon-card svg {{
                width: 48px;
                height: 48px;
                margin-bottom: 0.5rem;
            }}
            .footer {{
                text-align: center;
                padding: 2rem;
                color: #475569;
            }}
            
        </style>
    </head>
    <body>
        <header>
            <h1>Picta Icon Library</h1>
            <p>A Python-first, dependency-free icon library for web apps and dashboards.</p>
        </header>

        <div class="install">
            Install via pip: <code>pip install picta</code>
        </div>

        <div class="icons-grid">
            {icon_cards}
        </div>

        <div class="footer">
    &copy; 2025 Vaibhav Rawat | Powered by Picta | Inspired by Lucide Icons
    <br><br>
    <a href="https://github.com/VaibhavRawat27/picta" target="_blank" class="github-btn">Contribute on GitHub</a>
</div>

    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
