# استخدام صورة Python كأساس
FROM python:3.9-slim

# تعيين مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ كل الملفات من جهازك إلى الحاوية
COPY . /app

# تثبيت المتطلبات من ملف requirements.txt
RUN pip install -r requirements.txt

# تشغيل التطبيق
CMD ["python", "app.py"]

