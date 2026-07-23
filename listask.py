# aylar = ("Yanvar", "Fevral", "Mart")
# aylar_list = list(aylar)
# aylar_list.append("Aprel")
# aylar = tuple(aylar_list)
# print("Aylar:", aylar)


# qiymetler = [35, 67, 60, 12, 46, 91, 54, 40]
# qiymetler.sort(reverse=True) 
# kesilenler = [i for i in qiymetler if i < 51]
# print("Kəsilmiş tələbələrin sayısı:", len(kesilenler))
# qiymetler.pop(0)
# qiymetler.pop()  
# orta_qiymet = sum(qiymetler) / len(qiymetler)
# print("Qalan:", qiymetler)
# print("Orta:", orta_qiymet)


# ededler = [1, 2, 2, 3, 4, 4, 4, 5, 6, 1]
# unikal_ededler = []
# for i in ededler:
#     if i not in unikal_ededler:
#         unikal_ededler.append(i)
# print("Exercise 13 (Unikal ededler):", unikal_ededler)


# **Sevimli filmlərin siyahısı**

# 3 sevimli filmin adından ibarət filmler adlı bir list yarat.

# Siyahının sonuna yeni bir film əlavə et.

# Birinci filmi (index 0) başqa bir filmə dəyişdir.

# Siyahıda neçə film olduğunu `len()` ilə çap et.


# filmler = ["Inception", "The Matrix", "Interstellar"]
# filmler.append("The Dark Knight")
# filmler[0] = "The Godfather"
# enum_filmler = enumerate(filmler, start=1)
# print("Sevimli filmlər:")
# for index, film in enum_filmler:
#     print(f"{index}. {film}")
# print("Siyahıda neçə film var:", len(filmler))


# melumat = ("Mustafa", 26, "Baku")
# print("Ad:", melumat[0])
# print("Yas:", melumat[1])
# print("Seher:", melumat[2])
# print("Tuple uzunlugu:", len(melumat))
# for i, element in enumerate(melumat):
#     print(f"{i}. {element}")



# elifba = ["a", "b", "c", "d", "e", "f", "g", "h"]
# print("İlk 4 hərf:", elifba[:4])
# print("Son 3 hərf:", elifba[-3:])
# print("Ortadakı hərf:", elifba[2:5])



# temperaturalar = [0, 20, 37, 100]
# fahrenheit = [C * 9/5 + 32 for C in temperaturalar]
# print("Fahrenheit dərəcələri:", fahrenheit)