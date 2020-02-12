import os
import re
import zipfile
def volmoesort():
	#取得目前執行目錄(預設在該漫畫資料夾內)
	path = os.getcwd()
	#影像所在位置
	DIR = 'image/'
	#計算有幾張照片
	total = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
	#扣掉cover和madeby這兩張
	total = total-2
	#print(total)
	#cover to 00.jpg
	os.rename(path+'/'+DIR+'cover.jpg', path+'/'+DIR+'00.jpg')
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
		
		

current = os.getcwd()
filenames = os.listdir()
result = []
#print(filenames)
for i in filenames: # loop through all the files and folders to find epub
	if i.endswith(r'.epub'): #if epub found, unzip
		result.append(i)
		#print(i[:-5])
		#os.system('pause')
		with zipfile.ZipFile(open(i, 'rb')) as f:
			f.extractall(i[:-5])
#print("epub: "+result)


#os.system('pause')
filenames = os.listdir()
folderlist = []
for i in filenames: # loop through all the files and folders
    if os.path.isdir(os.path.join(os.path.abspath("."), i)): # check whether the current object is a folder or not
        folderlist.append(i)
print(folderlist)
#os.system('pause')
for i in folderlist:
	#print(current+'/'+i)
	os.chdir(current+'/'+i)
	print(os.getcwd())
	#os.system('pause')
	volmoesort()
	os.chdir(current)


