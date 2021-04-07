import os, os.path
import pandas as pd

list = os.listdir('C:/Users/golovach/Desktop/dataset')
list2=['albrecht-durer', 'alfred-sisley', 'amedeo-modigliani', 'andrei-rublev', 'andy-warhol',  'camille-pissarro', 'caravaggio', 'claude-monet', 'diego-rivera', 'diego-velazquez', 'edgar-degas', 'edouard-manet', 'edvard-munch', 'el-greco', 'eugene-delacroix', 'francisco-goya', 'frida-kahlo', 'georges-seurat', 'giotto-di-bondone', 'gustav-klimt', 'gustave-courbet', 'henri-de-toulouse-lautrec', 'henri-matisse', 'henri-rousseau', 'hieronymus-bosch', 'jackson-pollock', 'jan-van-eyck', 'joan-miro', 'kazimir-malevich', 'leonardo-da-vinci', 'marc-chagall', 'michelangelo', 'mikhail-vrubel', 'pablo-picasso', 'paul-cezanne', 'paul-gauguin', 'paul-klee', 'peter-paul-rubens', 'pierre-auguste-renoir', 'piet-mondrian', 'pieter-bruegel-the-elder', 'raphael', 'rembrandt', 'rene-magritte', 'salvador-dali', 'sandro-botticelli', 'titian', 'vincent-van-gogh', 'wassily-kandinsky', 'william-turner']

df_folders = pd.DataFrame(columns=['artist', 'images qty'])

for each in list2:
    list = os.listdir(f'C:/Users/golovach/Desktop/dataset/{each}/artworks')
    number_files = len(list)
    df_folder = pd.DataFrame([[each, number_files]], columns=['artist', 'images qty'])

    df_folders = df_folders.append(df_folder, ignore_index=True)
print (df_folders)


