
"""
list() 可以将一串字符，分成单个单个的字符
输入：
3 abc bca cab abc 1

"""
while True:
    try:
        all=input().split() #输入3 abc bca cab abc 1 生成=> ['3', 'abc', 'bca', 'cab', 'abc', '1']
        # print(all,type(all)) #此时的 <class 'list'>
        target=all[-2] # abc 注意此时还不是list，而是list的一个元素
        container=all[1:-2]
        word=[]
        count=0
        for i in container:
            if target!=i: #要求和原来的单词不同
                m=list(target) #将每个字符作为单个元素组合成list
                m.sort()
                n=list(i)
                n.sort()
                if m==n:
                    count+=1
                    word.append(i)
        word.sort()
        if count!=0 and int(all[-1])<=len(word): #注意int(all[-1])一定要int
            print(count)
            print(word[int(all[-1])-1])
        elif count!=0 and int(all[-1])>len(word):
            print(count)
        else:
            print(count)
    except:
        break