import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

def render_html_with_template(content, config, post_title=None, template_name="base.html"):
    """
    Renders HTML content using a Jinja2 template.

    Args:
    content (str): The HTML content to be inserted into the template.
    config (dict): Configuration settings.
    post_title (str): The title of the individual post (optional).
    template_name (str): The name of the Jinja2 template file.

    Returns:
    str: The rendered HTML.
    """

    theme = config.get('theme', 'default')
    templates_dir = os.path.join("themes", theme, "templates")

    # Format the title
    full_title = f"{post_title} | {config['site_title']}" if post_title else config['site_title']

    env = Environment(
        loader=FileSystemLoader(templates_dir),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template(template_name)
    
    return template.render(title=full_title, author=config['author'], content=content)

