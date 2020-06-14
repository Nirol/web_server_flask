import constants
from queries.yeshuv_knesset import query_yeshuvknesset_by_sn

from . import api
from kalfi_display import get_kalfi_meta_data_for_yeshuv_by_display


# not exposing as api.

# @api.route('/yeshuvs/<int:yeshuv_sn>',  methods=['GET'])
# def get_yeshuv_data_api(yeshuv_sn):
#  yeshuv_knesset_model_data = query_yeshuvknesset_by_sn(yeshuv_sn)
#  display = constants.get_representation_by_kalfi_num(yeshuv_knesset_model_data.Kalfi_Num_22)
#  kalfi_meta_display = get_kalfi_meta_data_for_yeshuv_by_display(yeshuv_sn, display)
#  return yeshuv_json_response(kalfi_meta_display, yeshuv_knesset_model_data)
#
