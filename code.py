import vk_api
import numpy as np
import urllib
import collections
import random
from PIL import Image

def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True

    return key, remember_device

login, password = 'your_login', 'your_p@ssw0rd' //enter your info
session = vk_api.VkApi(login, password, auth_handler=auth_handler, scope=2**13) //needs access to wall
session.auth(token_only=True)

api = session.get_api()

items = []
min_set_size = 1000 #you will get around min_set_size posts
nextfrom=''
while len(items)<1000:
    posts = api.newsfeed.search(count = 100, q = 'your_query', start_from = nextfrom)
    items+=posts['items']
    if 'next_from' in posts: 
        nextfrom = posts['next_from']
    else:
        break
        
posts = items #i was lazy to rename

texts = []
photos = []
for index, post in enumerate(posts):
    if 'text' in post:
        texts.append(post['text'])
    if 'attachments' in post:
        if post['attachments'][0]['type'] == 'photo':
            for link in post['attachments'][0]['photo']['sizes']:
                if link['type'] == 'z':
                    photos.append(link['url']) #gets links to pictures 
                    
for index, photo in enumerate(photos):
    try:
        urllib.request.urlretrieve(photo, 'imgs/'+str(index)+'.bmp') #downloads all pictures to /imgs/ to be used later 
    except:
        print(index) #if something happens you know where the problem occured
        

# TEXT AVERAGE

#gets rid of useless symbols
for i in range(len(texts)):
    texts[i] = texts[i].replace('\n', ' ')
    for n in range(10):
        texts[i] = texts[i].replace('  ', ' ')
    texts[i] = texts[i].lower()


#EACH LETTER APPROACH
sumlen = 0
for text in texts:
    sumlen+=len(text)
    
avglen = sumlen//len(texts) #average text length

#for each position writes the most common symbol
avgtext = ''
for i in range(avglen):
    letters = []
    for text in texts:
        if len(text)>i:
            if(text[i]!=' '):
                letters.append(text[i])
    col = collections.Counter(letters)
    maxinstance = col.most_common()[0][1]
    mostcommonletters = []
    for pair in col.most_common():
        if pair[1]==maxinstance:
            mostcommonletters.append(pair[0])
        else:
            break
    avgtext+=random.choice(mostcommonletters) 
    
#EACH WORD APPROACH
words = [text.split( ' ') for text in texts]

sumwlen = 0
for wording in words:
    sumwlen += len(wording)
avgwlen = sumwlen//len(words)

stopwords = ['', 'и', 'в', 'на'] #gets rid of stopwords in resulting text, as these are not interesting

avgwtext = ''
for i in range(avgwlen):
    ithwords = []
    for wording in words:
        if len(wording)>i:
            if wording[i] not in stopwords:
                ithwords.append(wording[i])
    col = collections.Counter(ithwords)
    maxinstance = col.most_common(1)[0][1]
    mostcommonwords = []
    for pair in col.most_common():
        if pair[1]==maxinstance:
            mostcommonwords.append(pair[0])
        else:
            break
    avgwtext+=random.choice(mostcommonwords)+' '
    

#PHOTO AVERAGE

npphotos = []
#for each photo changes it to 27 color palette and turns into (y,x,3) ndarray
for image in range(len(photos)):
    try:
        currimg = Image.open('imgs/'+str(image)+'.bmp').convert('RGB')
        currimg = currimg.point(lambda x: ((x+64)//128)*128-1)
        npphotos.append(np.asarray(currimg))
    except:
        print(image)

#average photo dimensions
xsum = 0
ysum = 0
for photo in npphotos:
    ysum+=photo.shape[0]
    xsum+=photo.shape[1]

avgx = xsum//len(npphotos)
avgy = ysum//len(npphotos)

avgpicture = np.zeros((avgy, avgx), dtype=(tuple,3)) #array to store the result

#for each pixel at x,y places the most common pixel at x,y
#very slow code
for y in range(avgy):
    for x in range(avgx):
        pixels = [] 
        for photo in npphotos:
            if photo.shape[0]>y and photo.shape[1]>x:
                pixels.append(tuple(photo[y,x]))
        col = collections.Counter(pixels)
        maxinstance = col.most_common()[0][1]
        mostcommonpixels = []
        for pair in col.most_common():
            if pair[1]==maxinstance:
                mostcommonpixels.append(pair[0])
            else:
                break
        avgpicture[y,x]=random.choice(mostcommonpixels)

avgimage = Image.fromarray(np.uint8(avgpicture)) #turns array to image


#RESULT
print(avgtext) #text with average letters
print(avgwtext) #text with average words

avgimage.show() #image with average pixels
