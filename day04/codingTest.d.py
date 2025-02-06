from collections import Counter

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
paragraph = paragraph.lower()
# 특수기호 없애기
new_paragraph = []
for p in paragraph:
    if p.isalpha() or p == ' ':
        new_paragraph.append(p)
    else:
        new_paragraph.append(' ')
print('000')
print(new_paragraph)
re_paragraph = ''.join(new_paragraph).split()
print(re_paragraph)

# 금지단어 치환
for para in re_paragraph[:]:
    if para in banned:
        re_paragraph.remove(para)

# for b in banned:
#     if len(b) 
#     re_paragraph = re_paragraph.replace(b, '')
print('11111')
print(re_paragraph)


p_cnt = Counter(re_paragraph).most_common()
# print(p_cnt[0][0])
print(p_cnt[0][0])