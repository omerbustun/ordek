import markdown2
import os

def convert_markdown_to_html(file_path, output_dir="public"):
    """
    Converts a Markdown file to HTML and writes it to the output directory.

    Args:
    file_path (str): The path to the Markdown file.
    output_dir (str): The directory where the HTML file will be saved.
    """

    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    html_content = markdown2.markdown(markdown_content)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    base_name = os.path.basename(file_path)
    output_file_name = os.path.splitext(base_name)[0] + '.html'
    output_file_path = os.path.join(output_dir, output_file_name)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(html_content)
