"""
Waqtu is a web app that serves as a personal assistance 
for muslims around the world. At its core function, the app 
allows users to be aware and ahead of their daily prayer times.
Copyright (C) 2020 Dihyah Al Hii

Waqtu is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

Waqtu is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with Waqtu.  If not, see <https://www.gnu.org/licenses/>.

Contact Me:
    You may reach me at hiidihyah@gmail.com if you have any inquiries.
"""

#import osmapi
#import geocoder
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session

from datetime import datetime, date


# Configure application
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Enable session
Session(app)


@app.route("/")
def index():
    """Index page"""
    return render_template("index.html")

@app.route("/dua")
def dua():
    """Du'a"""
    return render_template("dua.html")

@app.route("/contribute")
def contribute():
    """Contribution page"""
    return render_template("contribute.html")


@app.route("/about")
def about():
    """About page"""
    return render_template("about.html")


@app.route("/terms")
def terms():
    """Terms & Conditions"""
    return render_template("terms.html")


@app.route("/policy")
def policy():
    """Privacy Policy"""
    return render_template("policy.html")


