"""
The valve control defines the functions that the command line
interface will use for the execution of the underlying Maestro
studies. 

"""

from abc import ABC, abstractclassmethod
import os
from pathlib import Path
import subprocess
import PolyFlow.plumber as plumber

# I think there are more here

class ValveControl(ABC):
    """
    ValveControl handles the submission of maestro studies, abstracting
    this complex interaction between PolyFlow and Maestro.

    Subclasses are the different workflow steps
    
    Parameters:
    -----------
    mode: str
        This string points to the portion of the config file
        used to populate a specific Maestro step
    config_data: dict
        The YAML configuration file as a dict
    cli_args: argparse.Namespace
        The command line argumanets specified by user
    blueprint_name: str
        Name of the blueprint of interest

    """

    def __init__(self,
                 mode,
                 config_data,
                 cli_args,
                 blueprint_name,
                 env=None):
        
        self.mode = mode
        self.config_data = config_data
        self.config_vars = config_data[mode]['env']['variables']
        self.cli_args = cli_args
        self.env = env
        filename = getattr(cli_args, 'config_file', blueprint_name)
        study_name = Path(filename).stem
        self.blueprint = self.configure_blueprint(blueprint_name,
                                                  config_data,
                                                  mode,
                                                  study_name)
        self.study_filepath = self.configure_study_filepath(filename)

    @abstractclassmethod
    def generate_maestro_command(*args, **kargs):
        """
        Build a maestro command for the corresponding
        study

        """
        return

    def run(self, *args, **kargs):
        """
        Launch the maestro command

        """
        self.maestro_cmd = self.generate_maestro_command(*args, **kargs)
        plumber.dump_yaml(self.study, self.study_filepath)
        subprocess.run(self.maestro_cmd, shell=True, env=self.env)
        os.remove(self.study_filepath)

    def configure_blueprint(self, blueprint_name, config_data, mode, description_name=None):
        """
        Populate a template for corresponding study using the 
        Maestro study templates found in 'foreman/blueprints'

        """
        blueprint = plumber.get_blueprint(blueprint_name,
                                          True)
        revised_blueprint = plumber.configure_blueprint(blueprint,
                                                        config_data,
                                                        mode,
                                                        description_name)

    def configure_blueprint_filepath(self, filename):
        """
        Timestamp the blueprint filename

        """
        return plumber.resolve_path(plumber.timestamp_file(filename))


    def include_maestro_args(self,cli_args):
        """
        Take CLI args and convert them into maestro specific args

        """
        # Currently I am only going to support dry. Later I will add in 
        # support for other args.
        maestro_args = '-y'
        if cli_args.dry == True
            maestro_args = ' '.join([maestro_args, '--dry'])
        
        return maestro_args

class Preprocess(ValveControl):
    """
    Run the preprocessing study

    """
    def __init__(self, config_data, cli_args, env=None):
        store_path = config_data['store_path']
        config_vars = config_data['generate_data']['env']['variables']
        env = env

        store = plumber

class Train(ValveControl):
    """
    Run the training study

    """

class Inference(ValveControl):
    """
    Run the inference study

    """


