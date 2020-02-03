#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[2]:


# import io
# import csv
# corpus = io.BytesIO(upload["re_dataset_two_labels.csv"])

dataSet = []

# Import file csv & simpan data set dari csv ke list dataSet
with open("re_dataset_two_labels.csv") as file_csv:
  reader = csv.reader(file_csv, delimiter=",")
  next(reader)
  for data in reader:
    dataSet.append(data)


# In[3]:


stopwords = []

# Import file txt stopwordsindo & simpan data stopwords dari txt ke list stopwords
with open("stopwordsindo.txt") as file_txt:
  reader = csv.reader(file_txt)
  for data in reader:
    stopwords.append(data[0])

stopwords.append('yg')
stopwords.append('user')
stopwords.append('rt')
stopwords.append('url')

print(stopwords)


# In[4]:


# Menyimpan kata dalam kalimat kedalam list 
sentences = []
for data in dataSet:
  sentences.append([data[0], data[1].split()])


# ## REMOVE CHARACTER
# 
# ---

# ### Clean Tahap 1
# 

# In[5]:


# Menghapus karakter simbol tidak penting
bad_char_1 = ['0','1','2','3','4','5','6','7','8','9','0','\\n','-','/',':"D',"'",'"','.','#','?','!','(',')',':',';','%','|','~','*']
clean_sentences_1 = []

for kalimat in sentences:
  words = []
  for kata in kalimat[1]:
    for c in bad_char_1:
      kata = kata.replace(c, '')
    words.append(kata.lower())
  clean_sentences_1.append([kalimat[0], words])


# In[6]:


for data in clean_sentences_1:
  print(data)


# ### Clean Tahap 2

# In[7]:


# Menghapus huruf yang tidak penting
bad_char_2 = ['&gt','fx','xa','xb','xc','xd','xe','xf']
clean_sentences_2 = []

for kalimat in clean_sentences_1:
  words = []
  for kata in kalimat[1]:
    for c in bad_char_2:
      kata = kata.replace(c, '')
    words.append(kata)
  clean_sentences_2.append([kalimat[0], words])


# In[8]:


for data in clean_sentences_2:
  print(data)


# ### Clean Tahap 3

# In[9]:


# Menghapus huruf yang tidak penting
bad_char_3 = ['\\c','\\d','\\e','\\x','\\']
clean_sentences_3 = []

for kalimat in clean_sentences_2:
  words = []
  for kata in kalimat[1]:
    for c in bad_char_3:
      kata = kata.replace(c, '')
    words.append(kata)
  clean_sentences_3.append([kalimat[0], words])


# In[10]:


for data in clean_sentences_3:
  print(data)


# ### Clean Tahap 4

# In[11]:


# Menghapus kata yang tidak penting seperi kata keterangan, kata sambung, dan lainnya.
# Kata tidak penting ini tersimpan dalam stopwordsindo.txt
clean_sentences_4 = []

for kalimat in clean_sentences_3:
  words = []
  for kata in kalimat[1]:
    for c in stopwords:
      if kata == c:
        kata = kata.replace(c, '')
    words.append(kata)
  clean_sentences_4.append([kalimat[0], words])


# In[12]:


for data in clean_sentences_4:
  print(data)


# ### Clean Finish

# In[13]:


# Menghapus spasi dari list kemudian set datanya ke dataSet
dataSet = clean_sentences_4
for data in dataSet:
  while '' in data[1]:
    data[1].remove('')
    
for data in dataSet:
  print(data)


# ## Naive Bayes
# 
# ---

# In[168]:


# Proses klasifikasi menggunakan Naive Bayes

# Fungsi sum_kata befungsi untuk menjumlahkan kata yang kita ingin cari.
# Jika parameter c tidak diisi maka akan menjumlahkan kata yang kita cari di semua kelas
# Jika parameter c diisi maka akan menjumlahkan kata yang kita cari di kelas yang kita tentukan
def sum_kata(k,c=None):
  jum = 0
  for data in dataSet:
    for kata in data[1]:
      if c != None:
        if k in kata and data[0] == c:
          jum += 1
      else:
        if k in kata:
          jum += 1
  return jum

# Fungsi sum_all_kata befungsi untuk menjumlahkan semua kata yang ada pada kelas yang dipilih
def sum_all_kata(c):
  jum = 0
  for data in dataSet:
    if data[0] == c:
      jum += len(data[1])
  return jum

# Fungsi prob_class befungsi untuk menghitung probabilitas dari kelas yang dipilih
def prob_class(c):
  jum = 0
  for data in dataSet:
    if data[0] == c:
      jum += 1
  return jum/len(dataSet)
  
# Fungsi find_probability berfungsi untuk mencari probabilitas dari kalimat yang kita input berdasarkan kelasnya
def find_probability(d,c):
  result = 1
  for k in d:
    result *= ((sum_kata(k,c)+1)/(sum_all_kata(c)+sum_kata(k)))
  return result * prob_class(c)
  
# Fungsi main adalah fungsi utamanya. Didalam fungsi ini memanggil semua fungsi yang sudah didefinisikan diatas
# Hasil dari fungsi ini yaitu menampilkan apakah kalimat yang diinputkan termasuk ke kelas 1 atau kelas 2 berdasarkan hasil perhitungan Naive Bayes
hasil = []
def main():
    kalimat1 = 'disaat cowok berusaha melacak perhatian gue loe lantas remehkan perhatian gue kasih khusus elo basic elo cowok bego'
    kalimat2 = 'dasar jadi manusia anjing banget sih'
    kalimat3 = 'makanya jadi orang jangan tolol'
    kalimat4 = 'babi banget sih jadi orang'
    kalimat5 = 'kerjaan kamu ga becus'
    kalimat6 = 'ehh bangsat ngaca dong'
    kalimat7 = 'emang','dasar','ga','tau','diri'
    kalimat8 = 'kucing', 'i', 'terbuka', 'pintu', 'sikit', 'panjat', 'pagar', 'belajar', 'dr', 'monyet'
    kalimat9 = 'even', 'dah', 'tengok', 'pon,', 'still', 'tersenyum', 'youre', 'so', 'cute'
   
    input = [kalimat1, kalimat2, kalimat3, kalimat4, kalimat5, kalimat6, kalimat7, kalimat8]
    simpan = [kalimat1, kalimat2, kalimat3, kalimat4, kalimat5, kalimat6, kalimat7, kalimat8]
    for i in input:
        hasil_1 = find_probability(i, '1')
        hasil_2 = find_probability(i, '2')
        print(hasil_1)
        print(hasil_2)
    #     return hasil_1, hasil_2
        if hasil_1 > hasil_2:
            print('Label 1')
            temp = ['1', i]
            hasil.append(temp)
        else:
            print('Label 2')
            temp = ['2', i]
            hasil.append(temp)

main()


# In[171]:


num_true = 0
print(hasil)
for j in range(len(dataSet)):
    for i in range(len(hasil)):
        if hasil[i] == dataSet[j]:
            print(hasil[i], dataSet[j])
            num_true= num_true+1


# In[48]:


import nltk


# In[49]:


print(dataSet[1][1])


# In[25]:


kamus = {}
jum_kata_kamus = 0

for j in dataSet: #menghitung kata-kata yang ada berdasarkan corpus dengan menghitung jumlah keseluruhan kata
    for k in j[1]:
        if (k in kamus): #menghitung jumlah kata yang sudah di dalam kamus
            kamus[k] +=1
        else:
            kamus[k] = 1 #menghitung jumlah kata yang belum di dalam kamus
            jum_kata_kamus += 1 
        # mengetahui jumlah seluruh kata

#print(kamus)
print("Jumlah Kata dalam kamus: {}".format(jum_kata_kamus))


# In[28]:


#baru mencari probabilitas unigram 
#memakai dictionary agar membaca lebih gampang berdasarkan key dan value
probabilitas_unigram = {} 

for x in kamus.keys():
    #menghitung jumlah kata yang dihitung dengan jumlah kata keseluruhan 
    probabilitas_unigram[x] = kamus[x]/jum_kata_kamus
print (probabilitas_unigram)


# In[30]:


#menghitung bigram 
kamus_bigram = {}
jum_kata_kamus_bigram = 0

for j in (dataSet): #menghitung kata-kata yang ada berdasarkan corpus dengan menghitung jumlah keseluruhan kata
    for k in range(len(j[1])-1):
        if ((j[1][k],j[1][k+1]) in kamus_bigram): #menghitung jumlah kata yang sudah di dalam kamus
            kamus_bigram[(j[1][k], j[1][k+1])] +=1
        else:
            kamus_bigram[(j[1][k], j[1][k+1])] = 1 #menghitung jumlah kata yang belum di dalam kamus
            # mengetahui jumlah seluruh kata
            jum_kata_kamus_bigram += 1 
        
#print((kamus_bigram))
print("Jumlah bigram dalam kamus: {}".format(jum_kata_kamus_bigram))


# In[31]:


print(kamus_bigram)


# In[32]:


#menghitung probabilitas bigram 

#jumlah dari key (0,0+1)/jumlah(key(0))

probabilitas_bigram = {} 

for x in kamus_bigram.keys():
    #menghitung jumlah kata yang dihitung dengan jumlah kata keseluruhan 
    kata0 = x[0]
    kata1 = x[1]
    probabilitas_bigram[(kata0,kata1)] = kamus_bigram[(kata0,kata1)] / kamus[kata0]
print (probabilitas_bigram)


# In[33]:


# Fungsi menghitung perplexity

import math

def calculate_perplexity(inp, prob_bigram):
    pp = 1
    for i in range(len(inp)-1):
        # Menghindari underflow menggunakan log
        pp *= prob_bigram[(inp[i], inp[i+1])]
    pp = pp ** (1/len(inp))
    return pp


# In[40]:


# Menguji perplexity terhadap test set

# 5 kalimat yang akan dihitung perplexity dan diprediksi kata selanjutnya
kalimat1 = "'disaat', 'cowok', 'berusaha', 'melacak', 'perhatian', 'gue', 'loe', 'lantas', 'remehkan', 'perhatian', 'gue', 'kasih', 'khusus', 'elo', 'basic', 'elo', 'cowok', 'bego'"

# Array dari kalimat
test_set = [kalimat1]

# Proses seluruh kalimat
for row in range(len(test_set)):
    # Membuat tokenizer untuk men-token kalimat
    tokenizer = RegexpTokenizer(r'\w+')
    token_kalimat = tokenizer.tokenize(test_set[row])
    
    # Membuat kamus berisi seluruh kata dalam kalimat dan kamus awal
    kamus_temp = kamus
    for kata in token_kalimat:
        if kata not in kamus:
            kamus_temp[kata]= 1

    # Membuat table probabilitas unigram
    prob_unigram_temp = {}

    for key in kamus_temp.keys():
        prob_unigram_temp[key] = kamus_temp[key]/len(kamus_temp)
        
    # Laplace-smoothed bigram counts
    kamus_bigram_temp = {}
    keys = list(kamus_temp.keys())

    for i in range(len(keys)):
        for j in range(len(keys)):
            if((keys[i], keys[j]) in kamus_bigram):
                kamus_bigram_temp[(keys[i], keys[j])] = kamus_bigram[(keys[i], keys[j])] + 1
            else:
                kamus_bigram_temp[(keys[i], keys[j])] = 1
                
    print("Jumlah bigram : {}".format(len(kamus_bigram_temp)))
    
    # Probabilitas bigram setelah di smoothing
    prob_bigram_temp = {} 

    for x in kamus_bigram_temp.keys():
        #menghitung jumlah kata yang dihitung dengan jumlah kata keseluruhan 
        kata0 = x[0]
        kata1 = x[1]
        prob_bigram_temp[(kata0,kata1)] = kamus_bigram_temp[(kata0,kata1)]/(kamus_temp[kata0] + len(kamus_temp))
        i
    print("Perplexity Kalimat-{} : {}".format(row + 1, calculate_perplexity(token_kalimat, prob_bigram_temp)))


# In[38]:


for i in (kamus_bigram_temp):
da    print(i)


# In[61]:


dataset_smoothing = []
for i in (kamus_bigram_temp):
    dataset_smoothing.append(i)


# In[43]:


for i in dataset_smoothing:
    print(i)


# In[45]:


print(dataset_smoothing[1][1])


# In[ ]:




