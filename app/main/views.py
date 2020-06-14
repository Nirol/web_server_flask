from flask import render_template, jsonify


from forms import YeshuvNameQuery
from kalfi_display import  get_yeshuv_kalfi_json, \
    get_yeshuv_knesset_elections_data_json

from models import  Yeshuv
from queries.knesset22 import query_knesset_22_kalfi_count
from queries.yeshuv_type import query_yeshuv_type_json_by_name
from text_helper import  dequote_wrapper
from yeshuv_sn_by_name import query_yeshuv_sn_by_name, \
    query_yeshuv_type_by_name

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
        yeshuv_type_json = query_yeshuv_type_json_by_name(yeshuv_name)

        num_kalfis_22 = query_knesset_22_kalfi_count(yeshuv_sn)
        kalfis_json = get_yeshuv_kalfi_json(yeshuv_sn, num_kalfis_22)
        knesset_years_yeshuv_json = get_yeshuv_knesset_elections_data_json(yeshuv_sn)


        return render_template('auto_complete.html',form=yeshuv_form,
                               yeshuv_name_select=yeshuv_name, num_kalfis_22= num_kalfis_22,  kalfis_json=kalfis_json, total_yeshuv_json=knesset_years_yeshuv_json,
                               yeshuv_type_data=yeshuv_type_json
                               )

    return render_template('auto_complete.html', form=yeshuv_form)




@main.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    # optional_yeshuv_list = Yeshuv.query.filter(Yeshuv.yeshuv_name_hebrew.like('%' + str(search) + '%'))
    optional_yeshuv_list = db.session.query(Yeshuv.yeshuv_name_hebrew).filter(
        Yeshuv.yeshuv_name_hebrew.like('%' + str(search) + '%'))
    yeshuvs = []
    for yeshuv in optional_yeshuv_list:
        print(yeshuv)
        yeshuvs.append(dequote_wrapper(yeshuv.yeshuv_name_hebrew))
    return jsonify(matching_results=yeshuvs)


