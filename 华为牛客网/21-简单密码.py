
"""
ASCLL码 ：ord('y')=121   chr(122)='z'
"""
#  1 |  2 |  3 |
#  1 | abc| def|
########################
#  4 |  5 |  6 |
# ghi| jkl| mno|
########################
# 7  |  8 |  9 |
#pqrs| tuv|wxyz|
########################
#    |  0 |
#    |  0 |
while True:
    try:

        s=input()
        res=''
        for i in s:
            if i.isdigit():
                res+=i
            elif i.isupper() and i !="Z": #大写字母转小写再向后移
                res+=chr(ord(i.lower())+1)
            elif i=="Z":
                res+='a'
            else: #注意数字在这里接入是字符，需要加引号
                if i in 'abc':
                    res+='2'
                elif i in 'def':
                    res+='3'
                elif i in 'ghi':
                    res+='4'
                elif i in 'jkl':
                    res+='5'
                elif i in 'mno':
                    res+='6'
                elif i in 'pqrs':
                    res+='7'
                elif i in 'tuv':
                    res+='8'
                else:
                    res += '9'
        print(res)
    except:
        break