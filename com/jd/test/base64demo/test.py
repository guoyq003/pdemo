import base64
print base64.b64encode('binary\x00string')
print base64.b64encode('admin')
print base64.b64decode('YWRtaW4=')