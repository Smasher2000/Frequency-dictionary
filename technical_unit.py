import string

  def InputStr(): #голова функции
  with open("text.txt", "r") as file_stream: #открывает файл text.txt для чтения
    lines = file_stream.readlines() #создаём список строк для потока file_stream, поток закрывается
  char_table = string.punctuation + "–" + "«" + "»" #создаём таблицу символов, которые будут удалены из словаря
  for i in range(len(lines)):
    table = str.maketrans("", "", char_table)
    lines[i] = lines[i].translate(table) #10-11 строки удаляют символы пунктуации
    lines[i] = lines[i].lower() #делает все буквы строчными
    lines[i] = lines[i].strip() #удаляет пробелы в начале и конце строки
  full_str = " ".join(lines) #после обработки текста, привели к разделению слов пробелами
  return full_str #окончание функции

def break_str(val_str): #голова функции
  val_str = val_str.lower() #делает все буквы строчными
  Words = [] #создаём массив отдельных слов
  tmp_word = "" #создаём пустое слово
  for i in range(len(val_str)):
    if val_str[i] == " ": #если символ пробел, то...
      Words.append(tmp_word) #добавляем слово в конец списка
      tmp_word = "" #обнуляем слово
    else: #иначе...
      tmp_word += val_str[i] #добавляем символ в текущее слово
    if i == len(val_str) - 1: #если мы дошли до конца строки, то...
      Words.append(tmp_word) #добавляем слово в конец списка
  file = open('Vocabulary.txt', 'a') #открываем файл Vocabulary.txt для записи
  for word in Words: #проходимся по всем словам
    file.write(word + "\n") #записываем слова построчно в файл
  file.close() #закрываем файл
  return Words #конец функции

def Rewrite(): #голова функции
  with open("Vocabulary.txt", "r") as file: #открываем файл Vocabulary.txt для чтения
    list_of_words = file.readlines() #создаём список строк для потока file, закрываем
  list_of_words.sort() #сортировка
  with open("Vocabulary.txt", "w") as file: #открываем файл Vocabulary.txt для перезаписи
    for word in list_of_words: #для слов в списке
      if len(word) > 3: #если длина слова больше 3
        file.write(word) #записываем в файл

def Sort(): #голова функции
  with open ("Vocabulary.txt", "r") as rstream: #открываем файл Vocabulary.txt для чтения
    V = rstream.readlines() #создаём список строк для потока rstream, закрываем
  V = [line.rstrip() for line in V] #удаляем лишние пробелы
  V_key = [] #создаём ключ-слово
  V_value = [] #создаём значение-слово
  for i in range(len(V)): 
    if V[i] not in V_key: #если слова нет в ключ-словах
      V_key.append(V[i]) #добавляем в ключ-слова
      V_value.append(1) #добавляем в значение-слова 1
    else: #иначе
      V_value[-1] = V_value[-1] + 1 #увеличиваем значение-слова на 1
  V_dict = dict(zip(V_key, V_value)) #создаём словарь ключ-значение
  sorted_dict = dict(sorted(V_dict.items(), key=lambda x: x[1], reverse=True)) #сортировка по значениям
  for k, v in sorted_dict.items(): #для Ключ-значения проходимся по словарю
    print(f"{k} - {v}") #выводим ключ-значение
