from ordek.markdown_processor import convert_markdown_to_html
import os

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