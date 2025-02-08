#!/usr/bin/env python

from os import uname, getlogin
from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)

home_dir = Path.home()
hostname = uname()[1]
username = getlogin()

@app.route("/")
def home():
    with open(f"{home_dir}/.bash_history") as history:
        commands = history.readlines()
    return render_template(
        "base.html",
        hostname=f"{username}@{hostname}",
        commands=commands,
    )

app.run()
