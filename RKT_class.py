# coding:utf-8
import numpy as np

class RKT:
    def __init__(self,Text_Array,Get_Top = 15):
        self.Text_Array = Text_Array
        self.Text_Node,self.Text_Node_Connection = self.build_node_diagram(Text_Array)
        self.Text_Node_Connection_weight = np.zeros((len(self.Text_Node), len(self.Text_Node)),int)
        self.Text_Node_value = np.arange(float(len(self.Text_Node)))
        self.Train_Time = 5
        for i in range(len(self.Text_Node_value)):
            self.Text_Node_value[i]=1
        self.calculate_connect_weight()
        self.calculate_score()
        self.Get_Top_Num = Get_Top 
        self.TopText = np.sort(self.Text_Node_value.argsort()[-1*self.Get_Top_Num:], axis=None) 
        self.TopText_H2L = self.Text_Node_value.argsort()[-1*self.Get_Top_Num:][::-1]    #Scorc high to low
        



    def build_node_diagram(self,Text_Array,WindowsSize = 5):
        Text_Node =[]
        Text_Node_Connection = []
        
        for i in range(len(Text_Array)):
            if Text_Array[i] not in Text_Node:
                Text_Node.append(Text_Array[i])
            connect = []
            if i-WindowsSize<0:
                for j in range(0,i+WindowsSize+1):
                    if i != j:
                        try:
                            connect.append(Text_Array[j])
                        except IndexError as e:
                            jieba.Write_Log_Debug("Debug IndexError: "+str(e)+", reducing windows size, please.")

            elif i+WindowsSize >= len(Text_Array):
                for j in range(i-WindowsSize,len(Text_Array)):
                    if i != j:
                        connect.append(Text_Array[j])

            else:
                for j in range(i-WindowsSize,i+WindowsSize+1):
                    if i != j:
                        connect.append(Text_Array[j])
            Text_Node_Connection.append([Text_Array[i],connect])
	
        for i in range(len(Text_Node_Connection)):
            Text_Node_Connection[i][0] = Text_Node.index(Text_Node_Connection[i][0])
            for j in range(len(Text_Node_Connection[i][1])):
                Text_Node_Connection[i][1][j]=Text_Node.index(Text_Node_Connection[i][1][j])

        return Text_Node,Text_Node_Connection
    def calculate_connect_weight(self):
        for i in self.Text_Node_Connection:
            for j in i[1]:
                row = int(i[0])
                col = int(j)
                self.Text_Node_Connection_weight[row][col]+=1

    def calculate_score(self):
        Text_Node = self.Text_Node
        Text_Node_Connection_weight = self.Text_Node_Connection_weight
        Text_Node_value = self.Text_Node_value
        for time in range(self.Train_Time):
            for i in range(len(Text_Node)):     
                d = 0.85
                Score = 1-d
                for j in range(len(Text_Node_Connection_weight[i])):
                    Score+= d*float(Text_Node_Connection_weight[i][j])*Text_Node_value[i]/float(sum(Text_Node_Connection_weight[j]))
                Text_Node_value[i] = Score
        self.Text_Node_Connection_weight = Text_Node_Connection_weight
        self.Text_Node_value = Text_Node_value   
	









