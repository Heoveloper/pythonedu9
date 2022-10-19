# 딕셔너리 객체 생성 1
dictionary = {}
print(type(dictionary))

# 딕셔너리 객체 생성 2
# dictionary2 = dict()
# print(type(dictionary2)) # return <class 'dict'>

# 요소 추가
dictionary['student'] = '학생'
dictionary['teacher'] = '선생님'
dictionary['classroom'] = '교실'
print(dictionary)

# 요소 삭제
del dictionary['classroom']
print(dictionary)

deletedItem = dictionary.pop('teacher') # return value
print(deletedItem)
print(dictionary)

# 요소 수정
# 키가 없으면 추가하고 있으면 수정
dictionary['student'] = '1반 학생'
print(dictionary)

# 요소 조회
dictionary['teacher'] = '선생님'
dictionary['classroom'] = '교실'

# 요소 조회 1) items()
# 요소(키, 값)들은 튜플로, 전체는 리스트로 반환
items = dictionary.items()
print(items)

# 요소 조회 2) keys()
# 키를 요소로 갖는 리스트를 반환
keys = dictionary.keys() 
print(keys)

# 요소 조회 3) values()
# 값을 요소로 갖는 리스트를 반환
values = dictionary.values()
print(values)

# 요소 조회 4-1) 키로 값을 조회하기
value = dictionary['student']
print(value)

# 요소 조회 4-2) get() 키로 값을 조회하기
# 만약 없으면 2번째 매개값을 반환
getValue1 = dictionary.get('student', 'none')
print(getValue1)
getValue2 = dictionary.get('student2', '없음')
print(getValue2)

# 요소 전체 출력
def printList() :
    for ele in dictionary.keys() :
        print('단어: {:^13}, 뜻: {:}'.format(ele, dictionary.get(ele)))
printList()

# '사전' 객체 복사
dictionaryCopy = dictionary.copy()
print(dictionary, '\n', dictionaryCopy)

# update() 2개의 '사전' 객체 병합
# 키가 동일하면 업데이트, 다르면 추가되는 방식
dictionaryCopy['blackboard'] = '칠판'
dictionary.update(dictionaryCopy)
print(dictionary)

# setdefault()
# 키가 있으면 값을 반환하고 없으면 추가
# 1) 키가 있으면 값을 반환
print(dictionary.setdefault('student'))
# 2) 키가 없으면 요소 추가 후 값을 반환
print(dictionary.setdefault('student2', '2반 학생'))
print(dictionary)

# key 존재여부 판단
print('student' in dictionary) # True
print('student' not in dictionary) # False
print('student2' in dictionary) # False

# 요소 개수
print(len(dictionary))

# 요소 정렬
print('===정렬 시작===')
# 오름차순 정렬
sdasc = sorted(dictionary.items())
# 내림차순 정렬
sddesc = sorted(dictionary.items(), reverse=True)

print('오름차순 정렬')
for item in sdasc :
    print('단어: {:^13} 뜻: {}'.format(item[0], item[1]))

print('내림차순 정렬')
for item in sddesc :
    print('단어: {:^13} 뜻: {}'.format(item[0], item[1]))

print('===정렬 끝===')

# 문자열 공백 제거
# replace(): 모든 공백 제거
# strip(), lstrip(), rstrip(): 양쪽, 왼쪽, 오른쪽 공백 제거

# 파일에 저장
f = open('d:\Heo\kh\python\dictionary.txt', 'w', encoding='UTF-8')
for line in sdasc :
    f.write('{}: {}\n'.format(line[0].strip(), line[1].strip()))
f.close()

# 파일에서 읽어오기
f = open('d:\Heo\kh\python\dictionary.txt', 'r', encoding='UTF-8')
if f.readable() :
    dic = {}
    for line in f.readlines() :
        list = line.split(':') # :을 기준으로 요소를 나눠 리스트에 담아서 반환
        list[1].lstrip()
        print(list)
        dic[list[0].strip()] = list[1].strip()
    f.close()
    print(dic)

# 요소 전체 삭제
dictionary.clear()
print(len(dictionary)) # 빈 딕셔너리 객체 {} 상태

# '사전' 객체 제거: 메모리에서 제거되어 접근 불가
# del dictionary
# print(len(dictionary))


# 문자열 길이
print(len('student'))

# 문자열 비교 ==

# 소문자, 대문자 변환: lower(), upper()
print('aBc'.upper())
print('SCHOOL'.lower())

# word = input('단어를 입력하세요 >> ').upper()
# print(word)
# word = input('단어를 입력하세요 >> ')
# print(word.upper())

