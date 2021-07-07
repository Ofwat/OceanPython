from service import readExcel
from service import actualsService
from util import dbUtils as db
from service import actualsDao
import argparse

def main():
    parser = argparse.ArgumentParser()
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

    if ('PR14base' == args.command):
        readExcel.upload_data()
    elif ('PR19base' == args.command):
        readExcel.upload_data()
    elif ('PR19update' == args.command):
        if (None == args.comment):
            print('error: the following arguments are required: -c/--comment')
            exit()
        actualsService.process_actuals(args)

        
if __name__ == "__main__":
    main()