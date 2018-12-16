# coding:utf-8
import json 
import numpy as np
import sys
sys.path.append('./jieba_zn/')
import jieba
jieba.setLogLevel(60)

def update():
    
    f = open('train_data','r')
    new = open('stop_words.txt','wa')
    Json_Array = json.loads(f.read())
    Json_value_Array = [int(i) for i in Json_Array.values()]
    q75, q25 = np.percentile(Json_value_Array, [75 ,25])
    iqr = q75 - q25
    #d2= q75+iqr*1.5
    #d1= q25-iqr*1.5
    d2, d1 = np.percentile(Json_value_Array, [98.04 ,1.96])
    print d2,'-',d1
    for key, value in Json_Array.items():
        #print len(key)
        if int(value)>d2 or int(value)<d1:
            new.write(key.encode('utf-8')+'\n')
        else:
            pass
            #print key
    stop_words_default=["「","」","，","！"]
    for i in stop_words_default:
        new.write(i+'\n')
    new.close()
    drop_repeat()

def drop_repeat():
    print("drop repeat text.....")
    f = open('stop_words.txt','r')
    Stop_Words_Array_in_txt = f.readlines()
    f.close()
    f = open('stop_words.txt','w')
    Stop_Words_Array = []
    for i in Stop_Words_Array_in_txt:
        if i not in Stop_Words_Array and i != '\n':
            Stop_Words_Array.append(i) 
            f.write('\n'+i)
    f.close()




def train(data_file_name):

    print 'doc/waitfortrain/'+str(data_file_name)+'.txt'
    f = open('doc/waitfortrain/'+str(data_file_name)+'.txt','r')
    seg_list = jieba.lcut(f.read(),cut_all=False)
    #print seg_list
    doc={}
    for i in seg_list:
        if i.encode('utf-8') not in doc.keys():
            doc.update({i.encode('utf-8'):"1"})
        else:
            if i.encode('utf-8') != '\n' and  i.encode('utf-8') != '':
                doc[i.encode('utf-8')] = str(int(doc[i.encode('utf-8')])+1).strip()






    
    
    json_data = open('train_data','r')
    try:
        Json_Array = json.loads(json_data.read(),encoding="utf-8")
    except ValueError:
        print 'ValueError: error in your train data,maybe is a \'tap\' or likes word.'
    json_data.close()
    new_data ={}
    Json_Array_new = {}
    new_data.update(doc)
    exist_key = Json_Array.keys()

    for key, value in Json_Array.items():
        Json_Array_new.update({key.encode('utf-8'):value.encode('utf-8')})

    
    for key, value in new_data.items():
        if key.decode("utf-8") !="\n" and key.decode("utf-8")!="":
            if key.decode("utf-8") not in exist_key :
                Json_Array_new.update({str(key):str(value)})
            else:
                update_value = int(Json_Array_new[key])+int(value)
                Json_Array_new[key] = str(update_value)
            


    json_data_string = '{'
    for key, value in Json_Array_new.items():
        #print type(key),type(value)
        #print key,value
        nkv = '"'+key+'":"'+value+'",'
        json_data_string = json_data_string + nkv
    json_data_string = json_data_string[:len(json_data_string)-1]+'}'
    json_data = open('train_data','w')
    json_data.write(json_data_string)
    json_data.close()    
    f.close()
    



for i in range(1,291):
    train(i)
update()



