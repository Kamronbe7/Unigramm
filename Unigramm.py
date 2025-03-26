import re

gap = "Bitimga ko'ra, birinchi reaktor 2030 yilda, keyingi 5 yilda esa yana bir nechtasi ishga tushiriladi. a'lo g'oz"

unigram = re.sub(r"[^\w\s']", '', gap).split()
bigram = [unigram[i] + ' ' + unigram[i + 1] for i in range(len(unigram) - 1)]

print("Unigram ro'yxati:", unigram)
print("Bigram ro'yxati:", bigram)
