import base64
def safe_b64decode(str):
	i = len(str)
	while i%4 != 0:
		str += '='
		i = len(str)
	return base64.b64decode(str)
print safe_b64decode('YWJjZA')