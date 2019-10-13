import os
import pandas as pd
path = '/Users/sidhikatripathee/Downloads/100 leaves plant species/data'
base_gcs_name = 'gs://plantsight-vcm/data/'
data_array = []

directory = os.listdir(path)
for folder in directory:
    if folder == ".DS_Store":
        continue
    #print "folder: " + folder
    subdir = os.listdir(path+"/"+folder) #goes inside each plant species folder
    for file in subdir:
        #print "file: " + file
        #files_dict = dict(zip(folder, file))

        data_array.append((base_gcs_name+folder+'/'+file,'', folder))
dataframe = pd.DataFrame(data_array)
dataframe.to_csv('all_data_corrected.csv', index=False, header=False)
