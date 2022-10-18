import csv

# with 구문과 같이 사용하면 close() 처리를 자동으로 해준다.
with open('member.csv', 'r') as csvfile :
    lines = csv.reader(csvfile)
    for line in lines :
        print(line[0:2])

# with open('member.csv', 'r') as csvfile :
#     lines = csv.reader(csvfile, quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
#     for line in lines :
#         print(line[:])

# 쓰기모드
# with open('member.csv', 'w') as csvfile :
#     lines2 = csv.writer(csvfile)
#     lines2.writerows()