from enum import Enum

KNESSETS_LIST = ["18", "19", "20", "21", "22"]
KALFI_METADATA_COUNT = 10543
NUMBER_KALFI_DISPLAY = 5
class KalfiDisplayType(Enum):
    All_Kalfi = 0
    Top_N_Kalfi = 1

def get_representation_by_kalfi_num(kalfi_num: int) -> KalfiDisplayType:
    if kalfi_num <=10:
        return KalfiDisplayType.All_Kalfi
    else:
        return KalfiDisplayType.Top_N_Kalfi




class KnessetVars(Enum):

    Kalfi_Num = 1
    BZB = 2
    Voters = 3
    Error_Voters = 4
    vote_percent = 5
    Avg_BZB = 6