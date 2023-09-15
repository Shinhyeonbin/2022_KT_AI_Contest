from tkinter import messagebox as msg
import csv
import random
import webbrowser

f = open('Music_data.csv', 'r', encoding='utf-8')
Sound_data = csv.reader(f)

music_df5 = []
music_df6 = []
music_df7 = []
music_df8 = []
music_df9 = []
music_df10 = []

for line in Sound_data:
    if line[0] == "기쁨":
        music_df5.append(line)
    elif line[0] == "당황":
        music_df6.append(line)
    elif line[0] == "분노":
        music_df7.append(line)
    elif line[0] == "불안":
        music_df8.append(line)
    elif line[0] == "상처":
        music_df9.append(line)
    elif line[0] == "슬픔":
        music_df10.append(line)

f.close()

f2 = open('Word_data.csv', 'r', encoding='utf-8')
Word_data = csv.reader(f2)

word_df5 = []
word_df6 = []
word_df7 = []
word_df8 = []
word_df9 = []
word_df10 = []

for line in Word_data:
    if line[0] == "기쁨":
        word_df5.append(line)
    elif line[0] == "당황":
        word_df6.append(line)
    elif line[0] == "분노":
        word_df7.append(line)
    elif line[0] == "불안":
        word_df8.append(line)
    elif line[0] == "상처":
        word_df9.append(line)
    elif line[0] == "슬픔":
        word_df10.append(line)

f2.close()

def Music_mode(label_idx):
    Music_list = music_df10

    if label_idx == 5:
        Music_list = music_df5
    elif label_idx == 6:
        Music_list = music_df6
    elif label_idx == 7:
        Music_list = music_df7
    elif label_idx == 8:
        Music_list = music_df8
    elif label_idx == 9:
        Music_list = music_df9

    random_value = random.choice(Music_list)
    url = random_value[3]  # pandas 3번째 url'
    title = random_value[1]
    singer = random_value[2]
    print("제목-", title, "| 가수-", singer)
    print(url)
    webbrowser.open(url)  # Colab에서는 false -> 파이참 실행시 실행가능


def Sentence_mode(label_idx):
    Word_list = word_df10

    if label_idx == 5:
        Word_list = word_df5
    elif label_idx == 6:
        Word_list = word_df6
    elif label_idx == 7:
        Word_list = word_df7
    elif label_idx == 8:
        Word_list = word_df8
    elif label_idx == 9:
        Word_list = word_df9

    random_value = random.choice(Word_list)

    sentence = random_value[2]
    speaker = random_value[1]

    print(sentence + "\n-" + speaker + "-")
    msg.showinfo("글귀 추천", sentence + "\n-" + speaker + "-")
