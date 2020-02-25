from jinja2 import Environment, PackageLoader, select_autoescape
from starlette.templating import Jinja2Templates
from starlette.requests import Request
import json


def render_daily_messages(
    request: Request, days: list, number_of_messages: list, top_ten_accounts: list, top_ten_engagements:list
):
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "days": json.dumps(days),
            "number_of_messages": json.dumps(number_of_messages),
            "top_ten_accounts": top_ten_accounts,
            "top_ten_engagements": top_ten_engagements
        },
    )

