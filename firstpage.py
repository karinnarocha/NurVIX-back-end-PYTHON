from flask import Blueprint, render_template

firstpage = Blueprint("firstpage", __name__, static_folder="static",
                      template_folder="templates")


@firstpage.route("/")
def home():
    return render_template("index.html")
