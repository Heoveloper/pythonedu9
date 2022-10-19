# 파일 존재여부 판단하기

import os

file = r'd:\Heo\kh\python\test.txt'
print(os.path.exists(file))

vocabulary = None
if not os.path.exists(file) :
    # 파일이 존재하지 않으면 신규
    vocabulary = open(file, 'w', encoding="UTF-8")
    print('신규 생성')
else :
    # 파일이 존재하면 추가
    vocabulary = open(file, 'a', encoding="UTF-8")
    print('기존 파일 열기')