import random

kata_rahasia = {
    1: "Python",
    2: "Java",
    3: "Swift",
    4: "Kotlin"
}

jawaban_benar = random.randint(1, 4)

while True:
    print("\nPilih kata rahasia:")
    print("1. Python")
    print("2. Java")
    print("3. Swift")
    print("4. Kotlin")

    try:
        pilihan = int(input("Masukkan pilihan (1-4): "))

        if pilihan == jawaban_benar:
            print("Kamu benar! ")
            break
        elif pilihan in kata_rahasia:
            print("Salah! Coba lagi.")
        else:
            print("Pilihan tidak valid!")

    except ValueError:
        print("Masukkan angka saja!")
