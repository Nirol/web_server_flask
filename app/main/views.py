from flask import render_template, jsonify


from forms import YeshuvNameQuery

from models import  Yeshuv
from yeshuv_sn_by_name import query_yeshuv_sn_by_name
from . import main
from flask import request
from app import db


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')




@main.route("/a11", methods=['GET', 'POST'])
def a11():
    yeshuv_form = YeshuvNameQuery()
    if yeshuv_form.validate_on_submit():

        yeshuv_name = yeshuv_form.yeshuv_name.data
        yeshuv_sn = query_yeshuv_sn_by_name(yeshuv_name)
        create_json_response=


        # print(to_json)
        # print("kkkaaaa")
        # bb = jsonify(to_json)
        # print(bb)
        return render_template('auto_complete.html',form=yeshuv_form,
                               yeshuv_name_select=yeshuv_name)

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


