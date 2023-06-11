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

def validate_is_yaml():
        
def validate_is_file():

def validate_is_store():

def validate_user_config_file():


