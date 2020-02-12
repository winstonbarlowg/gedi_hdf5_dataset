import h5py
import pandas as pd
import numpy as np
import matplotlib as plt

filename = 'GEDI01_B_2019108002011_O01959_T03909_02_003_01.h5'
hdf = h5py.File(filename, 'r')

group1 = hdf.get('BEAM0000')

# get a list of the datasest manually excluding subgroups
def get_list(group): 
    result = []
    for key in group.keys():
        if key != 'ancillary':
            if key != 'geolocation':
                if key != 'geophys_corr':
                    result.append(key)
    return result

# get a list only of hdf5 dataset types, excludes subgroups
def get_dataset_list(group):
    just_datasets = []
    datasets_len = []
    for key in group.keys(): 
        if type(group.get(key)) == h5py._hl.dataset.Dataset:
            just_datasets.append(key)
            
    for dataset in just_datasets: # from previous list, store datasets of a specific array length in a list
        if len(np.array(group.get(dataset))) == 249810:
            datasets_len.append(dataset)

    #     return just_datasets
    return  datasets_len

# using the list from get_datasets_list(), get a numpy array for each dataset and store in list
def get_arrays(group):
    all_arrays = []
    for key in group:
        for k in get_dataset_list(group):
            if key == k:
                all_arrays.append(np.array(group.get(key)))
    return all_arrays

# create dictionary combining list with name of datasets and respective arrays
data = dict(zip(get_dataset_list(group1), get_arrays(group1)))

# pandas fataframe from dictionary
df = pd.DataFrame.from_dict(data)
# df.to_csv(r'File Name.csv') # export to csv if needed