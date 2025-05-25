# 📘 Scalar DOC

A powerful, customizable, and fully native way to render OpenAPI documentation using [Scalar API Reference](https://github.com/scalar/scalar) — directly from Python 🐍.


## ✨ Why Scalar DOC?

`scalar-doc` is a lightweight Python library that helps you **generate beautiful and interactive API documentation** from OpenAPI specs using the blazing-fast and modern [Scalar](https://scalar.dev/). Unlike static alternatives or clunky HTML exporters, Scalar DOC offers:

* ✅ **100% native Python**: No Node.js or frontend tooling required
* 🎨 **Fully customizable UI**: Tweak everything from layout to color scheme
* 🔗 **Compatible with any OpenAPI source**: Works seamlessly with generators like:

  * [FastAPI](https://fastapi.tiangolo.com/)
  * [Flask-RESTPlus](https://flask-restplus.readthedocs.io/)
  * [Django REST Framework](https://www.django-rest-framework.org/)
  * And any tool that outputs OpenAPI in JSON or URL format
* 💡 **Zero-config or full control**: Use sensible defaults or dive deep into layout, themes, authentication behavior, and more
* 🧰 **CLI support** (Coming Soon): Easily generate HTML files from your terminal


## 🚀 Installation

```bash
pip install scalar-doc
```

## ⚙️ How to Use

Checkout the `examples` folder to see the complete implementation of:
- A Spotify based theme for the Scalar DOCs
- A implementation using FastAPI

#### ✨ With FastAPI (Or any OpenAPI URL)

```python
from fastapi import FastAPI, responses

from scalar_doc import ScalarDoc

DESCRIPTION = """
# Sidebar Section

## Sidebar SubSection

### Title

Content
"""

app = FastAPI(
    title="Test",
    description=DESCRIPTION,
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)
docs = ScalarDoc.from_spec(app.openapi(), mode="dict")



@app.post("/foo")
def post_foo(a: str):
    return a + " - ok"


@app.get("/docs", include_in_schema=False)
def get_docs():
    return responses.HTMLResponse(docs.to_html())

```

Then simply run your application and see the magic! ✨

---

#### 🔧 Programmatically (Python)

```python
from scalar_doc import ScalarDocs, ScalarHeader, ScalarConfiguration

# From URL
docs = ScalarDocs.from_spec("https://example.com/openapi.json", mode="url")
docs.set_title("My API Docs")

# Optional: Tweak Scalar's configuration
docs.set_configuration(ScalarConfiguration(hide_sidebar=True))

# Output to HTML file
docs.to_file("docs/index_from_url.html")

# From JSON File
with open("openapi.json", "r", encoding="utf-8") as f:
    spec_json = f.read()

# Update specification
docs.set_spec(spec=spec_json, mode="json")

# Output to HTML file
docs.to_file("docs/index_from_file.html")
```

Then simply open `docs/index.html` in your browser!

---

#### 💻 From the CLI


Once installed, you can generate static docs from a URL or a JSON file:

- **From JSON File**
    ```bash
    scalar-doc path/to/openapi.json --mode json --output docs.html
    ```
- **From Openapi URL File**
    ```bash
    scalar-doc https://api.example.com/openapi.json --output docs.html
    ```
> CLI generated DOCs customization will soon be contemplated, stay tuned!


## 🧰 Customization

You can fully control the appearance and behavior of the documentation by adjusting:

* **Theme**: Light/dark mode colors, logo, favicon
* **Header**: Logo (light/dark), external links
* **Configuration**: Toggle visibility of models, sidebar, search, examples, etc.

Refer to the `ScalarConfiguration` dataclass for all options.

#### 🎵 Spotify API Customization Example
```python
from scalar_doc import (
    ScalarColorSchema,
    ScalarConfiguration,
    ScalarDoc,
    ScalarHeader,
    ScalarTheme,
)

spotify_docs = ScalarDoc.from_spec(
    "https://raw.githubusercontent.com/sonallux/spotify-web-api/refs/heads/main/official-spotify-open-api.yml"
)
spotify_docs.set_title("Spotify")
spotify_docs.set_header(
    ScalarHeader(
        logo_url="https://storage.googleapis.com/pr-newsroom-wp/1/2023/09/Spotify_Logo_RGB_Green.png",
        logo_url_dark="https://storage.googleapis.com/pr-newsroom-wp/1/2023/09/Spotify_Logo_RGB_White.png",
        links={"Spotify": "https://spotify.com"},
    )
)
spotify_docs.set_configuration(
    ScalarConfiguration(
        hide_download_button=True,
        show_models=False,
        expand_table_of_contents=True,
        schema_style="table",
    )
)
spotify_docs.set_theme(
    ScalarTheme(
        favicon_url="https://upload.wikimedia.org/wikipedia/commons/1/19/Spotify_logo_without_text.svg",
        color_scheme_light=ScalarColorSchema(
            color_1="#191414",  # Main Text
            color_2="#3e3e3e",  # Secondary Text
            color_3="#1DB954",  # Alternate Text - Spotify Green
            background_1="#ffffff",  # Main Background
            background_2="#f0f0f0",  # Secondary Background
            background_3="#e6e6e6",  # Alternate Background
            color_accent="#1DB954",  # Accent Text
            background_accent="#d2fbe3",  # Accent Background
            link_color="#1DB954",  # Links
            code="#2b2b2b",  # Code
        ),
        color_scheme_dark=ScalarColorSchema(
            color_1="#ffffff",
            color_2="#aaaaaa",
            color_3="#1DB954",
            background_1="#191414",  # Main Background
            background_2="#121212",  # Secondary Background
            background_3="#282828",  # Alternate Background
            color_accent="#1DB954",  # Accent Text
            background_accent="#1DB95433",  # Accent Background
            link_color="#1DB954",  # Links
            code="#1DB954",  # Code
        ),
    )
)
```

## 📌 References

* 📖 Scalar API Docs: [scalar.dev](https://scalar.dev/)
* 📦 Underlying engine: [github.com/scalar/scalar](https://github.com/scalar/scalar)
* ✍️ OpenAPI standard: [openapis.org](https://www.openapis.org/)

> This library is not affiliated with Scalar, but uses their open-source API Reference component with ❤️ and attribution.


## 🛠 Contributing

Contributions and feedback are welcome! If you find bugs or want to suggest improvements, feel free to open an issue or PR.

> There are some features that are not working yet, mainly the `ScalarConfiguration` abstraction isn't refleting in the DOCs behavior, this issue will be resolved in the next release.


## 📄 License

MIT License. See [LICENSE](./LICENSE) for details.
