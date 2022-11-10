import os

img=input('Enter img name:')

os.system('fswebcam '+img)

if(img):
    print('capture')
    
    
else:
    print('error')
    
          


