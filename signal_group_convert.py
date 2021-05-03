import base64
import sys
def b64_to_hex_str(group_id):
    return base64.b64decode(group_id.encode()).hex()
group_id = sys.argv[1]
print(b64_to_hex_str(group_id))