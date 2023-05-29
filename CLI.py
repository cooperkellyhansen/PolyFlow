import os
os_env = os.eviron.copy()
import argparse
import sys


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

         #
         # run command
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

    def dispatch_command(self, args):
        """
        Helper to execute commands

        """

        getattr(self.args.command)(args=args)

    def run(self, args):
        """
        functionality of 'run' command

        """

        getattr(self, args.command)(args=args)



def start_cli():
    """
    CLI entry point called in setup.py
    """
    PolyFlow_CLI()

if __name__ == '__main__':
    PolyFlow_CLI()
