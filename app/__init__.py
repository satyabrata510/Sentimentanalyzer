from flask import Flask
import os

app = Flask(__name__, template_folder=os.path.abspath("templates"))

from app import routes
