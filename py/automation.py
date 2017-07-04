#-*- coding:gbk -*-

import copy
from collections import Counter

#�����  
class node:  
    def __init__(self, ch, father=None):  
        self.ch = ch            #���ֵ  
        self.fail = None        #Failָ��  
        self.tail = 0           #β��־����־Ϊ i ��ʾ�� i ��ģʽ����β  
        self.child = []         #�ӽ��  
        self.childvalue = []    #�ӽ���ֵ

#AC�Զ�����  
class automation:           
    def __init__(self, keys):                   
        self.root = node("")                      #��ʼ�������  
        self.count = 0                            #ģʽ������
        self.keys = copy.copy(keys)
        
        for key in keys:
            self.count += 1                             #����ģʽ����ģʽ��������һ  
            p = self.root  
            for i in key:  
                if i not in p.childvalue:               #���ַ������ڣ�����ӽ��  
                    child = node(i, p)  
                    p.child.append(child)  
                    p.childvalue.append(i)  
                    p = child  
                else :                                  #����ת���ӽ��  
                    p = p.child[p.childvalue.index(i)]  
            p.tail = self.count                         #�޸�β��־  
        self.__ac_automation()
          
    #�ڶ������޸�Failָ��  
    def __ac_automation(self):                                                  
        queuelist = [self.root]                     #���б�������  
        while len(queuelist):                       #BFS�����ֵ���  
            temp = queuelist[0]  
            queuelist.remove(temp)                  #ȡ������Ԫ��  
            for i in temp.child:  
                if temp == self.root:               #�����ӽ��Failָ����Լ�  
                    i.fail = self.root  
                else:  
                    p = temp.fail                   #ת��Failָ��  
                    while p:                          
                        if i.ch in p.childvalue:    #�����ֵ�ڸý����ӽ���У���Failָ��ý��Ķ�Ӧ�ӽ��  
                            i.fail = p.child[p.childvalue.index(i.ch)]  
                            break  
                        p = p.fail                  #����ת��Failָ���������  
                    if not p:                       #��p==None����ʾ��ǰ���ֵ��֮ǰ��û���ֹ�������Failָ������  
                        i.fail = self.root  
                queuelist.append(i)                 #����ǰ���������ӽ��ӵ�������  
                
    #��������ģʽƥ��  
    def run(self, strmode):
        p = self.root  
        cnt = {}                                    #ʹ���ֵ��¼�ɹ�ƥ���״̬                               
        for i in strmode:           #����Ŀ�괮
            while i not in p.childvalue and p is not self.root:  
                p = p.fail  
            if i in p.childvalue:                   #���ҵ�ƥ��ɹ����ַ���㣬��ָ���Ǹ���㣬����ָ������  
                p = p.child[p.childvalue.index(i)]  
            else :                                    
                p = self.root  
            temp = p  
            while temp is not self.root:              
                if temp.tail:                    #β��־Ϊ0������           
                    if temp.tail not in cnt:  
                        #cnt.setdefault(temp.tail)  
                        cnt[temp.tail] = 1
                    else:  
                        cnt[temp.tail] += 1  
                temp = temp.fail
                
        ret = Counter()
        for key_index in cnt:
            ret[self.keys[key_index - 1]] = cnt[key_index]
        return ret                                  #����ƥ��״̬  

def test():
    key = ["��", "��־��", "dahai", "qww", "��ȫԱ"]        #����ģʽ��
    acp = automation(key)

    text = "������:���뵳ί�����ڹ������ϡ��䱸����ȫԱ"
    dct = acp.run(text)                    #�����Զ���
    
    print(dct)
    
if __name__ == "__main__":
    test()