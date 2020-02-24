from jinja2 import Environment, PackageLoader, select_autoescape
import json

def render_daily_messages(days: list, number_of_messages: list):
    env = Environment(
        loader=PackageLoader('dwise', 'templates'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('dashboard.html')
    html = template.render(days=json.dumps(days), number_of_messages=number_of_messages)
    print(html)
    return template.render(days=json.dumps(days), number_of_messages=number_of_messages)