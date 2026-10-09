"""
DO'KON CHEGIRMASI DASTURI
=========================

TALAB (spetsifikatsiya):
    Chegirma foizi uchta narsaga bog'liq: mijoz a'zomi, buyurtma summasi
    va promokod bormi.

    Asosiy chegirma:
        summa 500 000 so'm yoki undan ko'p, mijoz a'zo        -> 15 %
        summa 500 000 so'm yoki undan ko'p, mijoz a'zo emas   -> 10 %
        summa 500 000 so'mdan kam,          mijoz a'zo        ->  5 %
        summa 500 000 so'mdan kam,          mijoz a'zo emas   ->  0 %

    Promokod bo'lsa, asosiy chegirmaga yana +5 % qo'shiladi
    (yuqoridagi to'rt holatning har birida).

ISHGA TUSHIRISH:
    python chegirma.py

TOPSHIRIQ:
    1. Qaror jadvalini tuzing: 3 ta shart (a'zo, summa, promokod) -> 8 ta qoida.
    2. Har bir qoida uchun dasturni sinab ko'ring.
    3. Dasturdagi xatoni toping: qaysi holatda chegirma noto'g'ri chiqyapti?
    4. Xatoni tuzating.
"""

CHEGARA = 500000   # so'm


def chegirma_hisobla(a_zo, summa, promokod):
    """Chegirma foizini qaytaradi."""
    if summa >= CHEGARA:
        if a_zo:
            foiz = 15
        else:
            foiz = 10
        if promokod:
            foiz = foiz + 5
    else:
        if a_zo:
            foiz = 5
            if promokod:
                foiz = foiz + 5
        else:
            foiz = 0
    return foiz


def ha_yoq_sora(savol):
    """'ha' yoki "yo'q" javobini oladi. ha -> True, yo'q -> False."""
    while True:
        javob = input(savol + " (ha/yo'q): ").strip().lower()
        if javob in ("ha", "h"):
            return True
        if javob in ("yo'q", "yoq", "y"):
            return False
        print("Iltimos, 'ha' yoki 'yo'q' deb javob bering.")


def summa_sora():
    """Buyurtma summasini (so'mda, butun son) oladi."""
    while True:
        matn = input("Buyurtma summasi (so'm): ").replace(" ", "")
        if matn.isdigit():
            return int(matn)
        print("Iltimos, summani raqam bilan kiriting (masalan: 450000).")


def pul(son):
    """123456 -> '123 456' ko'rinishida chiroyli yozadi."""
    return f"{son:,}".replace(",", " ")


def main():
    print("=== Do'kon chegirmasi ===")
    print("Chiqish uchun Ctrl+C ni bosing.")

    while True:
        print()
        a_zo = ha_yoq_sora("Mijoz a'zomi?")
        summa = summa_sora()
        promokod = ha_yoq_sora("Promokod bormi?")

        foiz = chegirma_hisobla(a_zo, summa, promokod)
        chegirma_summa = summa * foiz // 100
        tolov = summa - chegirma_summa

        print()
        print(f"Chegirma: {foiz} %")
        print(f"Chegirma summasi: {pul(chegirma_summa)} so'm")
        print(f"To'lanadigan summa: {pul(tolov)} so'm")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nDastur tugadi.")
