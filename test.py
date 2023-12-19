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

import urllib.request, json 
with urllib.request.urlopen("https://api.unidadeditorial.es/sports/v1/classifications/current/?site=2&type=10&tournament=0101") as url:
    json_object = json.load(url)
    ranking = json_object['data'][0]['rank']
    for team in ranking:
        print(team['fullName'], team['standing']['points'])


        



   