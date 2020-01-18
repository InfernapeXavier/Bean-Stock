from flask import Flask, request, render_template
from config import Config
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://c18c45722b3146f0b6d15c68d7cbf31c@sentry.io/1886990",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)
app.config.from_object(Config)

from app import stock, errors
