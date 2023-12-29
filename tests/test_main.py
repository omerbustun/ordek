import os
import yaml
from ordek.markdown_processor import convert_markdown_to_html
from ordek.main import load_config

def test_convert_markdown_to_html(tmpdir):
    # Create a sample Markdown file
    test_md_file = tmpdir.join("test.md")
    test_md_file.write("# Hello World")

    # Define the output directory
    output_dir = str(tmpdir)

    # Run the conversion
    convert_markdown_to_html(str(test_md_file), output_dir=output_dir)

    # Check if the output HTML file exists
    output_html_file = os.path.join(output_dir, "test.html")
    assert os.path.isfile(output_html_file)

    # Read and verify the HTML content
    with open(output_html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    assert "<h1>Hello World</h1>" in html_content


def test_load_config(tmpdir):
    # Create a sample config file
    sample_config = {
        'theme': 'default',
        'site_title': 'Test Blog',
        'author': 'Jane Doe'
    }
    config_file = tmpdir.join("config.yml")
    config_file.write(yaml.dump(sample_config))

    # Load the config
    config = load_config(str(config_file))

    # Assert the values are correct
    assert config['theme'] == 'default'
    assert config['site_title'] == 'Test Blog'
    assert config['author'] == 'Jane Doe'