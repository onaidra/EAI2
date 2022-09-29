import cv2
 
img = cv2.imread('sapienzalogo.jpg', cv2.IMREAD_UNCHANGED)

dim = input("dimensione ridotta: ")
dim = int(dim)
print('Original Dimensions : ',img.shape)
 
#scale_percent = 60 # percent of original size
#width = int(img.shape[1] * scale_percent / 100)
#height = int(img.shape[0] * scale_percent / 100)
dim = (dim, dim)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)

cv2.imwrite("logo.jpg",resized)
