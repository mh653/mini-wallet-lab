from flask import Blueprint,render_template

# Blueprint名はsearch
mypage_bp = Blueprint('mypage',__name__)

# ==============================
# mypage画面表示処理('/mypage')
# ==============================
@mypage_bp.route('/mypage')
def mypage():
    #画面を表示
    return render_template('mypage/mypage.html')