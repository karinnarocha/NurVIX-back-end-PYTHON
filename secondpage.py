from flask import Blueprint, render_template

secondpage = Blueprint("secondpage", __name__, static_folder="static",
                       template_folder="templates")


@secondpage.route("/mychannel")
def channelpage():
    return render_template("my_channel.html")
