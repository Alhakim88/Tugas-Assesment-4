kata_rahasia = "python"

while True:
    tebakan = input("Tebak kata rahasianya: ")

    if tebakan == kata_rahasia:
        print("Kamu benar!")
        break
    else:
        print("Salah! Coba lagi.")
