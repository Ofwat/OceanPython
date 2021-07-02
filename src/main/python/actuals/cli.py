import argparse

def run():
    parser = argparse.ArgumentParser()

    my_parser.add_argument('-a',
                       action='store',
                       choices=['pr14base', 'pr19base', 'pr19update'],
                       required=True,
                       help='set the user choice to head or tail')

    my_parser.add_argument('-v',
                       '--verbosity',
                       action='store',
                       type=int,
                       dest='my_verbosity_level')

    args = my_parser.parse_args()
    print(vars(args))

if __name == '__main__':
    run()