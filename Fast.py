# Auther : Azim Mahmud
# GitHub : https://github.com/Azim143
# Whatsapp : The Error™
import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
