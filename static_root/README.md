# 3d_models.uz

Proyektni ishlatish uchun:

1) Kompyuteringizga Python 3.8.6 o'rnatilgan bo'lishi kerak. Buning u.n https://www.python.org/ftp/python/3.8.6/python-3.8.6-amd64.exe(Windows X64 versiyali OS lar uchun) yoki https://www.python.org/ftp/python/3.8.6/python-3.8.6.exe(Windows X86 versiyali OS lar uchun) o'rnatib olishingiz kerak bo'ladi. Pythonni to'g'ri o'rnatishni https://phoenixnap.com/kb/how-to-install-python-3-windows shu saytdan ko'rib olishingiz mumkin bo'ladi;
2) Undan keyin kompyuteringizga ushbu proyektni yuklab olasiz. Keyin esa shu proyektni Visual Studio Code(yoki boshqa redaktor) yordamida ochib olasiz.
3) cmd(командная строка) yoki Visual Studio Codeni(yoki qaysi redaktordan foydalanayotgan bo'lsangiz o'sha redaktorni) terminalini ochib olib terminalga pip install virtualenv komandasini yozib enter tugmasini bosishingiz kerak;
4) virtualenv venv komandasi orqali virtualenvning obyektini yaratishimiz kerak bo'ladi;
5) venv\Scripts\activate(ubuntudagilar source venv/bin/activate) ushbu komanda orqali virtualenvning obyektini aktiv qilishingiz kerak;
6) pip install -r requirements.txt ushbu komanda yordamida barcha kerakli bo'lgan paketlarni o'rnatib olinadi(kerakli paketlar yozilgan faqatgina ushbu komandani terminalga yoki cmd ga yozsangiz kifoya);
7) python manage.py makemigrations
8) python manage.py migrate
9) python manage.py runserver
10) Bu uchala komandani ishlatganimizdan keyin terminalni(yoki cmdni) o'chirmagan holda browserni ochib http://127.0.0.1:8000/ manziliga kirish kerak. Proyekt mana shu yerda ishlaydi(hozircha lokalniyda)
11) Frontendchilar js yoki css fayllarga o'zgartirish kiritgandan keyin terminalda(yoki cmd da) Ctrl+C(Ctrl+Z) tugmasini bosib qayta python manage.py runserver komandasini yozish orqali qilgan o'zgarishlaringizni ko'rishingiz mumkin bo'ladi.
