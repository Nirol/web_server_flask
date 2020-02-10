from flask import render_template, jsonify
from forms import YeshuvNameQuery

from models import User, Yeshuv
from . import main
from flask import request, session
from app import db


@main.route('/', methods=['GET', 'POST'])
def index():
    ip_address = get_ip()
    user = User.query.filter_by(ip=ip_address).first()
    if user is None:
        user = User(ip=ip_address)
        db.session.add(user)
        session['known'] = False
    else:
        session['known'] = True

    session['ip'] = ip_address
    user.ping()
    return render_template('index.html',
                           name=session.get('name'),
                           known=session.get('known', False))




@main.route("/a11", methods=['GET', 'POST'])
def a11():
    yeshuv_form = YeshuvNameQuery()
    if yeshuv_form.validate_on_submit():
        yeshuv_name = yeshuv_form.yeshuv_name.data
        # to_json = single_yeshuv_json_response("18", 300)
        # print(to_json)
        # print("kkkaaaa")
        # bb = jsonify(to_json)
        # print(bb)
        # return render_template('auto_complete.html',
        #                        yeshuv_name_select=yeshuv_name, lol=bb)

    return render_template('auto_complete.html', form=yeshuv_form)




@main.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    # optional_yeshuv_list = Yeshuv.query.filter(Yeshuv.yeshuv_name_hebrew.like('%' + str(search) + '%'))
    optional_yeshuv_list = db.session.query(Yeshuv.yeshuv_name_hebrew).filter(
        Yeshuv.yeshuv_name_hebrew.like('%' + str(search) + '%'))
    yeshuvs = []
    for yeshuv in optional_yeshuv_list:
        yeshuvs.append(yeshuv.yeshuv_name_hebrew)
    return jsonify(matching_results=yeshuvs)


def get_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR']
    else:
        request.environ['HTTP_X_FORWARDED_FOR']
