import mysql.connector
import os

# ==============================
# DB接続
# ==============================
def connect_db():
  if os.environ.get("DB_HOST"):
    # 本番（Aiven）
    return mysql.connector.connect(
      host=os.environ.get("DB_HOST"),
      port=int(os.environ.get("DB_PORT")),
      user=os.environ.get("DB_USER"),
      passwd=os.environ.get("DB_PASSWORD"),
      db=os.environ.get("DB_NAME"),
      ssl_ca=None,
      ssl_verify_cert=False,
      ssl_verify_identity=False
    )
  else:
    # ローカル（XAMPP）
    return mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      db="db_mini_wallet_lab"
    )