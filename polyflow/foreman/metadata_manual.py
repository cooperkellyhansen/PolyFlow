"""
Defaults for Kosh metadata and cofiguration

This script is meant to validate metadata and ensure it
is of a specific and standard format.

"""

from enum import Enum, auto

#
# Dataset types
#
class DatasetEnum(Enum):
    DREAM3D_DATA = auto()
    PYTEXTURE_DATA = auto()
    INFERENCE_DATA = auto()
    TRAIN_SPLIT = auto()
    TEST_SPLIT = auto()
    VALIDATION_SPLIT = auto()
    BINGO_MODEL = auto()
    FEAT_MODEL = auto()
    BINGO_SEEDS = auto()
    RFR_MODEL = auto()

#
# Machine learning methods 
#
class MethodEnum(Enum):
    NEURAL_NETWORK = auto()
    GPSR_FEAT = auto()
    GPSR_BINGO = auto()
    RANDOM_FOREST_REGRESSOR = auto()


