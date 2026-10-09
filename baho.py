"""
BAHO QO'YISH DASTURI
====================

TALAB (spetsifikatsiya):
    Talabaning balli (0 dan 100 gacha, butun son) bo'yicha baho qo'yiladi:

        0  - 59   ->  2 (qoniqarsiz)
        60 - 69   ->  3 (qoniqarli)
        70 - 89   ->  4 (yaxshi)
        90 - 100  ->  5 (a'lo)

    Ball 0 dan kichik yoki 100 dan katta bo'lsa, baho qo'yilmaydi
    va "Xato: ball 0 dan 100 gacha bo'lishi kerak" deb xabar beriladi.

ISHGA TUSHIRISH:
    python baho.py

TOPSHIRIQ:
    1. Dasturni ma'ruzadagi usullar (ekvivalent bo'laklar va chegaraviy
       qiymatlar tahlili) bilan sinab ko'ring.
    2. Dasturdagi xatoni toping: qaysi ball uchun noto'g'ri baho chiqyapti?
    3. Xatoni tuzating.
"""

BAHO_NOMLARI = {
    2: "qoniqarsiz",
    3: "qoniqarli",
    4: "yaxshi",
    5: "a'lo",
}


def baho_qoy(ball):
    """Ballga qarab bahoni qaytaradi. Ball noto'g'ri bo'lsa, None qaytaradi."""
    if ball < 0 or ball > 100:
        return None

    if ball <= 59:
        return 2
    elif ball <= 70:
        return 3
    elif ball <= 89:
        return 4
    else:
        return 5


def main():
    print("=== Baho qo'yish dasturi ===")
    print("Chiqish uchun 'q' harfini kiriting.")
    print()

    while True:
        matn = input("Ballni kiriting (0-100): ").strip()

        if matn.lower() == "q":
            print("Dastur tugadi.")
            break

        try:
            ball = int(matn)
        except ValueError:
            print("Xato: butun son kiriting.")
            continue

        baho = baho_qoy(ball)
        if baho is None:
            print("Xato: ball 0 dan 100 gacha bo'lishi kerak.")
        else:
            print(f"Baho: {baho} ({BAHO_NOMLARI[baho]})")


if __name__ == "__main__":
    main()
