from fastapi import FastAPI, Request, responses

from examples.spotify import spotify_docs
from scalar_doc import ScalarColorSchema, ScalarDoc, ScalarHeader, ScalarTheme

DESCRIPTION = """
# Sidebar Section

## Sidebar SubSection

### Title

Content
"""

app = FastAPI(title="Test", description=DESCRIPTION, docs_url=None, redoc_url=None)


@app.post("/foo")
def post_foo(a: str):
    return a + " - ok"


@app.get("/docs", include_in_schema=False)
def get_docs(request: Request):
    docs = ScalarDoc.from_spec(request.app.openapi_url)
    return responses.HTMLResponse(docs.to_html())


@app.get("/docs/spotify", include_in_schema=False)
def get_docs_spotify():
    html = spotify_docs.to_html()
    return responses.HTMLResponse(html)


@app.get("/docs/maistodos", include_in_schema=False)
def get_docs_maistodos(request: Request):
    docs = ScalarDoc.from_spec(request.app.openapi_url)
    docs.set_header(
        ScalarHeader(
            logo_url="https://www.maistodos.com.br/wp-content/uploads/2024/08/logo-white-and-green.webp",
        )
    )
    docs.set_title("Mais Todos")
    docs.set_theme(
        ScalarTheme(
            favicon_url="https://www.maistodos.com.br/wp-content/uploads/2024/06/faviconV2.png",
            color_scheme_light=ScalarColorSchema(
                color_1="#000000",
                color_2="#00000088",
                color_3="#7200d6",
                background_1="#ffffff",
                background_2="#00000011",
                background_3="#00000022",
                color_accent="#7200d6",
                background_accent="#7200d644",
                link_color="#6de102",
                code="#7200d6",
            ),
            color_scheme_dark=ScalarColorSchema(
                color_1="#ffffff",
                color_2="#ffffff88",
                color_3="#6de102",
                background_1="#10001E",
                background_2="#18002E",
                background_3="#9B29FF22",
                color_accent="#9B29FF",
                background_accent="#360066",
                link_color="#6de102",
                code="#7200d6",
            ),
        ),
    )
    return responses.HTMLResponse(docs.to_html())
