from flask import Blueprint, render_template

thirdpage = Blueprint("thirdpage", __name__, static_folder="static",
                      template_folder="templates")


@thirdpage.route("/content")
def contentpage():
    return render_template("content.html")
