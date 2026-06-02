<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=240&color=0:7c3aed,100:0f172a&text=VoiceScribe&fontColor=ffffff&fontSize=60&fontAlignY=40&desc=Audio%20%26amp;%20Microphone%20Speech%20Transcriber%20%7C%20CODE%20RAH&descAlignY=63&animation=twinkling" width="100%" />

# 🎙️ تبدیل صدا به متن با هوش مصنوعی گوگل

### توسعه داده شده توسط تیم تخصصی CODE RAH 💻

</div>

---

# 🛑 بیانیه کپی‌رایت و مالکیت معنوی (مهم)

> ⚠️ **تذکر جدی برای همکاران و اساتید:**  
> این کد برای اولین بار در سطح اینترنت منتشر می‌شود و توسط **امیرفرخانی موسس آکادمی آنلاین کدراه** پیاده‌سازی و کدنویسی شده است.  
> هرگونه استفاده، برداشته شدن سورس‌کد، تولید محتوای ویدیویی مشابه در سطح وب و آموزش آن **منحصراً مشروط به ذکر منبع و نام CODE RAH** است.  
> در غیر این صورت هیچ‌گونه رضایتی وجود نداشته و عواقب آن متوجه فرد خاطی خواهد بود.

---

# 📝 درباره پروژه

**VoiceScribe** یک نرم‌افزار دسکتاپ با رابط گرافیکی زیبا است که فایل‌های صوتی `MP3`/`WAV` را به متن فارسی تبدیل می‌کند. همچنین می‌توانید مستقیماً از میکروفن صحبت کنید و صدایتان بلافاصله به متن تبدیل و ذخیره شود.

---

# ⚡ ویژگی‌ها

- 🎵 **پردازش فایل صوتی** — پشتیبانی از `MP3` و `WAV`
- 🔪 **تقسیم هوشمند صدا** — پردازش chunk به chunk با نمایش پیشرفت
- 🎙️ **ضبط میکروفن** — شروع/توقف ضبط با دکمه اختصاصی
- 📄 **ذخیره خودکار متن** — ذخیره نتیجه در فایل TXT و باز شدن آن
- 🌀 **رابط گرافیکی متحرک** — نمایش GIF پس‌زمینه در پنجره اصلی
- 🔤 **زبان فارسی** — تشخیص گفتار با Google API به زبان `fa-IR`

---

# 🚀 راهنمای نصب و اجرا

## 📥 مرحله اول: دانلود پروژه

روی دکمه سبز **Code** کلیک و **Download ZIP** را انتخاب کنید، سپس از حالت فشرده خارج نمایید.

---

## 🧩 مرحله دوم: نصب Python

آخرین نسخه Python را نصب کرده و هنگام نصب این گزینه را فعال کنید:
```text
Add Python to PATH

```
## 📦 مرحله سوم: نصب پکیج‌ها

bash
pip install customtkinter pillow speechrecognition pydub

> ⚠️ برای پردازش `MP3` باید **FFmpeg** روی سیستم نصب باشد و در PATH قرار گرفته باشد.

---

## ▶️ مرحله چهارم: اجرا

فایل‌های `Shocked13.gif` و `mic (1).png` را کنار `main.py` قرار دهید، سپس:

bash
python main.py

---

# 📂 ساختار پروژه


VoiceScribe/
├── main.py
├── Shocked13.gif
└── mic (1).png

---

# 🖥️ نحوه استفاده

| روش | توضیح |
|-----|-------|
| 🎵 دکمه نت موزیک | انتخاب فایل `MP3`/`WAV` از سیستم و شروع transcribe |
| 🎙️ دکمه میکروفن | شروع ضبط از میکروفن |
| ⏹️ دکمه توقف | پایان ضبط و ذخیره متن در فایل TXT |
| 📊 نوار پیشرفت | نمایش درصد پردازش فایل صوتی |

---

# ⚡ فناوری‌های استفاده‌شده

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-GUI-7c3aed?style=for-the-badge)
![Google Speech API](https://img.shields.io/badge/Google%20Speech-API-4285F4?style=for-the-badge&logo=google&logoColor=white)
![pydub](https://img.shields.io/badge/pydub-Audio-f59e0b?style=for-the-badge)

</div>

---

# 🧠 درباره تیم CODE RAH

تیم **CODE RAH** یک گروه تخصصی در حوزه‌های پیشرفته فناوری است:

- 🤖 هوش مصنوعی و بینایی ماشین — `OpenCV` `YOLO` `ML`
- 💻 برنامه‌نویسی — `Python` `C#` `Java` `JavaScript`
- 🔒 امنیت سایبری — `Ethical Hacking` `Kali Linux`
- ⚙️ اینترنت اشیاء — `Arduino` `Raspberry Pi`

---

<div align="center">

# 💻 CODE RAH

### کدنویسی فقط نوشتن برنامه نیست؛ ساختن آینده است.

⭐ اگر از این پروژه خوشتان آمد، ستاره فراموش نشه ⭐

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&height=120&color=0:0f172a,100:7c3aed&section=footer" width="100%" />
`
