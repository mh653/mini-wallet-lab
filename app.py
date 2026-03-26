from flask import Flask, render_template, request
from blueprints.pages import pages_bp
from blueprints.login import login_bp
from blueprints.member_registration import member_registration_bp
from blueprints.products import products_bp
from blueprints.cart import cart_bp
from blueprints.search import search_bp
from blueprints.mypage import mypage_bp
from blueprints.admin import admin_bp
import os

app = Flask(__name__)

# セッションデータを暗号化するための鍵
# Flash用
app.secret_key = "secret"

# blueprintsを登録
app.register_blueprint(pages_bp)
app.register_blueprint(login_bp)
app.register_blueprint(member_registration_bp)
app.register_blueprint(products_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(search_bp)
app.register_blueprint(mypage_bp)
app.register_blueprint(admin_bp)


# 全ページ共通
@app.context_processor
def inject_user():
  # cookieからユーザIDを取得。存在しない場合はNoneが格納される
  user_id = request.cookies.get("user_id")
  return dict(user_id=user_id)


# ==============================
# HOME画面表示処理('/')
# ==============================
@app.route("/")
def index():
  # HOME画面を表示
  return render_template("index.html")


# ==============================
# アプリケーション実行
# ==============================
# if __name__ == "__main__":
#   app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))

# 開発環境用
if __name__ == "__main__":
  app.run(host="localhost", port=5000, debug=True)
