from jinja2 import Environment, PackageLoader, select_autoescape
from starlette.templating import Jinja2Templates
from starlette.requests import Request
import json
from typing import List, Dict


def render_daily_messages(
    request: Request,
    days: List,
    number_of_messages: List,
    top_ten_accounts: List,
    top_ten_engagements: List,
    word_cloud: Dict,
    hashtag_cloud: Dict,
):
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "days": json.dumps(days),
            "number_of_messages": json.dumps(number_of_messages),
            "top_ten_accounts": list(top_ten_accounts),
            "top_ten_engagements": top_ten_engagements,
            "word_cloud": json.dumps(word_cloud),
            "hashtag_cloud": json.dumps(hashtag_cloud),
        },
    )

