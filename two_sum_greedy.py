def two_sum_greedy(angka, target):
    angka_urut = sorted(angka, reverse=True)

    pasangan = []
    digunakan = set()

    for i in range(len(angka_urut)):
        if i in digunakan:
            continue

        for j in range(i + 1, len(angka_urut)):
            if j in digunakan:
                continue

            if angka_urut[i] + angka_urut[j] == target:
                pasangan.append((angka_urut[i], angka_urut[j]))
                digunakan.add(i)
                digunakan.add(j)
                break

    return pasangan

angka = list(map(int, input("Masukkan daftar angka: ").split()))
target = int(input("Masukkan angka target: "))

hasil = two_sum_greedy(angka, target)

print("\nHasil pencarian:")

if hasil:
    for nomor, (a, b) in enumerate(hasil, start=1):
        print(f"{nomor}. {a} + {b} = {target}")
else:
    print("Tidak ditemukan pasangan angka.")