from flask import Blueprint, render_template, request, make_response, redirect
from db import connect_db

# Blueprint名はmember_registration
member_registration_bp = Blueprint("member_registration", __name__)

# ================================================
# 会員登録画面出力処理('/member_registration')
# ================================================
@member_registration_bp.route("/member_registration", methods=["GET"])
def member_registration():
	# 会員登録画面出力処理
	return render_template("member_registration/member_registration.html")

# ================================================
# 会員登録成功画面出力処理('/member_registration_add')
# ================================================
@member_registration_bp.route("/member_registration_add", methods=["POST"])
def member_registration_add():
  # フォームからユーザー名を取得
  user_id = request.form.get("mail")
  password = request.form.get("pass")
  pass_confirm = request.form.get("pass_confirm")
  name = request.form.get("name")
  birthday = request.form.get("birthday")
  gender = request.form.get("gender")
  tel = request.form.get("tel")
  zip = request.form.get("zip")
  address1 = request.form.get("address1")
  address2 = request.form.get("address2")
  address3 = request.form.get("address3")
  m_flag = request.form.get("m_flag")

  # pass一致チェック
  if password != pass_confirm:
    err_msg = "パスワードが一致しません"
    return render_template("pages/error.html", err_msg=err_msg)

  # DB接続
  con = connect_db()  # コネクション
  cur = con.cursor(dictionary=True)

  # ID重複チェック
  sql = "SELECT id FROM t_member WHERE id=%s"
  cur.execute(sql,(user_id,))
  exists = cur.fetchone()
  if exists:
    cur.close()
    con.close()
    err_msg = "このメールアドレスは既に登録されています"
    return render_template("pages/error.html", err_msg=err_msg)

  # 登録用SQLを作成
  sql = """
  INSERT INTO t_member(
    id,
    pass,
    name,
    birthday,
    gender,
    tel,
    zip,
    address1,
    address2,
    address3,
    m_flag
  )
  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
  """

  data = (
    user_id,
    password,
    name,
    birthday,
    gender,
    tel,
    zip,
    address1,
    address2,
    address3,
    m_flag
    )

  cur.execute(sql,data)
  con.commit()  # コネクション
  cur.close()
  con.close()  # コネクション

  # レスポンスオブジェクトを作成
  response = make_response(redirect("/member_registration_success"))
  # ユーザIDをCookieに保存
  response.set_cookie("user_id", user_id, max_age=60 * 60 * 24 * 1)
  # レスポンスオブジェクトを返す
  return response

# ================================================
# 会員登録完了画面出力'/member_registration_success')
# ================================================
@member_registration_bp.route("/member_registration_success")
def member_registration_success():
	# 会員登録完了画面出力
	return render_template("member_registration/member_registration_success.html")

