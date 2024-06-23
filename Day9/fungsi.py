def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

angka = 5
print("Faktorial dari", angka, "adalah", faktorial(angka))
