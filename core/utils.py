import pathlib
from pathlib import Path
import numpy as np


def convert_file_to_h5(fpath, features=[], dtype=float):
    """
    Convert various types of files to hdf5

    Parameters:
    -----------
    fpath: str
    filepath to existing file not in hdf5 format
    
    features: list of str
    list of data feature names 

    dtype: dtype
    data type assigned to feature data

    """

    #
    # Read file type
    #
    fname = Path(fpath).stem
    file_extension = Path(fpath).suffix

    #
    # Create numpy array from file
    #
    if file_extension == '.npy':
        data = np.load(fpath)

    elif file_extension == '.txt':
        data = np.loadtxt(fpath)

    elif file_extension == '.csv':
        data = np.loadtxt(fpath, delimiter=',')
    
    #
    # Append feature names
    #
    if features:
        features = np.array(features)
        data = np.vstack(features, data)
    
    #
    # Create h5
    #
    h5_fpath = Path(fpath) \ fname \ '.hdf5'  
    with h5py.File(h5_fname, 'w') as f:
        f.create_dataset(h5_fname, dtype=dtype)

