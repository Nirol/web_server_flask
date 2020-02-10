from app import create_app, db



# used to clean hebrew texts
from db_queries import query_kalfi_metadata_all
import re
from models import Kalfi


def __clean_address(address):
    s=address
    s=s.strip()
    if s.startswith('"') and s.endswith('"'):
        s=s[1:-1]
        s=s.strip()
    s = re.sub(r"(\")\1*", r'\1', s)
    # if address != s:
    #     print("address={} ||| to={}".format(address,s))
    return s


def __clean_kalfi_hebrew_texts(kalfi_meta: Kalfi) -> None:
    address = kalfi_meta.get_address()
    location = kalfi_meta.get_location()
    clean_address = __clean_address(address)
    clean_location = __clean_address(location)
    if address != clean_address:
        if location != clean_location:
            kalfi_meta.update_location(clean_location)
            kalfi_meta.update_address(clean_address)
        else:
            kalfi_meta.update_address(clean_address)
    elif location != clean_location:
        kalfi_meta.update_location(clean_location)



def clean_kalfi_meta_hebrew():
    kalfi_meta_data_list = query_kalfi_metadata_all()
    for knesset_meta in kalfi_meta_data_list:
        __clean_kalfi_hebrew_texts(knesset_meta)

