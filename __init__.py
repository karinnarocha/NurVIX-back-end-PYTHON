from flask import Flask, render_template
from firstpage import firstpage
from secondpage import secondpage
from thirdpage import thirdpage

app = Flask(__name__)

app.register_blueprint(firstpage, url_prefix="/home")
app.register_blueprint(secondpage, url_prefix="/mychannel")
app.register_blueprint(thirdpage, url_prefix="/content")


@app.route("/home/")
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/mychannel/")
def mychannel():
    return render_template("my_channel.html")


@app.route("/content/")
def content():
    return render_template("content.html")


if __name__ == "__main__":
    app.run(debug=True)
