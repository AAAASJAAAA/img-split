from PIL import Image  

img = Image.open("data.jpg")
print('图片大小',img.size)
img_array=img.load()

data_list = []
for i in range(0,img.size[1]):
    if i != 648 or i != 0:
        data = []
        for a in range(200,240):#设置颜色区间
            data.append((a,a,a))

        for c in data:
            if img_array[0,i] == c:
                data_list.append(i)
print(len(data_list))

d = 0

for i in range(len(data_list)):
    try:
        d+=1
        left = 0
        upper = data_list[i] + 5
        right = img.size[0]
        lower = data_list[i+1]
        region = img.crop((left, upper, right, lower))#截取图片的位置
        print(region.size)
        if region.size[1] >20:
            region.save(str(d)+".jpg")
        else:
            d -=1
    except Exception as e:
        print(e)