import numpy as np
import pandas as pd
import random
import os

def ffff():
    directory = 'data\\'

    column_names = ["artist", "folder",	"artwork", "date", "style",	"genre", "link", "path"]

    df_full = pd.DataFrame(columns = column_names)
    df_train = pd.DataFrame(columns = column_names)
    df_test = pd.DataFrame(columns = column_names)
    for eachartistfolder in os.listdir(directory):

        df_full_each=pd.read_csv(f'{directory}\\{eachartistfolder}\\artworks.csv')
        np.random.seed(10)
        msk = np.random.rand(len(df_full_each)) <= 0.8
        #print (msk)
        df_train_each = df_full_each[msk]
        df_test_each = df_full_each[~msk]

        df_full = df_full.append(df_full_each, ignore_index=True)
        df_train = df_train.append(df_train_each, ignore_index=True)
        df_test = df_test.append(df_test_each, ignore_index=True)
        #print (len (df_file), len(train), len(test))

    #print (len(df_full), len (df_train), len (df_test))
    #df_full.to_csv('df_full.csv')
    #df_train.to_csv('df_train.csv')
    #df_test.to_csv('df_test.csv')

    #for each in os.listdir(f'{directory}\\{eachartistfolder}'):
    #    print (each)