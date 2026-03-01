from flask import Blueprint,render_template

# Blueprint名はsearch
admin_bp = Blueprint('admin',__name__)

# ==============================
# admin_login画面表示処理('/admin_login')
# ==============================
@admin_bp.route('/admin_login')
def admin_login():
    #画面を表示
    return render_template('admin/admin_login.html')