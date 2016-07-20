import base64, zlib, os
with open('es.exe', 'rb') as f:
    print base64.encodestring(zlib.compress(f.read()))+"*"+str(os.path.getsize(os.path.join(os.getcwd(), 'es.exe')))