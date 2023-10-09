from enum import Enum
from schema import Schema, And, Use, Optional, SchemaError

"""
Schemas are here to validate that the config files
are written correctly and the data types are valid.
Config files contain the command line arguments that
are passed to the various Python files running within 
PolyFlow. For instance, if you wanted to added a store
path in your config file that wasn't a string literal,
the schema validation would catch it.

"""

#
# Define some helpful validation functions using 
# the schema library
#



#
# Preprocessing config validation
#
#preprocessing_schema = {
#    'store_path': store_path,
#    'microstructure_data_dir': microstructure_data_dir,
#    'convert_to_h5': convert_to_h5,
#    'ensemble_metdata': ensemble_metadata,
#    'sve_metadata': sve_metadata,
#    'ensemble_size': ensemble_size,
#    'features': features}

#
# Training config validation
#

#
# Inference config validation
#

#
# Overall config validation
#
#config_file{
#    'store_path': store_path
#    'preprocessing': preprocessing_schema,
#    'training': training_schema,
#    'inference': inference_schema}


