from flask import Flask, request, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import stock, errors
