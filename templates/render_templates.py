from jinja2 import Environment, FileSystemLoader
from loguru import logger


def render_template(template_name: str, **kwargs) -> str:
    logger.debug(f"Render template {template_name} with arguments: {kwargs}")
    env = Environment()
    env.loader = FileSystemLoader("templates")
    template = env.get_template(f"{template_name}.txt")
    return template.render(**kwargs)
