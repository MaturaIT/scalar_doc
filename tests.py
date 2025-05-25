import os
import tempfile
import unittest

from scalar_doc import ScalarDoc

MOCK_OPENAPI_DICT = {
    "openapi": "3.0.0",
    "info": {"title": "Sample API", "version": "1.0.0"},
    "paths": {
        "/hello": {
            "get": {
                "summary": "Say Hello",
                "responses": {"200": {"description": "Successful Response"}},
            }
        }
    },
}


class TestScalarDoc(unittest.TestCase):
    def test_scalar_doc_from_dict(self):
        doc = ScalarDoc.from_spec(MOCK_OPENAPI_DICT, mode="dict")
        html = doc.to_html()
        self.assertIn("<!DOCTYPE html>", html)
        self.assertIn("Sample API", html)

    def test_scalar_doc_from_url(self):
        docs = ScalarDoc.from_spec(
            "https://spec.openapis.org/oas/3.0.3/openapi.json", mode="url"
        )
        self.assertIsNotNone(docs)

    def test_scalar_doc_set_spec(self):
        doc = ScalarDoc.from_spec(MOCK_OPENAPI_DICT, mode="dict")
        doc.set_spec(MOCK_OPENAPI_DICT, mode="dict")
        html = doc.to_html()
        self.assertIn("Sample API", html)

    def test_export_to_html_file(self):
        doc = ScalarDoc.from_spec(MOCK_OPENAPI_DICT, mode="dict")
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = os.path.join(tmpdir, "docs.html")
            doc.to_file(output_path)
            self.assertTrue(os.path.exists(output_path))
            with open(output_path, "r", encoding="utf-8") as f:
                content = f.read()
                self.assertIn("Sample API", content)


if __name__ == "__main__":
    unittest.main()
