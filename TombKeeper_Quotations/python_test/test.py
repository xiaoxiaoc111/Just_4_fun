# coding=utf8


def test1():
    with open('C:/Users/xiaoxiaoc/Desktop/test/test.txt','r',encoding= 'utf-8') as f:  
        lines=f.readlines()  
    with open('C:/Users/xiaoxiaoc/Desktop/test/test.txt','w',encoding= 'utf-8') as w:  
        for l in lines:  
            if ('(javascript:void(0);)' not in l) : 
                w.write(l)     
    print ("test1 is ok ,已经去除收藏 点赞 转发 评论的 js ")

def test2():
    with open('C:/Users/xiaoxiaoc/Desktop/test/test.txt','r',encoding= 'utf-8') as f:  
        lines=f.readlines()  
    with open('C:/Users/xiaoxiaoc/Desktop/test/test.txt','w',encoding= 'utf-8') as w:  
        for l in lines:  
            if ('[![' not in l) : 
                w.write(l)  
    print ("test3 is ok ,已经去除头像")

def test3():
    with open('C:/Users/xiaoxiaoc/Desktop/test/test.txt','r',encoding= 'utf-8') as f:  
        lines=f.readlines()  
    with open('C:/Users/xiaoxiaoc/Desktop/test/test.txt','w',encoding= 'utf-8') as w:  
        for l in lines:  
            if ('[*û**收藏' not in l) : 
                w.write(l)    
    print ("test3 is ok ,已经转发微博中的收藏 点赞 转发 评论的 js")

def test31():
    with open('C:/Users/xiaoxiaoc/Desktop/test/test.txt','r',encoding= 'utf-8') as f:  
        lines=f.readlines()  
    with open('C:/Users/xiaoxiaoc/Desktop/test/test.txt','w',encoding= 'utf-8') as w:  
        for l in lines: 
            if ('[*ñ**' not in l) : 
                w.write(l)    
    print ("test31 is ok ,已经转发微博中的收藏 点赞 转发 评论的 js")

def test32():
    with open('C:/Users/xiaoxiaoc/Desktop/test/test.txt','r',encoding= 'utf-8') as f:  
        lines=f.readlines()  
    with open('C:/Users/xiaoxiaoc/Desktop/test/test.txt','w',encoding= 'utf-8') as w:  
        for l in lines: 
            if ("[***" not in l) : 
                w.write(l)
   
    print ("test3 is ok ,已经转发微博中的收藏 点赞 转发 评论的 js")

def test33():
    with open('C:/Users/xiaoxiaoc/Desktop/test/test.txt','r',encoding= 'utf-8') as f:  
        lines=f.readlines()  
    with open('C:/Users/xiaoxiaoc/Desktop/test/test.txt','w',encoding= 'utf-8') as w:  
        for l in lines: 
            if ("[** *" not in l) : 
                w.write(l)
   
    print ("test3 is ok ,已经转发微博中的收藏 点赞 转发 评论的 js")

def test4():
    with open('C:/Users/xiaoxiaoc/Desktop/test/test.txt','r',encoding= 'utf-8') as f:  
        lines=f.readlines()  
    with open('C:/Users/xiaoxiaoc/Desktop/test/test.txt','w',encoding= 'utf-8') as w:  
        for l in lines:  
            if ('[tombkeeper]'  in l) : 
                  w.write(l.replace('[tombkeeper]', '### [tombkeeper]'))
                  continue
            w.write(l) 
    print ("test4 is ok ,已经依据markdown文本要求 为[] 前置位添加### 渲染为标题3")

countBlank = 0
def test5():
    global countBlank
    c = '---'
    with open('C:/Users/xiaoxiaoc/Desktop/test/test.txt','r',encoding= 'utf-8') as f:  
        lines=f.readlines()  
    with open('C:/Users/xiaoxiaoc/Desktop/test/test.txt','w',encoding= 'utf-8') as w:  
        for te in lines:  
            if  ('标签'  in te ):
                countBlank = 0
            if not  te.split(): 
                countBlank += 1 
            if countBlank == 2 :
                w.write(str(c))
                continue
            w.write(te)  
    print ("test5 is ok ,已经依据markdown文本要求 为每一条微博之间添加 --- 进行隔断")


test1()
test2()
test3()
test31()
test32()
test33()
test4()
test5()

