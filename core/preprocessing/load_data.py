import kosh
import numpy as np
from mpi4py import MPI
import PolyFlow.utils.convert_file_to_h5


comm = MPI.COMM_WORLD
rank = comm.Get_rank()


"""
Load microstructure data from a single ensemble of SVEs
into a Kosh store. This promotes organization and good
documentation practice during development of machine learning 
models in the context of microscale fatigue.

"""

def main():
    parser = argparser.ArgumentParser()
    parser.add_argument('--store_path', required=True)
    parser.add_argument('--microstructure_data_dir', required=True)
    parser.add_argument('--convert_to_h5', default=False)
    parser.add_argument('--current_data_format', default=False, 
                        choices=['csv', 'txt', 'npy'])
    parser.add_argument('--ensemble_metdata', default={})
    parser.add_argument('--sve_metadata', default={})
    parser.add_argument('--sve_naming_convention', default='sve_')
    parser.add_argument('--ensemble_size', required=True)
    parser.add_argument('--features', default=[])

    store_path              = args.store_path
    microstructure_data_dir = args.microstructure_data_dir
    validate_d3d_data       = args.validate_d3d_data
    convert_to_h5           = args.convert_to_h5
    current_data_format     = args.current_data_format
    sve_metadata            = args.microstructure_metadata
    ensemble_metadata       = args.ensemble_metadata
    sve_naming_convention   = args.sve_naming_convention
    ensemble_size           = args.ensemble_size
    features                = args.features

    print(f'Building Kosh store @ {store_path}')
    #
    # Set up kosh store
    #
    store = kosh.connect(store=store_path)

    #
    # Gather all data from the microstructure data dir
    # NOTE: This requires that your microstructure data dir
    # only contains sve datasets. We can check for stray dirs
    # but thats about it.
    #
    sve_filenames = os.listdir(microstructure_data_dir)
    
    for sve in sve_list:
        # Check for any dirs
        if os.path.isdir(sve):
            sve_filenames.remove(sve)
            msg = f'{sve} is not a valid data file. ' 
            msg += 'It will not be added to the Kosh store unless '
            msg += 'done so manually.\n'

    #
    # Ensure that ensemble size is correct.
    #
    found_ens_size = len(sve_filenames)
    msg  = 'Size of the ensemble found by PolyFlow does not match '
    msg += 'the size specified in the configuration file.'
    assert found_ens_size = ensemble_size, msg

    #
    # Convert data to h5 format if necessary.
    #
    if convert_to_h5:
        # Make sure that the current data format has also been specified
        msg  = 'Conversion of data to h5 triggered but --current_data_format '
        msg += 'and/or --features not specificed.'
        assert features and current_data_format, msg

        print('Converting sve files to .hdf5 format')
        for f in os.listdir(microstructure_data_dir):
            # Convert microstructure data to h5
            convert_file_to_h5(f, features)

    #
    # Store data in Kosh store with proper metadata 
    #
    ens = store.create_ensemble(name='', metadata=ensemble_metadata)
    for sve_num, sve_file in enumerate(sve_filenames):
        # Parse sve metadata

        # Setup some default metadata 
        metadata = {'ds_tag': DatasetEnum.SVE.name, **sve_metadata}
        
        # Create datasets and associate
        ds = kosh.create('_'.join([sve_naming_convention, sve_num]), 
                         mime_type = 'hdf5',
                         metadata=metadata)
        ds.associate(sve_file)

    #
    # Summary
    #
    load_data_report  = 'Load data report: \n'
    load_data_report += f'Number of SVEs loaded {ensemble_size}\n'
    load_data_report += f'Ensemble id {}\n'


if __name__ == '__main__':

    if rank == 0:
        main()
