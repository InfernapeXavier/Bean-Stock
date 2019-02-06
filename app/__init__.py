from flask import Flask, request, render_template

app = Flask(__name__)
app.secret_key = "x/A?D(G+KbPeShVmYq3s6v9y$B&E)H@M"

from app import stock, errors
