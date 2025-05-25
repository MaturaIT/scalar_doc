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
            color_1="#191414",  # Texto principal
            color_2="#3e3e3e",  # Texto secundário
            color_3="#1DB954",  # Verde Spotify
            background_1="#ffffff",  # Fundo principal
            background_2="#f0f0f0",  # Fundo secundário
            background_3="#e6e6e6",  # Fundo terciário
            color_accent="#1DB954",  # Cor de destaque
            background_accent="#d2fbe3",  # Fundo do destaque
            link_color="#1DB954",  # Links
            code="#2b2b2b",  # Código
        ),
        color_scheme_dark=ScalarColorSchema(
            color_1="#ffffff",
            color_2="#aaaaaa",
            color_3="#1DB954",
            background_1="#191414",  # Fundo principal
            background_2="#121212",  # Fundo secundário
            background_3="#282828",  # Fundo terciário
            color_accent="#1DB954",  # Cor de destaque
            background_accent="#1DB95433",  # Fundo do destaque
            link_color="#1DB954",  # Links
            code="#1DB954",  # Código
        ),
    )
)
