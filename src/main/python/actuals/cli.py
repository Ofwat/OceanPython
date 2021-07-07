import argparse
import os

def run():

    print('user dir ', os.environ['USERPROFILE'] + '/.dbt/profiles.yml')


    parser = argparse.ArgumentParser()
# type=argparse.FileType('r')
    parser.add_argument('command',
                        metavar='command',
                        action='store',
                        choices=['PR14base', 'PR19base', 'PR19update'],
                        help='Select which type of data to process')


    parser.add_argument('-i',
                       '--input_file',
                       required=False,
                       action='store',
                       type=str,
                       dest='input_file')
    # can we use file or directory?

    parser.add_argument('-c',
                       '--comment',
                       required=False,
                       action='store',
                       type=str,
                       dest='comment')

    parser.add_argument('-u',
                       '--user',
                       required=False,
                       action='store',
                       type=str,
                       dest='data')

    parser.add_argument('-l',
                       '--log_file',
                       required=False,
                       action='store',
                       type=str,
                       dest='log_file')

    args = parser.parse_args()
    print(vars(args))

  
        
    

if __name__ == '__main__':
    run()