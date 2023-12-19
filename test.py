# import time
# import datetime

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(10):
#    print(numeros[i])

# # for (i = 0; i < 10; i++) {
# #    printf("%d", numero[i]);
# # }

# n = 0
# while n < 8:
#     if n % 2 == 0:
#         print(n)
#     elif n == 7:
#         print(n)
#     else:
#         print("No es par")
#     n += 1

# import urllib.request, json 
# url = urllib.request.urlopen("https://api.unidadeditorial.es/sports/v1/classifications/current/?site=2&type=10&tournament=0101")
# json_object = json.load(url)
# ranking = json_object['data'][0]['rank']
# for team in ranking:
#     print(team['fullName'], team['standing']['points'])


impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

json_object = {
    "impares": impares,
    "pares": pares
}

print(json_object)

        



   