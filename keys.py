from base64 import b64encode

client_id = '953f762da4cd12019ce5ce417475c0'
client_secret = '58c8eaf8340e999ef34ddae709672a'
data = client_id + ':' + client_secret
data_b64_encoded = b64encode(data.encode('utf-8')).decode('utf-8')
b64 = 'Basic ' + data_b64_encoded
