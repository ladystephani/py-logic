# print('t'.encode('utf-8'))

# file = open('./src/script4.txt', 'r', encoding='utf-8') # 'r' means read
# filecontent = file.read()
# print(filecontent)
# file.close()

# openfile = open('./src/script4.txt', 'a', encoding='utf-8') # 'w' means erase and write, 'a' means append
# openfile.write('\nRating:\n')
# openfile.write('Five Stars\n')
# openfile.close()

scores = open('./src/magic_hw.txt','r', encoding='utf-8')
scores_per_line = scores.readlines() #becomes a list
scores.close()
for score in scores_per_line:
    # print(score)
    data = score.split()

    #storage
    total_score = 0

