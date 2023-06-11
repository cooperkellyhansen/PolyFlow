import os
import yaml
import posix.Path as Path

"""
The 'plumber' is a collection of tools to help the workflow
run smoothly. Some validations are also done here.

"""

def get_blueprints():
    """
    Grab the blueprint config files.

    """

def load_from_yaml(fname, mode='r', from_str=False):
    """
    Load a yaml file.

    Built for consistency

    Parameters
    ----------
    fname: str
        path of file to load
    mode: str
        open method 
    from_str: str
        load a yaml formatted string
    """

    if from_str:
        data = yaml.safe_load(fname)
    else:
        data = yaml.safe_load(open(Path(fname), mode))
    return data

def dump_to_yaml(fname, data={}, as_str=False, mode='w'):
    """
    Dump data into a yaml file

    Built for consistency

    Parameters
    ----------
    data: dict
        Data to dump
    fname: str
        Path to save yaml
    as_str: bool
        write to str rather than save
    """
    if as_str:
        result = yaml.dump(data)
    else:
        fname = resolve_path(fname)
        parent_dir = Path(fname).parent

        if not parent_dir.is_dir():
            parent_dir.mkdir(parents=True)

        with open(Path(fname), mode) as f:
            yaml.dump(data, f)

        return resolve_path(fname)

def resolve_path(fname, as_str=True):
    """
    Ensure that any path is resolved 
    or in its absolute form

    Parameters
    ----------
    fname: str
        file to resolve
    as_str: bool
        convert to str from PosixPath
    """

    if as_str == True:
       return str(Path(fname).resolve())
    else:
       return Path(fname).resolve()

def validate_is_yaml(fname):
    """
    Confirm that a given file is actually a yaml file

    Parameters:
    -----------
    fname: str
        string path to a yaml file
    """
    #Split with os
    ext = os.path.splitext(fname)[-1].lower()
    if ext == '.yaml':
        return True
    else:
        return False

def validate_is_file():
    """
    Confirm that a given fname is actually a file
    in the file system

    Parameters:
    -----------
    fname: str
        string path to a file
    """
    exists = os.path.isfile(fname)
    return exists

def validate_is_store():
    """
    Confirm that a given store path exists and
    is a kosh store

    Parameters:
    -----------
    fname: str
        string path to a kosh store
    """
    exists = os.path.isfile(fname)
    ext = os.path.splittest(fname)[-1].lower()
    
    if exists and ext == '.sql'
        return True
    else:
        return False

def validate_user_config_file():
    """
    Confirm that a user config file meets
    PolyFlow requirements

    """


