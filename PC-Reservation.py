import Gaon as gaon
from flask import Flask

app = Flask(__name__)
Setting = gaon.SettingManager

_Web = Setting.setting.get("Server").get("Web")


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(_Web.get("host"), _Web.get("port"))
