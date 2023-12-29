import shutil
import pytest
from ordek.template_renderer import render_html_with_template

def test_render_html_with_template(tmpdir):
    # Create the directory structure that matches your project's expectations
    themes_dir = tmpdir.mkdir("themes")
    default_theme_dir = themes_dir.mkdir("default")
    templates_dir = default_theme_dir.mkdir("templates")

    # Create a sample template file
    template_file = templates_dir.join("base.html")
    template_file.write("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{{ title }}</title>
        </head>
        <body>
            <p>{{ content }}</p>
            <footer>Author: {{ author }}</footer>
        </body>
        </html>
    """)

    # Mock config
    config = {
        'theme': 'default',
        'site_title': 'Test Site',
        'author': 'Test Author'
    }

    # Copy the mock theme directory to the actual location Jinja2 will look for
    shutil.copytree(str(themes_dir), 'themes', dirs_exist_ok=True)

    # Call the function
    rendered_html = render_html_with_template(
        content="Hello, World!",
        config=config,
        post_title="Test Post"
    )

    # Assert the rendered HTML
    full_title = f"Test Post | Test Site"
    assert f"<title>{full_title}</title>" in rendered_html
    assert "<p>Hello, World!</p>" in rendered_html
    assert "<footer>Author: Test Author</footer>" in rendered_html

    # Clean up: Remove the copied themes directory after the test
    shutil.rmtree('themes')
