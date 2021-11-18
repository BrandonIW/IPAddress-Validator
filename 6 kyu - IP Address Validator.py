# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid
# if they consist of four octets, with values between 0 and 255, inclusive.

# This regex also works
# ^([12])?((?(?<=2)[0-5]|[0-9]))?((?(?<=25)[0-5]|[0-9])){1}$
import re
def is_valid_IP(strng):
    regex = re.compile(r'(^([12])?((?<=2)[0-5]|(?<!2)[0-9])?((?<=25)[0-5]|(?<!25)[0-9])?$)')
    oct_list = [octet for octet in strng.split(".")]
    return False if len(oct_list) != 4 else all(map(lambda octet: bool(regex.fullmatch(octet)), oct_list))


print(is_valid_IP("192.168.0.256"))

