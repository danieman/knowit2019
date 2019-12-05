cipher = 'tMlsioaplnKlflgiruKanliae' \
         'beLlkslikkpnerikTasatamkD' \
         'psdakeraBeIdaegptnuaKtmte' \
         'orpuTaTtbtsesOHXxonibmkse' \
         'kaaoaKtrssegnveinRedlkkkr' \
         'oeekVtkekymmlooLnanoKtlst' \
         'oepHrpeutdynfSneloietbol'
length = len(cipher)
mid = length // 2
cipher = list(cipher)

for i in range(0, mid, 3):
    cipher[i:i+3], cipher[-(i+1):-(i+4):-1] = cipher[-(i+1):-(i+4):-1][::-1], cipher[i:i+3][::-1]

for i in range(0, length, 2):
    cipher[i], cipher[i+1] = cipher[i+1], cipher[i]

cipher[:mid], cipher[mid:] = cipher[mid:], cipher[:mid]

print(''.join(cipher))