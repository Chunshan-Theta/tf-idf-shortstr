from tfidfalgorithm import idf
import os,sys
sys.path.append('./jieba_zn/')
import jieba
import logging as log
jieba.setLogLevel(60)
log.basicConfig(format='\n%(levelname)s:%(message)s',level=log.INFO)
import matplotlib.pyplot as plt



#loading all of the text files in training folder into a 2v array
def loadingFile(FileNum=10,trainingfolder="./collection/"):
    FileContentArray = []
    #search all subfile
    for dirPath, dirNames, fileNames in os.walk(trainingfolder):
        #print dirPath
        #for f in fileNames:
        for idx, f in enumerate(fileNames):
            #print os.path.join(dirPath, f)
            TargetFileDir = str(os.path.join(dirPath, f))
            with open(TargetFileDir,"r") as f:
                content =str(f.read())
                log.debug(content)
                FileContentArray.append(content)
            if idx>FileNum:
                break
    log.debug(FileContentArray)
    return FileContentArray

#make a list of all the words from training data
def MakeWordsList(DataArray):
    wordslist = []
    
    
    for idx, unitContent in enumerate(DataArray):

        seg_list = jieba.lcut(unitContent,cut_all=False)

        log.debug(seg_list)
        for words in seg_list:
            if not words in wordslist:
                log.debug(words)
                wordslist.append(words)

    log.debug(wordslist)    
    return wordslist
  
#comput the four arguments like appear time of word in the article, the number of word in the article,  the number of articles contains the target word and the number of the all article. 
def frontProcess(wordslist,DataArray=[],additionalWeight=0):
  
    NumberAppearArticle = 0
    NumberArticle = len(DataArray)
    currentdict = {}
    
    for word in wordslist:
        if not word in currentdict:
            NumberAppearArticle = 0
            for row in DataArray:
                if word in row:
                    NumberAppearArticle+=1
                    theta=row.count(word)/len(row)
                    log.debug(word)
                    log.debug(theta)
                    NumberAppearArticle+=theta*additionalWeight
           
            currentdict = computing(NumberArticle,NumberAppearArticle,currentdict,word)
    log.debug(currentdict)    
    return currentdict



# computing result of the word with tfidf algorithm.

def computing(NumberArticle,NumberAppearArticle,dictObject,wordunit):
    IDF_Result = idf(NumberArticle,NumberAppearArticle)
    newdict = recordingResult(dictObject,newData={wordunit:IDF_Result},outputFile=0)
    return newdict


# make an output JSON file with computing result
# adding new result to dict object,then output the object to a file and return dict object. 
def recordingResult(dictObject={},newData={},outputFile=0):
    dictObject.update(newData)
    if outputFile:
        pass
    return dictObject



def showchart(d,showON=1):

    
    x = range(len(d.values()))
    y = d.values()
    y = [float(n) for n in y]
    y.sort(key=float)
    log.debug(y)
    plt.plot(x, y, '-o')
    if showON:
        plt.show()




DataArray = loadingFile(200)
wordslist = MakeWordsList(DataArray)
'''
d = frontProcess(wordslist,DataArray,2)
showchart(d,0)
d = frontProcess(wordslist,DataArray,1)
showchart(d,0)
'''

for i in range(5):
    d = frontProcess(wordslist,DataArray,5-i)
    showchart(d,0)
d = frontProcess(wordslist,DataArray,0)
showchart(d)