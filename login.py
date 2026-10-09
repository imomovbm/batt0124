"""
TIZIMGA KIRISH (LOGIN) DASTURI
==============================

TALAB (spetsifikatsiya) - "Tizimga kirish" use case'i:

    Asosiy oqim:
        Foydalanuvchi login va parolni to'g'ri kiritadi
        -> "Xush kelibsiz, <login>!"

    Muqobil oqimlar:
        A1. Login yoki parol (yoki ikkalasi) bo'sh
            -> "Login va parolni to'ldiring!"
        A2. Bunday login ro'yxatda yo'q
            -> "Bunday foydalanuvchi topilmadi!"
        A3. Login bor, lekin parol noto'g'ri
            -> "Parol noto'g'ri!"

ISHGA TUSHIRISH:
    python login.py

TOPSHIRIQ:
    1. Use case'ning har bir oqimi (asosiy + A1, A2, A3) uchun test
       ssenariysi yozing (kirish ma'lumoti va kutilgan natija).
    2. Ssenariylarni dasturda bajarib, natijani kutilgan natija bilan solishtiring.
    3. Dasturdagi xatoni toping: qaysi ssenariyda xabar noto'g'ri?
    4. Xatoni tuzating.
"""

FOYDALANUVCHILAR = {
    "student1": "Parol#2026",
    "student2": "Qwerty!77",
}


def kirish(login, parol):
    """Login va parolni tekshiradi, foydalanuvchiga xabar qaytaradi."""
    if login == "":
        return "Login va parolni to'ldiring!"

    if login not in FOYDALANUVCHILAR:
        return "Bunday foydalanuvchi topilmadi!"

    if FOYDALANUVCHILAR[login] != parol:
        return "Parol noto'g'ri!"

    return f"Xush kelibsiz, {login}!"


def main():
    print("=== Tizimga kirish ===")
    print("Sinov uchun foydalanuvchilar:")
    for login, parol in FOYDALANUVCHILAR.items():
        print(f"    login: {login}   parol: {parol}")

    while True:
        print()
        login = input("Login: ").strip()
        parol = input("Parol: ").strip()

        print(kirish(login, parol))

        javob = input("Yana urinib ko'rasizmi? (ha/yo'q): ").strip().lower()
        if javob not in ("ha", "h"):
            print("Dastur tugadi.")
            break


if __name__ == "__main__":
    main()
