
#coding: utf-8

import wave
import struct
import numpy as np
import cv2
import math
import time
import random
#from pylab import *
s=""
font = cv2.FONT_HERSHEY_SIMPLEX
width=0
height=0
color=[255 for i in range(16)]
mode=""
drawing=False
fs=0
length=1000
NoP=0
page=1
#inputAAF=[] 
inputFreq=[]
inputAmp=[]
envelopeAmp=[0,0]
envelopeLength=[[0,0],[1000,0]]
envelopeAAF=[]
o=-1
F0=0
lengthList=[1000]
nothing_end=False
b=1
generate_end=False
erasing = False





#ErasingMode,ViewMode
#各変数のメモリ開放処理
#音響合成作業の進捗(%)をimg4に追記

#同じ行にenvelopeが入力された場合の処理を書く
#envelopeの描画で0以下の時は0に修正
#RBUTTONDOWNで描画した線を削除
#謎のエラーを修正

#説明書を書く#説明書を読ませたうえでおんなじ説明をする
#コメントを録音する
#良い点と悪い点をちゃんと聞きだして
#展望、改善点







#再生method
#wav書き出しmethod
#envelopeAAFの省略

#一連の動作をループから抜けずに


#variable



def window_size(event,x,y,flags,param): #初期設定
    
    global color,height,width,mode,fs,NoP
    
    cv2.rectangle(img,(0,80),(299,599),(0,0,0),thickness=-1,lineType=cv2.LINE_8)
    cv2.rectangle(img, (0, 80), (299, 160), (255, color[0], 255), thickness=-1, lineType=cv2.LINE_4)#1
    cv2.putText(img,'3840 * 2160' ,(50,130), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.rectangle(img, (0, 160), (299, 240), (200, color[1], 255), thickness=-1, lineType=cv2.LINE_4)#2
    cv2.putText(img,'2048 * 1536' ,(50,210), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.rectangle(img, (0, 240), (299, 320), (255, color[2], 255), thickness=-1, lineType=cv2.LINE_4)#3
    cv2.putText(img,'1920 * 1440' ,(50,290), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.rectangle(img, (0, 320), (299, 400), (200, color[3], 255), thickness=-1, lineType=cv2.LINE_4)#4
    cv2.putText(img,'1920 * 1080' ,(50,370), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.rectangle(img, (0, 400), (299, 480), (255, color[4], 255), thickness=-1, lineType=cv2.LINE_4)#5
    cv2.putText(img,'1680 * 1050' ,(50,450), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.rectangle(img, (0, 480), (299, 560), (200, color[5], 255), thickness=-1, lineType=cv2.LINE_4)#6
    cv2.putText(img,'1600 * 1200' ,(50,530), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.rectangle(img, (0, 560), (299, 640), (255, color[6], 255), thickness=-1, lineType=cv2.LINE_4)#7
    cv2.putText(img,'1600 * 1024' ,(50,610), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.rectangle(img, (0, 640), (299, 720), (200, color[7], 255), thickness=-1, lineType=cv2.LINE_4)#8
    cv2.putText(img,'1366 * 768' ,(50,690), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.rectangle(img, (0, 720), (599, 800), (0, 200, 200), thickness=-1, lineType=cv2.LINE_8)#9
    cv2.putText(img,'Enter' ,(350,770), font, 1,(0,0,0),2,cv2.LINE_AA)
    
    cv2.rectangle(img, (300, 80), (599, 160), (200, color[8], 255), thickness=-1, lineType=cv2.LINE_4)#1
    cv2.putText(img,'#96000' ,(350,130), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.rectangle(img, (300, 160), (599, 240), (255, color[9], 255), thickness=-1, lineType=cv2.LINE_4)#2
    cv2.putText(img,'#48000' ,(350,210), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.rectangle(img, (300, 240), (599, 320), (200, color[10], 255), thickness=-1, lineType=cv2.LINE_4)#3
    cv2.putText(img,'#44100' ,(350,290), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.rectangle(img, (300, 320), (599, 400), (255, color[11], 255), thickness=-1, lineType=cv2.LINE_4)#4
    cv2.putText(img,'#24000' ,(350,370), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.rectangle(img, (300, 400), (599, 480), (200, color[12], 255), thickness=-1, lineType=cv2.LINE_4)#5
    cv2.putText(img,'#22100' ,(350,450), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.rectangle(img, (300, 480), (599, 560), (255, color[13], 255), thickness=-1, lineType=cv2.LINE_4)#6
    cv2.putText(img,'12000' ,(350,530), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.rectangle(img, (300, 560), (599, 640), (200, color[14], 255), thickness=-1, lineType=cv2.LINE_4)#5
    cv2.putText(img,'10000' ,(350,610), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.rectangle(img, (300, 640), (599, 720), (255, color[15], 255), thickness=-1, lineType=cv2.LINE_4)#6
    cv2.putText(img,'8000' ,(350,690), font, 1,(0,0,0),2,cv2.LINE_AA)


    if event == cv2.EVENT_LBUTTONDOWN:
        
        if y < 80:
            pass;
        elif 80 < y < 160 and x < 300: #3840*2160
            width = 3840
            height = 2160
            color[0] = 0
            for i in range(1,8):
                color[i] = 255
        elif 80 < y < 160 and x >= 300: #Rate 96000
            fs=96000
            color[8]=10
            for i in range(9,16):
                color[i] = 255

        elif 160 < y < 240 and x < 300: #2048*1536
            width = 2048
            height = 1536
            for i in range(8):
                color[i]=255
            color[1]=0
        elif 160 < y < 240 and x >=300: #Rate 48000
            fs = 48000
            for i in range(8,16):
                color[i] = 255
            color[9]=10
        
        elif 240 < y < 320 and x < 300: # 1920 * 1440
            width = 1920
            height = 1440
            for i in range(8):
                color[i]=255
            color[2]=0

        elif 240 < y < 320 and x >= 300: #Rate 44100
            fs = 44100
            for i in range(8,16):
                color[i]=255
            color[10]=10

        elif 320 < y < 400 and x < 300: # 1920 * 1080
            width = 1920
            height = 1080
            for i in range(8):
                color[i]=255
            color[3]=0
        elif 320 < y < 400 and x >=300: #Rate 24000
            fs = 24000
            for i in range(8,16):
                color[i] = 255
            color[11]=10

        elif 400 < y < 480 and x < 300: # 1680 * 1050
            width = 1680
            height = 1050
            for i in range(8):
                color[i]=255
            color[4]=0
        elif 400 < y < 480 and x >=300: #Rate 22100
            fs = 22100
            for i in range(8,16):
                color[i] = 255
            color[12]=10

        elif 480 < y < 560 and x < 300: # 1600 * 1200
            width = 1600
            height = 1200
            for i in range(8):
                color[i]=255
            color[5]=0
        elif 480 < y < 560 and x >=300: #Rate 12000
            fs = 12000
            for i in range(8,16):
                color[i] = 255
            color[13]=10

        elif 560 < y <640 and x < 300: # 1600 * 1024
            width = 1600
            height = 1024
            for i in range(8):
                color[i]=255
            color[6]=0
        elif 560 < y < 640 and x >=300: #Rate 10000
            fs = 10000
            for i in range(8,16):
                color[i] = 255
            color[14]=10


        elif 640 < y <720 and x < 300: # 1366 * 768
            width = 1366
            height = 768
            for i in range(7):
                color[i]=255
            color[7]=0
        elif 640 < y < 720 and x >=300: #Rate 8000
            fs = 8000
            for i in range(8,16):
                color[i] = 255
            color[15]=10


        elif 720 < y < 800: #Enter
            if fs !=0 and width !=0:
                mode = "Launch"
                NoP = math.ceil(fs/width/2)
                print("Number of Page , ",NoP," SamplingRate ,",fs," width ",width," height ",height)
            else:
                pass;
        
        
        



def paint(event,x,y,flags,param): # 実際のスペクトラムのドローイング
    
    global width,height,fs,NoP,page,mode,inputAmp,inputFreq,envelopeLength,lengthList,erasing
    
    nowHz=x+(width*(page-1))
    nowAmp=math.floor((height-y)/(height-(height/10+height/10))*10000)/10000
    if generate_end:
        str_play="Play"
        
    elif generate_end!=True:
        str_play="#Play"
        
    
    # Page切り替えボタン
    cv2.rectangle(img, (0, 0), (width//2, height//10), (0, 200, 200), thickness=-1, lineType=cv2.LINE_8)
    cv2.putText(img,"NextFrequencyPage" ,(width//4,height//20), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.rectangle(img, (width//2, 0), (width-1, height//10), (200, 200, 200), thickness=-1, lineType=cv2.LINE_8)
    cv2.putText(img,"PreviousFrequencyPage" ,(width//2+width//8,height//20), font, 1,(0,0,0),2,cv2.LINE_AA) 

    # mode切り替えボタン
    cv2.rectangle(img, (0, height//10), (width//8, height//10+height//10), (200, 255, 255), thickness=-1, lineType=cv2.LINE_8)
    cv2.putText(img,str_play ,(width//45,height//10+height//20), font, 0.7,(0,0,0),2,cv2.LINE_AA)

    cv2.rectangle(img, (width//8, height//10), (width//4, height//10+height//10), (255, 255, 255), thickness=-1, lineType=cv2.LINE_8)
    cv2.putText(img,"Clear" ,(width//7+width//80,height//10+height//20), font, 1,(0,0,0),2,cv2.LINE_AA)
    
    cv2.rectangle(img, (width//4, height//10), (width//4+width//8, height//10+height//10), (255, 255, 0), thickness=-1, lineType=cv2.LINE_8)
    cv2.putText(img,"#ViewMode" ,(width//4+width//90,height//10+height//20), font, 0.8,(0,0,0),2,cv2.LINE_AA)
    
    cv2.rectangle(img, (width//4+width//8, height//10), (width//4*2, height//10+height//10), (0, 100, 100), thickness=-1, lineType=cv2.LINE_8)
    cv2.putText(img,"Preset" ,(width//4+width//7,height//10+height//20), font, 1,(0,0,0),2,cv2.LINE_AA)
    
    cv2.rectangle(img, (width//4*2, height//10), (width//4*3, height//10+height//10), (0, 255, 0), thickness=-1, lineType=cv2.LINE_8)
    cv2.putText(img,"Envelope" ,(width//16+width//2,height//10+height//20), font, 1,(0,0,0),2,cv2.LINE_AA)
    
    cv2.rectangle(img, (width//4*3, height//10), (width//4*4-1, height//10+height//10), (0, 0, 255), thickness=-1, lineType=cv2.LINE_8)
    cv2.putText(img,"Generate" ,(width-width//6,height//10+height//20), font, 1,(0,0,0),2,cv2.LINE_AA)

    
    

    # 200Hz毎に直線を描画
    if page > 1:    
        for i in range((page-1)*width,(page-1)*width+width):
            if i%200==0:
                cv2.line(img,(i-(width*(page-1)),height//10*2),(i-(width*(page-1)),height),(255,255,255),thickness=1,lineType=cv2.LINE_8)
    elif page == 1:
        for i in range(0,width,200):
            cv2.line(img,(i,height//10*2),(i,height),(255,255,255),thickness=1,lineType=cv2.LINE_8)


    #現在位置の周波数と振幅を描画
    cv2.rectangle(img, (int(width*0.70), height//10+height//10), (width, height//10+height//6), (255, 255, 255), thickness=-1, lineType=cv2.LINE_8)
    cv2.putText(img,str(nowHz)+" Hz, Amplitude: "+str(nowAmp)+ " nowPage: "+str(page)+"/"+str(NoP) ,(int(width*0.71), height//10+height//7), font, 0.5,(0,0,0),2,cv2.LINE_AA)
    
    if event == cv2.EVENT_LBUTTONDOWN:
        global drawing , s
        drawing = True
        
        if nowHz > fs//2:
            drawing = False
        
        
        if height//10+height//10 < y and drawing:
            cv2.line(img, (x, y), (x, height-1), (255, 0, 0), thickness=1, lineType=cv2.LINE_8) #Amplitudeの描画
            cv2.line(img,(x,y),(x,height//10+height//10),(0,0,0),thickness=1,lineType=cv2.LINE_8)
            inputFreq.append(nowHz) #配列にnowAmpとnowHzを追加
            inputAmp.append(nowAmp)
            
            if inputFreq.count(nowHz) > 1: #重複した場合前者を削除
                del inputAmp[inputFreq.index(nowHz)]
                inputFreq.remove(nowHz)
                
                print(str(inputFreq)+"Hz: "+str(inputAmp))
            
        elif 0 < x < width//2 and 0 < y < height//10: #nextPageが押された
            if page == NoP:
                pass
            else:
                page+=1
                switchPage()
                #for i in range(len(inputFreq)):
                #    if (page-1)*width< inputFreq[i] < (page-1)*width+width:     #pageが切り替わったときに周波数を再描画 #(height-y)/(height-(height/10+height/10))*100
                #        cv2.line(img,(inputFreq[i]-(page-1)*width,height),(inputFreq[i]-(page-1)*width,math.floor(height/10*8-(inputAmp[i]*(height/10*8))+height/10*2)),(255,0,0),thickness=1,lineType=cv2.LINE_8)
        
        elif 2//width < x < width and 0 < y <height//10: #PreviousPageが押された
            if page==1:
                pass
            else:
                page-=1
                switchPage()
                

        elif width//4*3 < x < width and height // 10 < y < height // 10 * 2: #Generateが押された *****************************
            mode = "Generate"
            print("Generate")
            #synthesis(inputAmp,envelopeAmp,inputFreq,fs,length)

        elif width//4*2 < x < width//4*3 and height//10 < y < height//10+height//10: # Envelopeが押された
            mode = "envelope"
            print("envelope")
            s=[[width//10,height//2-height//8],[width,height//2-height//8]]
            #envelope系の変数の初期化
            envelopeLength=[[0,0],[length,0]]
            lengthList=[length]
            b=1
        elif width//4+width//8 < x < width//4*2 and height //10 < y < height // 10 + height // 10 : # Presetが押された
            mode = "Preset"
            print("preset")

        elif width//4< x < width//4+width//8 and  height//10 < y < height//10+height//10: #viewmodeが押された
            pass
            mode = "view"
            print("view")

        elif width//8 < x < width//4 and height//10 < y < height//10*2: #AllClear
            cv2.rectangle(img,(0,height//10*2),(width,height),(0,0,0),thickness=-1)
            inputFreq.clear()
            inputAmp.clear()
            switchPage()

        elif 0 < x < width//8 and height//10 < y < height//10*2: #play?
            play(unpobreak,fs,8)

 
        
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        drawing=True
        if nowHz > fs//2:
            drawing = False
        elif height//10+height//10 < y and drawing:
            cv2.line(img, (x, y), (x, height-1), (255, 0, 0), thickness=1, lineType=cv2.LINE_8) #Amplitudeの描画
            cv2.line(img,(x,y),(x,height//10+height//10),(0,0,0),thickness=1,lineType=cv2.LINE_8)
            inputFreq.append(nowHz) #配列にnowAmpとnowHzを追加
            inputAmp.append(nowAmp)
            if inputFreq.count(nowHz) > 1: #重複した場合前者を削除
                del inputAmp[inputFreq.index(nowHz)]
                inputFreq.remove(nowHz)
                
                print(str(inputFreq)+"Hz: "+str(inputAmp))

    elif event == cv2.EVENT_LBUTTONUP:

        drawing = False

    """elif event == cv2.EVENT_RBUTTONDOWN: # ********************************************************************
        erasing = True
        cv2.line(img,(x,height),(x,height//10+height//10),(0,0,0),thickness=1,lineType=cv2.LINE_8)
        print("unchi")
        if nowHz in inputFreq:
            del inputAmp[inputFreq.index(x)]
            del inputFreq[inputFreq.index(x)]
            print("uncho")"""
            



def switchPage(): #************************************
    global page,width,height
    cv2.rectangle(img,(0,0),(width,height),(0,0,0),thickness=-1)
    for i in range(len(inputFreq)):
        if (page-1)*width< inputFreq[i] < (page-1)*width+width:     #pageが切り替わったときに周波数を再描画 #(height-y)/(height-(height/10+height/10))*100
            cv2.line(img,(inputFreq[i]-(page-1)*width,height),(inputFreq[i]-(page-1)*width,math.floor(height/10*8-(inputAmp[i]*(height/10*8))+height/10*2)),(255,0,0),thickness=1,lineType=cv2.LINE_8)
            #print(inputFreq[i]-(page-1)*width,math.floor(height/10*8-(nowAmp*(height/10*8))+height/10*2))

    



v=0
s=[[width//10,height//2-height//8],[width,height//2-height//8]]



def envelope(event,x,y,flags,param):
    global img2,width,height,fs,NoP,page,mode,drawing,v,s,length,envelopeLength,nothing_end,lengthList,b #s mean  point and line to draw envelope
    
    nowAmp=math.floor((y*-1+(height//2-height//8))/(height//2-height//8)*1000)/1000 #0.~1.
    if y > height//2-height//8:
        nowAmp=0.0
    nowLength=math.floor((x-width//10)/(width-width//10)*length) #0.0~length(default:1000ms)
    if x < width//10:
        nowLength=0
    

    cv2.rectangle(img2,(0,0),(width//10,height//2-height//8),(255, 255, 255), thickness=-1, lineType=cv2.LINE_8)
    cv2.rectangle(img2,(0,height//2-height//8),(width,height//2),(255 , 255 , 255),thickness=-1, lineType=cv2.LINE_8)
    cv2.line(img2, (0, height//2-height//8), (width, height//2-height//8), (0, 0, 0), thickness=1, lineType=cv2.LINE_8)
    if v == 0:
        for i in range(len(s)):
            cv2.circle(img2,(s[i][0],s[i][1]-1),10,(0,0,255),thickness=-1)
            if i >=1:
                cv2.line(img2,(s[i][0],s[i][1]-1),(s[i-1][0],s[i-1][1]-1),(0,0,255))
        v+=1
    for i in range(1,11):#目盛り
        cv2.line(img2,(width//12,height//2-height//8-((height//2-height//8)//10)*i),
                 (width//10,height//2-height//8-((height//2-height//8)//10)*i),(0,0,0),thickness=1,lineType=cv2.LINE_8)
        cv2.line(img2,(width//11,math.ceil(height//2-height//8-((height//2-height//8)//10)*(i+0.5))),
                 (width//10,math.ceil(height//2-height//8-((height//2-height//8)//10)*(i+0.5))),(0,0,0),thickness=1,lineType=cv2.LINE_8)

    cv2.rectangle(img2,(3*width//4,int(height//2-height//8*0.5)),(width,height//2),(0,255,0),thickness=-1) #ClearButton
    cv2.putText(img2,"Clear" ,(7*width//8,height//2-height//40), font, 1,(0,0,0),2,cv2.LINE_AA)
    
    cv2.rectangle(img2,(0,int(height//2-height//8*0.5)),(width//3,height//2),(255,0,0),thickness=-1) #Set Length Button
    cv2.putText(img2,"Length(now:"+str(length)+"(ms))",(width//34,height//2-height//40),font,0.8,(0,0,0),2,cv2.LINE_AA)
    
    cv2.rectangle(img2,(3*width//4,height//2-height//8),(width,int(height//2-height//16)),(255,255,0),thickness=-1)# Enter Button
    cv2.putText(img2,"Enter",(7*width//8,height//2-height//13),font,1,(0,0,0),2,cv2.LINE_AA)
    
    cv2.putText(img2,"x:"+str(nowLength)+"(ms)"+"y:"+str(nowAmp),(3*width//8,height//2-height//40),font,1,(0,0,0),2,cv2.LINE_AA) #座標表示
    
    
    if event == cv2.EVENT_LBUTTONDOWN and 3*width//4<x<width and int(height//2-height//8*0.5) < y < height//2:# as pushed Clear
        s=[[width//10,height//2-height//8],[width,height//2-height//8]]
        cv2.rectangle(img2,(width//10,height//2-height//8),(width,0),(0,0,0),thickness=-1)
        for i in range(len(s)):
            cv2.circle(img2,(s[i][0],s[i][1]-1),10,(0,0,255),thickness=-1)
            if i >=1:
                cv2.line(img2,(s[i][0],s[i][1]-1),(s[i-1][0],s[i-1][1]-1),(0,0,255))
        
        envelopeLength=[[0,0],[0,length]]
        lengthList=[length]
        b=1

    elif event == cv2.EVENT_LBUTTONDOWN and 3*width//4 < x < width and height//2-height//8 < y < int(height//2-height//16): # as pushed Enter
        envelopeLength=sorted(envelopeLength)
        b=1
        
        
        mode = "Launch"
        
    
    
    
        
    if event == cv2.EVENT_LBUTTONDOWN and x > width//10 and y < height//2-height//8: #envelopeの描画
        drawing=True
        
        
    elif event == cv2.EVENT_MOUSEMOVE and drawing and x > width//10 and y < height//2-height//8:
        
        cv2.rectangle(img2,(width//10,height//2-height//8),(width,0),(0,0,0),thickness=-1)#初期化
        
        cv2.circle(img2,(x,y),10,(0,0,255),thickness=-1)
        for i in range(len(s)):
            cv2.circle(img2,(s[i][0],s[i][1]),10,(0,0,255),thickness=-1)
            if i >=1:
               cv2.line(img2,(s[i][0],s[i][1]),(s[i-1][0],s[i-1][1]),(0,0,255))

    elif event == cv2.EVENT_LBUTTONUP and x > width//10 and y < height//2-height//8:
        
        cv2.rectangle(img2,(width//10,height//2-height//8),(width,0),(0,0,0),thickness=-1)
        s.append([x,y])
        s.sort(reverse=True)
        
        cv2.circle(img2,(x,y),10,(0,0,255))
        for i in range(len(s)):
            cv2.circle(img2,(s[i][0],s[i][1]),10,(0,0,255),thickness=-1)
            if i >=1:
                cv2.line(img2,(s[i][0],s[i][1]),(s[i-1][0],s[i-1][1]),(0,0,255))
        drawing = False
        envelopeLength.insert(1,[nowLength,nowAmp])
        print(envelopeLength)
        #envelopeAmp.insert(1,nowAmp)

    """elif event == cv2.EVENT_LBUTTONUP and x > width//10 and y < height//2-height//8:
            
        cv2.rectangle(img2,(width//10,height//2-height//8),(width,0),(0,0,0),thickness=-1)
        s.append([x,0])
        s.sort(reverse=True)
        
        cv2.circle(img2,(x,y),10,(0,0,255))
        for i in range(len(s)):
            cv2.circle(img2,(s[i][0],s[i][1]),10,(0,0,255),thickness=-1)
            if i >=1:
                cv2.line(img2,(s[i][0],s[i][1]),(s[i-1][0],s[i-1][1]),(0,0,255))
        drawing = False
        envelopeLength.insert(1,[nowLength,nowAmp])
        print(envelopeLength)"""
    
    cv2.rectangle(img2,(0,int(height//2-height//8*0.5)),(width//3,height//2),(255,0,0),thickness=-1) #Set Length Button
    cv2.putText(img2,"Length(now:"+str(length)+"(ms))",(width//34,height//2-height//40),font,0.8,(0,0,0),2,cv2.LINE_AA)





def preset(event,x,y,flags,param):
    global o,mode,F0
    
    
    cv2.rectangle(img3,(0,height//8),(width//4,height//4),(255,color[0],255),thickness=-1)
    cv2.putText(img3,"Rectangle",(width//13,height//5),font,1,(0,0,0),2,cv2.LINE_AA)
    cv2.rectangle(img3,(width//4,height//8),(width//4*2,height//4),(200,color[1],255),thickness=-1)
    cv2.putText(img3,"Triangle",(width//4+width//12,height//5),font,1,(0,0,0),2,cv2.LINE_AA)
    cv2.rectangle(img3,(width//4*2,height//8),(width//4*3,height//4),(255,color[2],255),thickness=-1)
    cv2.putText(img3,"Phasor",(width//2+width//12,height//5),font,1,(0,0,0),2,cv2.LINE_AA)
    cv2.rectangle(img3,(width//4*3,height//8),(width,height//4),(200,color[3],255),thickness=-1)
    cv2.putText(img3,"Noise",(width//2+width//3,height//5),font,1,(0,0,0),2,cv2.LINE_AA)

    cv2.rectangle(img3,(0,height//4),(width,height//2),(0,255,0),thickness = -1)
    cv2.putText(img3,"Enter",(width//4*2,height//3),font,1,(0,0,0),2,cv2.LINE_AA) #Enter
    
    cv2.putText(img3,"LowerOvertone (ON : OFF)",(width//20,height//20),font,1,(0,0,255),2,cv2.LINE_AA) #toggle button as Lower overtune
    cv2.rectangle(img3,(width//4+width//8,0),(width//2,height//8),(255,255,255),thickness=1)
    
    #cv2.rectangle()#Enter
    if event == cv2.EVENT_LBUTTONDOWN and width//4+width//8< x < width//2 and y < height//8: #LowerOvertoneのtoggleが押された
        if o == -1:
            cv2.line(img3,(width//4+width//8,0),(width//2,height//8),(0,0,255)) 
            cv2.line(img3,(width//4+width//8,height//8),(width//2,0),(0,0,255))
            o*=-1 #×が描画されている状態だと下方倍音列がONの状態
            
            
        elif o==1:
            o*=-1
            cv2.rectangle(img3,(width//4+width//8,0),(width//2,height//8),(0,0,0),thickness=-1)
            

    if event == cv2.EVENT_LBUTTONDOWN:
        if x < width//4 and height//8 < y < height//4:
            color[0]=0
            for i in range(1,3):
                color[i] = 255
                mode = "Rectangle"
        elif width//4 < x < width//4*2 and height//8 < y < height//4:
            for i in range(4):
                color[i] = 255
            color[1] = 0
            mode = "Triangle"
        elif width//4*2 < x < width//4*3 and height//8 < y < height//4:
            for i in range(4):
                color[i] = 255
            color[2]=0
            mode = "Phasor"
        elif width//4*3 < x < width and height//8 < y < height//4:
            for i in range(3):
                color[i] = 255
            color[3] = 0
            mode = "Noise"
        elif height//4 < y < height//2:
            c=1
            if mode == "Rectangle":
                for i in range(F0,fs//2,F0):
                    if c % 2 == 0:
                        inputFreq.append(i)
                        inputAmp.append(1/c)
                    elif c:
                        inputFreq.append(i)
                        inputAmp.append(1/c)
                    c+=1
                
                    if o==1: # LowerOvertone
                        if c % 2 == 0:
                            inputFreq.append(F0//c)
                            inputAmp.append(1/c)

            elif mode =="Triangle":
                for i in range(F0,fs//2,F0):
                    inputFreq.append(i)
                    inputAmp.append(1/c**c)
                    c+=1
                    if o==1: #下方倍音列
                        inputFreq.append(F0//c)
                        inputAmp.append(1/c**c)
            
            elif mode == "Phasor":
                for i in range(F0,fs//2,F0):
                    inputFreq.append(i)
                    inputAmp.append(1/c)
                    c+=1
                    if o==1: #下方倍音列
                        inputFreq.append(F0//c)
                        inputAmp.append(1/c)
            
            elif mode == "Noise":
                for i in range(fs//2):
                    inputFreq.append(i)
                    inputAmp.append(random.random())

                
            mode = "Launch"
            switchPage()
            print(inputAmp,inputFreq)

    

def Generate(event,x,y,flags,param):
    
    global mode,envelopeAAF,envelopeLength,length,fs,inputAmp,b,generate_end
    
    cv2.rectangle(img4,(170,180),(230,220),(255,255,255),thickness=-1)
    cv2.putText(img4,"Yes",(175,210),font,1,(255,0,255),2,cv2.LINE_AA)
    cv2.rectangle(img4,(240,180),(300,220),(255,255,255),thickness=-1)
    cv2.putText(img4,"No",(250,210),font,1,(255,0,255),2,cv2.LINE_AA)
    cv2.putText(img4,"Output with wavfile?",(100,100),font,1,(255,255,255),2,cv2.LINE_AA)


    if event == cv2.EVENT_LBUTTONDOWN and 170 < x < 230 and 180 <y < 220: #YES
        cv2.rectangle(img4,(170,180),(230,220),(0,0,255),thickness=-1)
        cv2.putText(img4,"Yes",(175,210),font,1,(255,0,255),2,cv2.LINE_AA)
        time.sleep(1)
        mode = "Launch"
        a=1
        print(1,"AAF ",len(envelopeAAF)," envelopeLength ",envelopeLength," inputAmp ",inputAmp," inputFreq ",inputFreq)
        if b==1: #envelopeLengthの値をlength*fs/1000にソート
            for i in range(len(envelopeLength)):
                envelopeLength[i][0]*=int(fs/1000)
        
        if sum(inputAmp) > 1:
            for i in range(len(inputAmp)):
                inputAmp[i]*=1/sum(inputAmp)
        while(1):
        
            
            for j in  range(envelopeLength[a-1][0],envelopeLength[a][0]):
                envelopeAAF.append(envelopeLength[a-1][1]+((envelopeLength[a][1]-envelopeLength[a-1][1])*(j-envelopeLength[a-1][0])/(envelopeLength[a][0]-envelopeLength[a-1][0]))) #サンプル数*length/1000ぶんのamplitudeDataをenvelopeAAFを使う
                print(a,j)
                
                #if (j-envelopeLength[a-1][0])/(envelopeLength[a][0]-envelopeLength[a-1][0])==float(1):
                #    continue
            
            #if envelopeLength[a]==envelopeLength[-1]:
             #   print("oppai")
              #  break
            if envelopeLength[a]==len(envelopeLength):
                break
            a+=1
            ("a+=1")
            if a>len(envelopeLength):
                print("unpo")
                break
                
            elif int(fs*length/1000)<=len(envelopeAAF):
                print("ochinchin")
                break;
                
        
        #print(envelopeAAF)
        #print(len(envelopeLength))
        #print(int(length/1000 * fs))
        #print(len(envelopeAAF),"envelopeAAF")
        
        cv2.destroyWindow("image4")
        print(2,"AAF ",len(envelopeAAF)," envelopeLength ",envelopeLength," inputAmp ",inputAmp," inputFreq ",inputFreq)
        #unpobreak=synthesis()
        #play(unpobreak,fs,8)
        
        a=1
        b-=1
        generate_end=True

    elif event == cv2.EVENT_LBUTTONDOWN and 240 < x < 300 and 180 <y < 220: #No
        cv2.rectangle(img4,(240,180),(300,220),(0,0,255),thickness=-1)
        cv2.putText(img4,"No",(250,210),font,1,(255,0,255),2,cv2.LINE_AA)
        time.sleep(0.5)
        mode = "Launch"

    


def view(event,x,y,flags,param): #*************************************************************** shift & closed
    global mode
    cv2.rectangle(img5,(0,0),(width,height),(0,0,0),thickness=-1)
    cv2.rectangle(img5,(0,0),(width,height//10*2),(255,255,255),thickness=-1) # CloseButton
    cv2.putText(img5,"Close",(width//7*3,height//10),font,1,(0,0,0),2,cv2.LINE_AA)
    if event == cv2.EVENT_LBUTTONDOWN:
        mode = "close"





img = np.zeros((800,600,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',window_size)


def unko():
    global img,width,height
    img = np.zeros((height,width,3), np.uint8)
    cv2.namedWindow("image")
    cv2.setMouseCallback('image',paint)
    cv2. waitKey(1)
    cv2.startWindowThread()
    cv2. waitKey(1)
    print(width,height)

def launchEnvelope():
    global img2,width,height
    pass

def nothing(x):
    global nothing_end
    
    
    nothing_end=True
    
    


def nothing_2(x):
    pass


def synthesis():
    global envelopeAAF
    data = []
    # [-1.0, 1.0]の小数値が入った波をfs*length/1000個作成
    for n in range(int(length/1000 * fs)):  # nはサンプルインデックス #np.arange
        z=0.0
        for k in range(len(inputFreq)):  # サンプルごとに10個のサイン波を重ね合わせ ここのrangeの値が描画されたx座標の数になり、変数f0の数値がx座標に対応する
            z += envelopeAAF[n]*inputAmp[k]  * np.sin(2 * np.pi  *(inputFreq[k]) * n / fs) # 振幅はここの0.01がinputAmp*EnvelopeAmp座標の値に対応すること #inputAmpにinputEAmp[n]をかける
            #print(n)        
        # 振幅が大きい時はクリッピング
        if z > 1.0:  z = 1.0
        if z < -1.0: z = -1.0
        data.append(z)
    # [-32768, 32767]の整数値に変換
    data = [int(x * 32767.0) for x in data]

    # バイナリに変換
    data = struct.pack("h" * len(data), *data)  # listに*をつけると引数展開される
    envelopeAAF.clear()
    return data


def play (data, fs, bit):
    import pyaudio
    # ストリームを開く
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=int(fs),
                    output= True)
    # チャンク単位でストリームに出力し音声を再生
    chunk = 1024
    sp = 0  # 再生位置ポインタ
    buffer = data[sp:sp+chunk]
    while buffer != b'':
        stream.write(buffer)
        sp = sp + chunk
        buffer = data[sp:sp+chunk]
    stream.close()
    p.terminate()
    





if __name__ == "__main__" : # main()
    text=["Please Select Resolution","Select SamplingRate"]
    
    mode="windowSize"
    print(mode)
    if mode == "windowSize":
        while(1):
            cv2.imshow("image",img)
            img = cv2.rectangle(img, (0, 0), (299, 80), (255, 255, 255), thickness=-1, lineType=cv2.LINE_8)
            img = cv2.putText(img,text[0] ,(5,50), font, 0.7,(0,0,0),2,cv2.LINE_AA)
            img = cv2.rectangle(img, (300, 0), (599, 80), (255, 255, 255), thickness=-1, lineType=cv2.LINE_8)
            img = cv2.putText(img,text[1] ,(305,50), font, 0.7,(0,0,0),2,cv2.LINE_AA)
            if cv2.waitKey(2) & 0xFF == 27:
                print("aaaaaaaaaaaaaaaaaaa",mode)
                cv2.destroyAllWindows()
                break
            elif cv2.waitKey(2) & 0xFF == 13 and width !=0:
                mode = "Launch"

            elif mode =="Launch":
                #unko()
                for i in range(16):
                    color[i]=255
                cv2. waitKey(1)
                cv2.destroyWindow("image")
                cv2. waitKey(1)
                break;
            

    if mode == "Launch":
        
        unko()
        
        while(1):
            
            cv2.imshow("image",img)
            if cv2.waitKey(2) & 0xFF == 27: #Esc
                print("aaaaaaaaaaaaaaaaaaa",mode)
                cv2.destroyAllWindows()
                break
            elif cv2.waitKey(2) & 0xFF == 13: #Enter
                print("unko",mode)

            
                
            
            elif mode == "envelope":
                

                cv2. waitKey(1)
                img2 = np.zeros((height//2,width,3), np.uint8) #envelope window
                cv2. waitKey(1)
                cv2.namedWindow('image2')
                cv2. waitKey(1)
                cv2.setMouseCallback('image2',envelope)
                cv2. waitKey(1)
                cv2.startWindowThread()
                cv2. waitKey(1)
                print("envelope")
                
                cv2.createTrackbar('length(ms)','image2',1000,10000,nothing)
                
                while(1):
                    cv2. waitKey(1)
                    cv2.imshow("image2",img2)
                    cv2. waitKey(1)
                    length = cv2.getTrackbarPos('length(ms)','image2')
                    if length ==0:
                        length=1
                    
                    if nothing_end:
                        b=1
                        lengthList.append(length)
                        print(lengthList)
                        v=0
                        for i in envelopeLength: #Lengthが0になった場合の処理
                            envelopeLength[v][0]=math.ceil(envelopeLength[v][0]*lengthList[-1]/lengthList[-2])
                            
                            v+=1
                        v=0
            
                        if len(lengthList) > 2:
                           print(lengthList)
                           del lengthList[:-2]
                           print("tinpo",lengthList)
                           print("unpo",envelopeLength)
                        nothing_end=False
                    
                    
                    if cv2.waitKey(1) & 0xFF == 27: #Esc
                        cv2.destroyWindow("image2")
                        break
                    elif cv2.waitKey(1) & 0xFF == 13: # Enter **********************************************************************
                        cv2.destroyWindow("image2")
                        break
                    elif mode == "Launch":
                        cv2.destroyWindow("image2")
                        break
                continue

            
            elif mode == "Preset":
                
                cv2.waitKey(1)
                img3 = np.zeros((height//2,width,3),np.uint8) #PresetWindow
                cv2.waitKey(1)
                cv2.namedWindow("image3")
                cv2.setMouseCallback("image3",preset)
                cv2. waitKey(1)
                cv2.startWindowThread()
                cv2. waitKey(1)
                cv2.createTrackbar('F0(Hz)','image3',440,int(fs/2),nothing_2)
                
                
                print("preset")
                
                while(1):
                    cv2.waitKey(1)
                    cv2.imshow("image3",img3)
                    cv2.waitKey(1)
                    F0 = cv2.getTrackbarPos('F0(Hz)','image3')
                    
                    

                    if cv2.waitKey(1) & 0xFF == 27: # Esc
                        cv2.destroyWindow("image3")
                        break
                    elif cv2.waitKey(1) & 0xFF == 13: #Enter
                        cv2.destroyWindow("image3")
                        break
                    elif mode == "Launch":
                        cv2.destroyWindow("image3")
                        break
                continue
                    

            elif mode == "Generate":
                cv2.waitKey(1)
                img4 = np.zeros((400,500,3),np.uint8) #GenerateWindow
                cv2.waitKey(1)
                cv2.namedWindow("image4")
                cv2.setMouseCallback("image4",Generate)
                cv2. waitKey(1)
                cv2.startWindowThread()
                cv2. waitKey(1)
                
                while(1):
                    cv2.waitKey(1)
                    cv2.imshow("image4",img4)
                    cv2.waitKey(1)
                    if cv2.waitKey(1) & 0xFF == 27: # Esc
                        cv2.destroyWindow("image4")
                        break
                    elif cv2.waitKey(1) & 0xFF == 13: #Enter
                        cv2.destroyWindow("image4")
                        break
                    elif mode =="Launch":
                        cv2.destroyWindow("image4")
                        break
                unpobreak=synthesis()
                play(unpobreak,fs,8)
                continue

            elif mode == "view":
                print(1)
                cv2.waitKey(1)
                img5 = np.zeros((height,width,3),np.uint8) #viewWindow
                cv2.waitKey(1)
                cv2.namedWindow("image5")
                cv2.setMouseCallback("image5",view)
                cv2. waitKey(1)
                cv2.startWindowThread()
                cv2. waitKey(1)

                while(1):
                    cv2.waitKey(1)
                    cv2.imshow("image5",img5)
                    cv2.waitKey(1)
                    if cv2.waitKey(1) & 0xFF == 27: # Esc
                        cv2.destroyWindow("image5")
                        break
                continue
                    
                
        
        

        
            
    
        
        
    cv2.destroyAllWindows()