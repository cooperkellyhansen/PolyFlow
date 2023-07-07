import os
import yaml
from pathlib import Path
import datetime
from polyflow.foreman.schemas import user_config_schema, Schema

"""
The 'plumber' is a collection of tools to help the workflow
run smoothly. Some validations are also done here.

"""
def configure_blueprint(blueprint, config_data, mode, description_name=None):
    """
    Take data from the config_data dictionary and format for
    use in a maestro study yaml (blueprint)

    """
    store_path = config_data['store_path']
    core_data = config_data[mode]
    core_data['env']['variables']['store_path'] = store_path

    to_configure = ['batch', 'env']
    for tc in to_configure:
        blueprint[tc] = core_data[tc]

    if description_name:
        blueprint['description']['name'] = str(description_name)

    return blueprint

def get_blueprint(filename, load=False):
    """
    Get filepath of config_data

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
    
    if exists and ext == '.sql':
        return True
    else:
        return False

def validate_user_config_file(config_file, mode='all', ignore_extra_keys=True):
    """
    Confirm that a user config file meets
    PolyFlow requirements

    """
    # Ensure that file exists
    if not validate_is_file(config_file):
        print('Config file not found')
        sys.exit(1)

    # Ensure that file is yaml
    if not validate_is_yaml(config_file):
        print('Config file must be a yaml file')
        sys.exit(1)

    config_data = load_yaml(config_file)

    if mode == 'all':
        test_schema = {**user_config_schema}
    elif user_config_schema.get(mode, False):
        test_schema = {mode: user_config_schema[mode]}
    else:
        print(f'Mode argument {mode} not valid')

    if not 'store_path' in test_schema:
        test_schema = {
            'store_path': user_config_schema['store_path'],
            **test_schema}
    
    config_schema = Schema(test_schema, ignore_extra_keys=ignore_extra_keys)
    validated_config_data = config_schema.validate(config_data)

    return validated_config_data

def get_timestamp(timespec='seconds'):
    """
    Create a timestamp. Generally used for timestamping files

    """
    return datetime.dateime.now().isoformat(timespec=timespec)

def timestamp_file(filename, timespec='seconds'):
    """
    Add a timestamp to a file

    """

    f = Path(filename)

    f_stamped = '_'.join([f.stem, 
                          get_timestamp(timespec),
                          f.suffix])
    return f_stamped

