import os
os_env = os.eviron.copy()
import argparse
import sys
import shutil
import valve.valve_control

class PolyFlow_CLI():
    """
    Class to help with PolyFlow CLI
    
    """

    def __init__(self):

        description = "PolyFlow CLI"
        args = parser.parser_args()

        # Check for args
        if not getatter(args, 'command', False):
            args.parser.print_help()
            sys.exit(1)

        self.dispatch_command(args)
     
     def configure_parser(self, description):
         """
         Setup internal CLI using argparser

         """

         #
         # Parent parser
         #
         parentp = argparse.ArgumentParser(prog='PolyFlow',
                                           description=description,
                                           epilog='')
         parentp.set_defaults(parser-core)

         #
         # Child subparser group
         #
         childp = core.add_subparsers(dest='command')

         #
         # 'setup' command subparser
         #
         setup_parser = childp.add_parser('setup', help='Setup option for PolyFlow')
         setup_parser.add_argument('--mode', '-m', choices = ['all', 'preprocessing', 'training', 'inference'])
         setup_parser.set_defaults(parser=setup_parser)

         #
         # 'run' command subparser
         #
         run_parser = childp.add_parser('run', help='Run a specified step in PolyFlow')
         run_parser.set_defaults(parser=run_parser)
         
         # setup step commands
         run_subparser = run_parser.add_subparsers(dest='command')

         # Preprocess
         preprocess_parser = run_subparser.add_parser('preprocess', 
                             help='Execute preprocessing step of PolyFlow')
         # Train
         train_parser = run_subparser.add_parser('train', 
                        help='Execute model training step of PolyFlow')
         # Add train options
         train_parser.add_argument('--use_feat', help='Use FEAT to create seeds for Bingo')

         #Inference
         inf_parser = run_subparser.add_parser('inference', 
                      help='Execute inference step of PolyFlow')

        for parser in [preprocess_parser, train_parser, inf_parser]:
            parser.add_argument('--config_file', '-c', type=str, required=True,
                    help='Configuration file for workflow')

            #
            # Connection maestro to PolyFlow commands
            #
            maestro_parser = parser.add_argument_group('maestro args', 'Arguments to pass to maestro')
            maestro_parser.add_argument('--dry', action='store_true',
                    help='Generate all work directories including slurm scripts but do not submit to HPC resource')
            maestro_parser.add_argument('--rlimit', '-r', action='store_true', 
                    help='Maximum number of Maestro restarts allowed.')
            maestro_parser.add_argument('--debug', action='store_true', 
                    help='Enable DEBUG logging in Maestro')

        return parentp

    def dispatch_command(self, args):
        """
        Helper to execute commands

        Parameters
        ----------
        args: argparser.Namespace
            Parsed arguments from argparser
        """

        getattr(self.args.command)(args=args)

    def run(self, args):
        """
        functionality of 'run' command

        Parameters
        ----------
        args: argparser.Namespace
            CLI args obtained from ArgumentParser

        """

        getattr(self, args.command)(args=args)
    
    def setup(self, args):
        """
        Functionality for setup command. 

        This is used to generate config files

        Parameters:
        -----------
        args: argparse.Namespace
            CLI args from ArgumentParser

        """
        if not getattr(args, 'mode', False):
            args.parser.print_help()
            sys.exit(1)

        config_path = ######
        new_config_file = args.config_file

        if not validate_is_yaml(new_config_file): #########
            new_config_file = '.'.join([new_config_file, 'yaml'])
        if 'all' in args.mode:
            shutil.copy(config_path, new_config_file)
        else:
            entries = ['store_path'] + args.mode
            blueprint_data = load_yaml(config_path)
            requested_data = {k: blueprint_data[k] for k in entries}
            dump_yaml(data=requested_data, filename=new_config_file)

        msg  = f'Default config file generated @ '{new_config_file}'.'
        msg += f'Edit this file to fit your needs.'

        print(msg)

    def preprocessing(self, args):
        """
        Run the preprocessing portion of PolyFlow.

        Parameters:
        -----------
        args: argparse.Namespace
            CLI args from ArgumentParser

        """

        if not getattr(args, 'config_file', False)
            args.parser.print_help()
            sys.exit(1)

        config_file = args.config_file
        mode        = args.command
        validated   = validate_user_config_file(config_file, mode )##########
        variables   = validated[mode]['env']['variables']
        store_path  = validated['store_path']

        store = kosh.connect(store=store_path)
        coordinator.validate_kosh_store(store=store) #############
        
        valve_control.Preprocess(config_data=validated, cli_args=args, env=os_env).run()
        


def start_cli():
    """
    CLI entry point called in setup.py
    """
    PolyFlow_CLI()

if __name__ == '__main__':
    PolyFlow_CLI()
