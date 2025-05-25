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
