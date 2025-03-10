nama = str(input("Nama anda: "))
nik = int(input("Nik anda: "))
status = str(input("Status anda: "))

    #jika status pegawai tetap
if status == "pegawai tetap" :
    gaji_pokok = 1000000
    golongan = str(input("Golongan anda (A/B/C): "))
    if golongan == "A" or golongan == "a":
        bonus = 200000
    elif golongan == "B" or golongan == "b":
        bonus = 400000  
    elif golongan == "C" or golongan == "c":
        bonus = 600000
    else : raise ValueError("golongan tidak valid")
    gaji_total = gaji_pokok + bonus
    print("<<< Rincian Gaji >>>")
    print(f"Nama :", nama)
    print(f"NIK :", nik)
    print(f"Status :", status)
    print(f"Golongan :", golongan)
    print("Gaji pokok: ", gaji_pokok)
    print("Bonus: ", bonus)
    print("Gaji total: ", gaji_total)

   #jika status honor 
elif status == "honor" :
    gaji_pokok_honor= 750000
    golongan = str(input("golongan anda: "))
    if golongan == "A" or golongan == "a":
        bonus = 150000
        gaji_pokok_honor += bonus
    elif golongan == "B" or golongan == "b" :
        bonus = 275000
        gaji_pokok_honor += bonus
    elif golongan == "C" or golongan == "c" :
        bonus = 480000
    else : raise ValueError("golongan tidak valid")
    gaji_total_honor = gaji_pokok_honor + bonus
    print("<<< rincian gaji >>>")
    print(f"Nama :", nama)
    print(f"NIK :", nik)
    print(f"Status :", status)
    print(f"Golongan :", golongan)
    print("Gaji pokok: ", gaji_pokok_honor)
    print("Bonus: ", bonus)
    print("Gaji total: ", gaji_total_honor)
else :
    print("status tidak valid")