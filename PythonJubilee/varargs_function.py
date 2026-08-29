def salamPagi(*suneo):
    print("Halo!")
    print("Selamat Pagi ", *suneo)  # tuple dibongkar kalau dengan asterik *
    print("selamat siang ", suneo)  # tuple tidak dibongkar, dipanggil saja


salamPagi("Rohmat ", "Edi ", "Siti ")
