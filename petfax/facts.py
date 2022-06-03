from flask import (Blueprint, render_template)

bp = Blueprint('facts', __name__, url_prefix="/facts")

@bp.route('/new')
def new_fact(): 
    return render_template('create_fact.html')