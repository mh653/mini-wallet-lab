from flask import Blueprint,render_template

# Blueprint名はabout
pages_bp = Blueprint('pages',__name__)

# ==============================
# about画面表示処理('/about')
# ==============================
@pages_bp.route('/about')
def about():
    #画面を表示
    return render_template('pages/about.html')

# ==============================
# news画面表示処理('/news')
# ==============================
@pages_bp.route('/news')
def news():
    #画面を表示
    return render_template('pages/news.html')

# ==============================
# store画面表示処理('/store')
# ==============================
@pages_bp.route('/store')
def store():
    #画面を表示
    return render_template('pages/store.html')
