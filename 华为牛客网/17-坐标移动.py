

while True:
    try:
        all=input().split(";") #A10;S20;W10;D30;X;A1A;B10A11;;A10;
        rule={"A":1,"D":2,"W":3,"S":4}
        x,y=0,0
        for i in range(len(all)):
            temp=all[i]
            if not temp:
                continue #continue放在循环（for或者while）里面，当true的时候，不继续往下执行，而是进行下一轮循环♻️
            judge=rule.get(temp[0],0) #关键点3：当temp[0]没有rule字典里面的元素时，将0赋给judge
            if judge and len(temp)<=3:
                number=-1 #关键点2：为的是之后不执行坐标移动，不变化
                try:
                    number=int(temp[1:]) #关键点1：当除去第一位之后的字符不是数字时，判断为（pass无效invalid），该处不能赋值未能覆盖number=-1,直接跳过往下执行
                except:
                    pass
                """放在if judge and len(temp)<=3:里面"""
                if number>=0: #只有number=-1时，不满足
                    if judge==1:
                        x-=number
                    elif judge==2:
                        x+=number
                    elif judge==3:
                        y+=number
                    else:
                        y-=number
        print(x,end=",")
        print(y)
    except:
        break
