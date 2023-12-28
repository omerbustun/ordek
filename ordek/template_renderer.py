from jinja2 import Environment, FileSystemLoader, select_autoescape
import os

def render_html_with_template(content, title="Page Title", theme="default", template_name="base.html"):
    """
    Renders HTML content using a Jinja2 template.

    Args:
    content (str): The HTML content to be inserted into the template.
    title (str): The title of the HTML page.
    template_name (str): The name of the Jinja2 template file.
    templates_dir (str): The directory containing the Jinja2 templates.

    Returns:
    str: The rendered HTML.
    """

    templates_dir = os.path.join("themes", theme, "templates")
    
    env = Environment(
        loader=FileSystemLoader(templates_dir),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template(template_name)
    
    return template.render(title=title, content=content)
