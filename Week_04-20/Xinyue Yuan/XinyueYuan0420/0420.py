# -*- coding: cp936 -*-
from matplotlib import pyplot as plt
'''
希尔排序
'''
def ShellSort(list):
  
    m = len(list) # 元素数目
    gap = m/2     # gap = 
    while gap > 0:  # 
        '''
                  列表中的list[i],按间隔gap从列表中取元素list[i+1],list[i+1+gap],list[i+1+2gap]...与list[i]比较
                  选择小的与list[i]交换
        '''
        for i in xrange(m):  
            index = i
            j = i+1
            while j < m: 
                if list[j] < list[index]:
                    index = j
                j += gap
            if index != j:  # 若有元素比list[i]小,交换
                list[index],list[i] = list[i],list[index]
        gap = gap / 2
    return list
   
if __name__== '__main__':
    list_0=[]
    f=open("input.txt")
    lines=f.readlines()
    for line in lines:
        line.strip('\n')
        key=int(line)
        list_0.append(key)
    list_1 = ShellSort(list_0)
    print "Min:",list_1[0]
    print "Mid:",list_1[(len(list_1)+1)/2]
    print "Max:",list_1[len(list_1)-1]
    # 参数依次为list,抬头,X轴标签,Y轴标签,XY轴的范围

def draw_hist(myList,Title,Xlabel,Ylabel,Xmin,Xmax,Ymin,Ymax):
    plt.hist(myList,1000)
    plt.xlabel(Xlabel)
    plt.xlim(Xmin,Xmax)
    plt.ylabel(Ylabel)
    plt.ylim(Ymin,Ymax)
    plt.title(Title)
    plt.show()
draw_hist(list_1,'Histogram','Number of input','Frequency',0.0,1000,0.0,30) 
