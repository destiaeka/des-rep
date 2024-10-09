import random

def main():
  print("Yukkk, mulai permainan tebak angka")
  print("===MULAI YUK===")
  # Tentukan batas atas dan bawah untuk tebakan
  angka_maksimum = 100
  angka_minimum = 1


  # Memilih angka acak menggunakan fungsi 'randint' yang disediakan oleh modul 'random'
  angka_rahasia = random.randint(angka_minimum, angka_maksimum)

  # Memberikan kesempatan kepada pemain untuk menebak
  tebakan = 0
  while tebakan != angka_rahasia:
    tebakan = int(input(f"Masukkan tebakan Anda antara {angka_minimum} dan {angka_maksimum}: "))

    if tebakan < angka_rahasia:
      print("Yah, tebakanmu terlalu rendah")
    elif tebakan > angka_rahasia:
      print("Aduh, ketinggian nih")
    else:
      print("Nah, ini dia angka rahasianya!!")
  # Output apabila angka tebakan betul
  print(f"Jadi angka rahasianya tuh {angka_rahasia}")

if __name__ == "__main__":
  main()

#ini hanya percobaan

