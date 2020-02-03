import re

from models import Kalfi


def _clean_address(address):
    s=address
    s=s.strip()
    if s.startswith('"') and s.endswith('"'):
        s=s[1:-1]
        s=s.strip()
    s = re.sub(r"(\")\1*", r'\1', s)
    # if address != s:
    #     print("address={} ||| to={}".format(address,s))
    return s


def clean_kalfi_hebrew_texts(kalfi_meta: Kalfi) -> None:
    address = kalfi_meta.get_address()
    location = kalfi_meta.get_location()
    clean_address = _clean_address(address)
    clean_location = _clean_address(location)
    kalfi_meta.update_hebrew_texts(clean_address, clean_location)