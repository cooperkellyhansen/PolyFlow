# Import PyTexture
import kosh
import argparse
from PyTexture.core import Orientation

def main():
    """
    We will query our Kosh store here for SVE data and create orientation
    objects from it. The Orientation class in PyTexture allows us to 
    validate that the orientation matrix is valid. 
    
    """
    parser = argparser.ArgumentParser() 
    parser.add_argument('--store_path', required=True)
    parser.add_argument('--orientation_type', required=True,
            choices=['rodrigues', 'quaternion',
                     'euler', 'miller', 'angle_axis',
                     'rotation_mat'])
    parser.add_argument('--unit_cell_type', required=True, 
            choices=['FCC', 'HCP'])

    store_path = args.store_path
    orientation_type = args.orientation_type
    unit_cell_type = args.unit_cell_type

    #
    # Open Kosh store
    #
    store = kosh.connect(store=store_path)

    #
    # Query store for SVE datasets
    #
    sve_ds_list = list(
              store.find(ds_tag = DatasetEnum.SVE.name,
                         data_state_var = StateEnum.RAW.name,
                         has_data=True
                         )
              )

    #
    # Ensure that orientation features exist in any
    # PyTexture compatible format (i.e., rod, quat, euler)
    #
    for sve_ds in sve_ds_list:
        msg  = 'No grain orientation information found in '
        msg += f'{sve_ds.name} dataset. This will need to '
        msg += 'be added in order to validate the grain data.'
        assert 'orienation', sve_ds.list_features(), msg

    orientation_type_map = {'rodrigues': Orientation.fromRodrigues,
                            'quaternion': Orientation.fromQuaternion,
                            'euler': Orientation.fromEulerAngles,
                            'miller': Orientation.fromMillerIndices,
                            'angle_axis': Orientation.fromAngleAxis,
                            'rotation_mat' ,Orientation.fromRotationMatrix}
    #
    # Build and validate orienation objects
    #
    for sve_ds in sve_ds_list:
        # Build Texture
        o = Orientation()
        o.
        # Validate
        ##BUILD##

    #
    # Store this data back in the dataset for 
    # optional use.
    #
    # Pickle and cache the texture objects 

    # Add to Kosh store


if __name__ == '__main__':
    
    if rank == 0:
        main()

