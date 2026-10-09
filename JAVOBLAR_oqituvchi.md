# JAVOBLAR — faqat o'qituvchi uchun

> **Diqqat:** bu faylni talabalar GitHub repozitoriyasiga **qo'shmang**.
> Repoga faqat `baho.py`, `chegirma.py`, `karta_pin.py`, `login.py` joylanadi.

Har bir dasturda **aynan bitta** xato bor. Xato dasturning o'z spetsifikatsiyasidan
(fayl boshidagi `TALAB` qismi) chetga chiqish sifatida yozilgan, shuning uchun talaba
"to'g'ri javob nima?" degan savolga fayl ichidan javob topa oladi.

Tekshiruv: har bir dastur etalon (to'g'ri) variant bilan solishtirilgan.
Farq faqat quyida ko'rsatilgan joylarda chiqadi, boshqa hech qayerda yo'q.

---

## 1. `baho.py` — Baho qo'yish

**Texnika:** chegaraviy qiymatlar tahlili (BVA)

**Xato (41-qator):**

```python
elif ball <= 70:      # bo'lishi kerak: ball <= 69
    return 3
```

| Kirish | Kutilgan | Dastur beradi |
|--------|----------|---------------|
| 70     | 4        | **3** ❌      |

Boshqa barcha ballar (−50 dan 150 gacha tekshirilgan) to'g'ri.

**Nima uchun topish qiyin:** ekvivalent bo'lakning o'rtadagi vakili (masalan 65 yoki 75)
xatoni **o'tkazib yuboradi**. Faqat chegara qiymatlari (59, 60, 69, **70**, 89, 90) topadi.

**Tuzatish:** `elif ball <= 69:`

**Talabaga savol:** "Nega 65 va 75 bilan sinab xatoni topa olmadingiz?"

---

## 2. `chegirma.py` — Do'kon chegirmasi

**Texnika:** qaror jadvali (decision table)

**Xato (46-qator):** a'zo emas + summa < 500 000 shoxida promokod hisobga olinmagan.

```python
else:
    foiz = 0      # bo'lishi kerak: foiz = 5 if promokod else 0
```

8 qoidadan **faqat bittasi** noto'g'ri:

| # | A'zo | Summa ≥ 500 000 | Promokod | Kutilgan | Dastur |
|---|------|-----------------|----------|----------|--------|
| 1 | ha   | ha  | ha  | 20 | 20 |
| 2 | ha   | ha  | yo'q | 15 | 15 |
| 3 | yo'q | ha  | ha  | 15 | 15 |
| 4 | yo'q | ha  | yo'q | 10 | 10 |
| 5 | ha   | yo'q | ha  | 10 | 10 |
| 6 | ha   | yo'q | yo'q | 5 | 5 |
| 7 | yo'q | yo'q | ha  | **5** | **0** ❌ |
| 8 | yo'q | yo'q | yo'q | 0 | 0 |

Misol: a'zo emas, 300 000 so'm, promokod bor → 5 % bo'lishi kerak, dastur 0 % beradi.

**Nima uchun topish qiyin:** 7 ta qoida to'g'ri. Talaba hamma 8 kombinatsiyani
sinamasa, xato ko'rinmaydi. Ayniqsa "a'zo emas" holatini promokod bilan sinamasa.

**Tuzatish:**
```python
else:
    foiz = 0
    if promokod:
        foiz = foiz + 5
```

**Talabaga savol:** "Qaror jadvalida nechta qoida bor edi? Siz nechtasini sinadingiz?"

---

## 3. `karta_pin.py` — PIN-kod va holatlar o'tishi

**Texnika:** holatlar o'tishi bo'yicha testlash (state transition)

**Xato (49–51-qatorlar):** to'g'ri PIN kiritilganda xatolar hisobi nolga tushmaydi.

```python
if pin == self.togri_pin:
    self.holat = "FAOL"
    # YETISHMAYAPTI:  self.xatolar = 0
    print("PIN to'g'ri. Xush kelibsiz!")
    return True
```

Xato faqat ma'lum **ketma-ketlikda** ko'rinadi (X = noto'g'ri PIN, T = to'g'ri PIN):

| Ketma-ketlik | Kutilgan oxirgi holat | Dastur beradi |
|--------------|-----------------------|---------------|
| X, T, X      | XATO_1                | **XATO_2** ❌ |
| X, T, X, X   | XATO_2                | **BLOKLANGAN** ❌ |
| X, X, T, X   | XATO_1                | **BLOKLANGAN** ❌ (to'g'ri PIN dan keyin 1 ta xato bilan bloklanadi!) |

Eng qisqa xato ketma-ketlik: **X → T → X** (3 ta kiritish).

Faqat noto'g'ri PIN lar yoki faqat to'g'ri PIN lar bilan sinasa, xato **ko'rinmaydi**.
Xato faqat "xato → to'g'ri → yana xato" sxemasi bo'lganda chiqadi
(uzunligi 7 gacha bo'lgan barcha ketma-ketliklar etalon bilan solishtirilgan).

**Tuzatish:** to'g'ri PIN shoxiga `self.xatolar = 0` qo'shish.

**Talabaga savol:** "Nega har bir o'tishni alohida sinash yetarli bo'lmadi?
Xato qaysi *ikki* o'tish orasidagi bog'liqlikda yashiringan?"

---

## 4. `login.py` — Tizimga kirish (use case)

**Texnika:** use case testlash (muqobil oqim A1)

**Xato (38-qator):** faqat login bo'shligi tekshiriladi, parol bo'shligi tekshirilmaydi.

```python
if login == "":          # bo'lishi kerak: if login == "" or parol == "":
```

| Login | Parol | Kutilgan | Dastur beradi |
|-------|-------|----------|---------------|
| student1 | *(bo'sh)* | Login va parolni to'ldiring! | **Parol noto'g'ri!** ❌ |
| yoq_odam | *(bo'sh)* | Login va parolni to'ldiring! | **Bunday foydalanuvchi topilmadi!** ❌ |
| *(bo'sh)* | har qanday | Login va parolni to'ldiring! | to'g'ri ✅ |

Asosiy oqim, A2 va A3 to'g'ri ishlaydi.

**Nima uchun topish qiyin:** A1 oqimi spetsifikatsiyada "login **yoki** parol" deb yozilgan.
Talaba faqat "ikkalasi bo'sh" holatini sinasa, xato ko'rinmaydi.

**Tuzatish:** `if login == "" or parol == "":`

**Talabaga savol:** "A1 oqimi uchun nechta alohida test kerak? (Javob: 3 — login bo'sh,
parol bo'sh, ikkalasi bo'sh.)"

---

## Xulosa jadvali

| Dastur | Texnika | Xato qatori | Qanday topiladi |
|--------|---------|-------------|-----------------|
| baho.py | BVA | 41 | ball = **70** |
| chegirma.py | Qaror jadvali | 46 | a'zo emas + <500 000 + **promokod** |
| karta_pin.py | Holatlar o'tishi | 49–51 | **xato → to'g'ri → xato** |
| login.py | Use case | 38 | login bor + **parol bo'sh** |

## Baholash bo'yicha tavsiya (ixtiyoriy)

- Xatoni topdi va aniq kirish ma'lumotini ko'rsatdi — to'liq ball.
- Xatoni topdi, lekin tuzatmadi yoki sababini tushuntirolmadi — qisman ball.
- Faqat "dastur ishlayapti" deb yozdi — talaba texnikani qo'llamagan (chegaraviy
  qiymat / barcha kombinatsiya / ketma-ketlik / muqobil oqim).

## Keyingi laboratoriya uchun (ixtiyoriy)

Dasturlar import qilinadigan qilib yozilgan (`from baho import baho_qoy` va h.k.), shuning
uchun keyingi darsda integration va system testlar topshirig'ini shu to'rtta modul
asosida berish mumkin: modullarni bitta menyuga ulash, ssenariylar jadvalini tuzish
va natijalarni hujjatlashtirish.
