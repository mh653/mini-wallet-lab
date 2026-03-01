from flask import Blueprint,render_template

# Blueprint名はsearch
search_bp = Blueprint('search',__name__)

# ==============================
# search画面表示処理('/search')
# ==============================
@search_bp.route('/search')
def search():
    #画面を表示
    return render_template('search/search.html')

