# Picta – Python Icon Library

![Picta](https://img.shields.io/badge/Picta-v0.2.0-blue?style=for-the-badge)

Picta is a **Python-first, dependency-free icon library** inspired by [Lucide Icons](https://lucide.dev/). It allows Python developers to **easily use SVG icons** in web apps, dashboards, or any Python project that can render HTML.

---

## 🌟 Features

- **100+ most used icons** included (SVG files bundled).  
- **Zero external dependencies** — works on any OS with Python ≥ 3.8.  
- **Dynamic icon listing** via `list_icons()` to discover all available icons.  
- **Direct SVG output** via `icon()` for web, Flask, Streamlit, Dash, or Jupyter notebooks.  
- Clean, easy-to-use **Python API**.  

---

## 📦 Installation

Install via pip:

```bash
pip install picta
```

Or download the latest release manually:

[![Download](https://img.shields.io/badge/Download-Release-blue?style=for-the-badge)](https://github.com/VaibhavRawat27/picta/releases/latest)

---

## ⚡ Quick Start

### Importing icons

```python
from picta import icon, list_icons

# Get an SVG string for a single icon
svg_str = icon("user", size=32, color="blue")
print(svg_str)

# List all available icons
all_icons = list_icons()
print(all_icons)
```

---

### 🔹 Using in a web app (Flask)

```bash
pip install flask
python index.py
```

Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000) to see the icons.

---

## 💻 Demo

- Header explaining Picta and its purpose  
- Install instructions with pip command  
- Grid of icons showing **icon + name**  
- Footer with **“Contribute on GitHub” button** and credit to Lucide Icons  

---

## 🔧 Usage Examples

### Getting a single icon

```python
from picta import icon

user_icon = icon("user", size=48, color="#1e40af")
```

### Displaying multiple icons dynamically

```python
from picta import icon, list_icons

for name in list_icons()[:10]:
    print(icon(name, size=32))
```

---

## 🤝 Contributing

Picta is **open-source**. Contributions are welcome!  

- Submit bug reports or feature requests via [GitHub Issues](https://github.com/VaibhavRawat27/picta/issues)  
- Fork the repository and submit pull requests  
- Help us **add more icons or improve documentation**

[![Contribute on GitHub](https://img.shields.io/badge/Contribute-GitHub-black?style=for-the-badge&logo=github)](https://github.com/VaibhavRawat/picta)

---

## 📄 License

Picta is released under the **MIT License**.  
Icons are inspired by [Lucide Icons](https://lucide.dev/) and follow their usage rules.
