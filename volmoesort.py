import os
import re
#取得目前執行目錄(預設在該漫畫資料夾內)
path = os.getcwd()
#影像所在位置
DIR = 'image/'
#計算有幾張照片
total = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
#扣掉cover和madeby這兩張
total = total-2
#print(total)
for i in range(1,total+1):
 filename = 'html/'+str(i)+'.html'
 fp = open(filename, 'r', encoding = 'utf8')
 #print(filename)
 html = fp.readlines()
 #利用正規表現式在html中尋找jpg的位置
 imgRe = re.compile(r'src="(.+?\.jpg)"')
 imageUrl = imgRe.findall(str(html))
 #把前面的..拿掉
 last = "".join(imageUrl)[2:]
 #last = last[2:]
 #加上路徑以免跑掉
 newfilename = '/'+DIR+str(i)+'.jpg'
 #print(last)
 #print(newfilename)
 os.rename(path+last, path+newfilename)
 fp.close()
 #print(fp.readlines())
os.rename(path+'/cover.jpg', path+'/00.jpg')
