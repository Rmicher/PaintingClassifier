import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from matplotlib import image
import os
from PIL import Image
import PIL

#df_full=pd.read_csv(f'df_full.csv', index_col=0)
#print (df_full)

def get_shape(path):
    shape=[0,0,0]
    shape= tuple(shape)
    try:
        img = image.imread(f'data\\{path}')
        shape=img.shape

    except:
        pass
    if len(shape)==2:
        shape_list=list(shape)
        shape_list.append(0)
        shape=tuple(shape_list)
    #print (shape)
    return shape

#getting size for each image
'''df_full['size']=df_full.apply(lambda row: get_shape(row['path']), axis = 1)

df_full[['size1', 'size2', 'size3']] = pd.DataFrame(df_full['size'].tolist(), index=df_full.index)
print (df_full)

df_full.to_csv('df_full_with_size.csv')'''


def resized_images_max_streched_1 (path, size):
    image = Image.open(f'data\\{path}')
    #print(image.size)
    img_resized = image.resize(size)
    #print(img_resized.size)

    #plt.imshow(image)
    #plt.show()
    #plt.imshow(img_resized)
    #plt.show()
    return img_resized

def resized_images_max_padded_2 (path, size):
    image = Image.open(f'data\\{path}')
    #print(image.size)
    width, height = image.size
    left=int((size[0]-width)/2)
    #print (width,left)
    top=int((size[1]-height)/2)
    #print (height,top)
    result = Image.new(image.mode, size, color='white')
    result.paste(image, (left, top))

    #plt.imshow(result)
    #plt.show()
    return result

#size=(750, 600)
#path='albrecht-durer\\artworks\\bacchanal-with-silenus.jpg'
#resized_images_max_streched_1 (path,size)
#resized_images_max_padded_2 (path,size)


def image_to_matrix(path,size):
    #print (path)
    #images_matrix=0
    try:
        #image_reshaped = resized_images_max_streched_1(path, size)
        image_reshaped=resized_images_max_padded_2 (path,size)
        #plt.imshow(image_reshaped)
        #plt.show()
        #print (image_reshaped.size)
        images_array = np.asarray(image_reshaped)
        #print (images_array)
        #image_reshaped2 = images_array.reshape(images_array.shape[0] * images_array.shape[1], 1)
        images_matrix=images_array
    except:
        images_matrix=0
        pass
    #print (images_matrix)
    return images_matrix

#image_reshaped=image.reshape(image.shape[0]*image.shape[1],1)

"""print (image_to_matrix(path,size))

image_reshaped2 = resized_images_max_padded_2(path, size)
print("image1", np.asarray(image_reshaped2).shape)
images_array=np.asarray(image_reshaped2)
print (images_array.shape)
print (images_array.shape[0], images_array.shape[1])
image_reshaped2 = images_array.reshape(images_array.shape[0] * images_array.shape[1], 1)
images_matrix=np.matrix(image_reshaped2)"""

#plt.imshow(image1)
#plt.show()

#image2 = image.imread(f'data\\{path}')
#print(image2.shape)


#print (np.array(image1))
#print (np.matrix(np.array(image1)).shape)

#image_to_matrix(path,size)

#df_full[['image_matrix']] = df_full.apply(lambda row: image_to_matrix(row['path'], size), axis = 1)
#df_full.to_csv('df_full_with_image_matrix.csv')