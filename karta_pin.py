"""
PLASTIK KARTA PIN-KODI DASTURI
==============================

TALAB (spetsifikatsiya):
    Karta PIN-kodi 3 marta ketma-ket noto'g'ri kiritilsa, karta bloklanadi.

    Karta holatlari:  FAOL -> XATO_1 -> XATO_2 -> BLOKLANGAN

        FAOL    holatida noto'g'ri PIN kiritilsa  -> XATO_1
        XATO_1  holatida noto'g'ri PIN kiritilsa  -> XATO_2
        XATO_2  holatida noto'g'ri PIN kiritilsa  -> BLOKLANGAN

        FAOL, XATO_1 yoki XATO_2 holatida to'g'ri PIN kiritilsa
            -> FAOL (xatolar hisobi nolga tushadi)

        BLOKLANGAN holatda hech qanday PIN qabul qilinmaydi
        (to'g'ri PIN ham). Kartani faqat dasturni qayta ishga tushirib
        "ochish" mumkin.

ISHGA TUSHIRISH:
    python karta_pin.py

TOPSHIRIQ:
    1. Holatlar o'tishi diagrammasini chizing.
    2. Barcha o'tishlarni (va yaroqsiz o'tishni) dasturda sinab ko'ring.
       Eslatma: sinov faqat bitta PIN bilan emas, har xil KETMA-KETLIKLAR
       bilan o'tkazilsin.
    3. Dasturdagi xatoni toping: qanday ketma-ketlikda holat noto'g'ri?
    4. Xatoni tuzating.
"""

TOGRI_PIN = "1234"


class Karta:
    def __init__(self, togri_pin):
        self.togri_pin = togri_pin
        self.xatolar = 0
        self.holat = "FAOL"

    def pin_kiritish(self, pin):
        """PIN ni tekshiradi. To'g'ri bo'lsa True, aks holda False qaytaradi."""
        if self.holat == "BLOKLANGAN":
            print("Karta bloklangan. PIN qabul qilinmaydi.")
            return False

        if pin == self.togri_pin:
            self.holat = "FAOL"
            print("PIN to'g'ri. Xush kelibsiz!")
            return True

        self.xatolar = self.xatolar + 1
        if self.xatolar == 1:
            self.holat = "XATO_1"
        elif self.xatolar == 2:
            self.holat = "XATO_2"
        else:
            self.holat = "BLOKLANGAN"

        if self.holat == "BLOKLANGAN":
            print("PIN noto'g'ri. Karta bloklandi!")
        else:
            qolgan = 3 - self.xatolar
            print(f"PIN noto'g'ri. Qolgan urinishlar: {qolgan}")
        return False


def main():
    karta = Karta(TOGRI_PIN)

    print("=== Plastik karta ===")
    print(f"(Sinov uchun to'g'ri PIN: {TOGRI_PIN})")
    print("Chiqish uchun 'q' harfini kiriting.")
    print()
    print(f"Karta holati: {karta.holat}")

    while True:
        pin = input("PIN-kodni kiriting: ").strip()
        if pin.lower() == "q":
            print("Dastur tugadi.")
            break

        karta.pin_kiritish(pin)
        print(f"Karta holati: {karta.holat}")
        print()


if __name__ == "__main__":
    main()
