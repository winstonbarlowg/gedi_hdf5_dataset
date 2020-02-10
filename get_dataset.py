import h5py
import pandas as pd
import numpy as np
import matplotlib as plt

filename = 'GEDI01_B_2019108002011_O01959_T03909_02_003_01.h5'
hdf = h5py.File(filename, 'r')

# # see list of ites in the file
# base_items = list(hdf.items())
# print('Items in the base directory:', base_items)

# look into what is in the first group
group1 = hdf.get('BEAM0000')

# for key in group1:
    # print(key)

# get a list of the names of datasets excluding a subgroup
def get_list(): 
    result = []
    for key in group.keys():
        if key != 'ancillary':
            result.append(key)
    return result

def get_arrays(group):
    for key in group:
        for k in get_list():
            if key == k:
                all_data = [np.array(group.get(key))]
    return all_data

get_arrays(group1)

# get an array of a dataset contained in the group
all_samples_sum = np.array(group1.get('all_samples_sum'))
delta_time = np.array(group1.get('delta_time'))

# create a pandas dataframe from the previous array 
df = pd.DataFrame(all_samples_sum)
df.columns = ['All Samples Sum']
# print(df)
# df.plot()

# combining two arrays into one pandas dataframe
df_from_arr = pd.DataFrame(data=[all_samples_sum, delta_time])
df3 = df_from_arr.T
df3.columns = ['all_samples_sum', 'delta_time']
df3


