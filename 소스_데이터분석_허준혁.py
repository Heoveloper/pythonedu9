import os

file = r'd:\Heo\kh\python\voca.txt'
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

# 반복문 여부
vocaRun = True

# 영어단어장 생성
vocaNote = {}

while vocaRun == True :

    print('\n영어단어장')
    print('1. 저장 2. 검색 3. 수정 4. 삭제 5. 목록 6. 통계 7. 종료 ')
    svc = int(input('번호를 입력하세요 >> '))

    if svc == 1 :
        print('\n[저장]')
        voca = input('저장할 단어를 입력해주세요 >> ').lower()
        mean = input('뜻을 입력해주세요 >> ').lower()

        if len(vocaNote) > 4 :
            print('최대 5개 단어만 저장할 수 있습니다.')
        elif voca in vocaNote :
            print('이미 등록된 단어입니다.')
        else :
            vocaNote[voca] = mean

        print('\n현재 단어장: {}'.format(vocaNote))
        continue

    elif svc == 2 :
        print('\n[검색]')
        SearchedVoca = input('검색할 단어를 입력해주세요 >> ').lower()

        if SearchedVoca in vocaNote :
            value = vocaNote[SearchedVoca]
            print(value)
        elif SearchedVoca not in vocaNote :
            print('단어를 검색할 수 없습니다.')
        elif list(vocaNote.keys())[0].startswith(SearchedVoca) :
            voca = list(vocaNote.keys())[0]
            mean = vocaNote[voca]
            print('검색단어 일부로 찾은 결과입니다.')
            print('전체 단어: {}, 뜻: {}'.format(voca, mean))
        elif list(vocaNote.keys())[1].startswith(SearchedVoca) :
            voca = list(vocaNote.keys())[1]
            mean = vocaNote[voca]
            print('검색단어 일부로 찾은 결과입니다.')
            print('전체 단어: {}, 뜻: {}'.format(voca, mean))
        elif list(vocaNote.keys())[2].startswith(SearchedVoca) :
            voca = list(vocaNote.keys())[2]
            mean = vocaNote[voca]
            print('검색단어 일부로 찾은 결과입니다.')
            print('전체 단어: {}, 뜻: {}'.format(voca, mean))
        elif list(vocaNote.keys())[3].startswith(SearchedVoca) :
            voca = list(vocaNote.keys())[3]
            mean = vocaNote[voca]
            print('검색단어 일부로 찾은 결과입니다.')
            print('전체 단어: {}, 뜻: {}'.format(voca, mean))
        elif list(vocaNote.keys())[4].startswith(SearchedVoca) :
            voca = list(vocaNote.keys())[4]
            mean = vocaNote[voca]
            print('검색단어 일부로 찾은 결과입니다.')
            print('전체 단어: {}, 뜻: {}'.format(voca, mean))
        else :
            print('단어를 검색할 수 없습니다.')
        continue

    elif svc == 3 :
        print('\n[수정]')
        voca = input('수정할 단어를 입력해주세요 >> ').lower()
        modMean = input('수정할 뜻을 입력해주세요 >> ').lower()

        if voca in vocaNote :
            vocaNote[voca] = modMean
            print('단어의 뜻을 수정하였습니다.')
        else :
            print('수정할 단어를 검색할 수 없습니다.')
        continue

    elif svc == 4 :
        print('\n[삭제]')
        deletedVoca = input('삭제할 단어를 입력해주세요 >> ').lower()

        if deletedVoca in vocaNote :
            del vocaNote[deletedVoca]
            print('단어를 삭제하였습니다.')
            print('현재 단어장: {}'.format(vocaNote))
        else :
            print('삭제할 단어를 검색할 수 없습니다.')
        continue

    elif svc == 5 :
        print('\n[목록]')
        print('1. 오름차순 조회 2. 내림차순 조회')
        selectedMenu = int(input('번호를 입력하세요 >> '))

        asc = sorted(vocaNote.items())
        desc = sorted(vocaNote.items(), reverse=True)

        if selectedMenu == 1 :
            for item in asc :
                print('단어: {} 뜻: {}'.format(item[0], item[1]))
        if selectedMenu == 2 :
            for item in desc :
                print('단어: {} 뜻: {}'.format(item[0], item[1]))
        continue

    elif svc == 6 :
        print('\n[통계]')

        # 단어 글자수가 가장 많은 단어
        keys = list(vocaNote.keys())
        longestVoca = max(keys)

        # 단어 글자수 내림차순 목록
        desc = sorted(keys, key=lambda voca: len(voca), reverse=True)

        print('저장된 단어 개수: {}'.format(len(vocaNote)))
        print('단어 글자수가 가장 많은 단어: {}'.format(longestVoca))
        print('단어 글자수 내림차순 목록: {}'.format(desc))
        continue

    elif svc == 7 :
        asc = sorted(vocaNote.items())

        # 파일에 저장
        f = open(file, 'w', encoding='UTF-8')
        for line in asc :
            f.write('{}: {}\n'.format(line[0].strip(), line[1].strip()))
        f.close()

        # 파일에서 읽어오기
        f = open(file, 'r', encoding='UTF-8')
        if f.readable() :
            vocabulary = {}
            for line in f.readlines() :
                list = line.split(':')
                list[1].lstrip()
                print(list)
                vocabulary[list[0].strip()] = list[1].strip()
            f.close()

        print('\n단어장이 종료됩니다.')
        break

    else :
        print('\n잘못된 입력입니다.')
        continue
