from service import readExcel
from service import actualsService
from util import dbUtils as db
from service import actualsDao
import argparse

def main():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument('command',
                        metavar='command',
                        action='store',
                        choices=['PR14base', 'PR14submeasures', 'PR19base', 'PR19update'],
                        help='Select which type of data to process')

    parser.add_argument('--input_file',
                       required=True,
                       action='store',
                       type=str,
                       dest='input_file')

    parser.add_argument('--comment',
                       required=False,
                       action='store',
                       type=str,
                       dest='comment')

    parser.add_argument('--user',
                       required=True,
                       action='store',
                       type=str,
                       dest='user')

    parser.add_argument('--log_file',
                       required=False,
                       action='store',
                       type=str,
                       dest='log_file',
                       default='..\outcomes.log')

    parser.add_argument('--test',
                       action='store_true',
                       dest='test_run')

    cli_args = parser.parse_args()
    print(vars(args))

    if ('PR14base' == args.command):
        readExcel.upload_data_PR14_base(cli_args)
    elif ('PR14submeasures' == args.command):
        readExcel.upload_data_PR14_submeasues(cli_args)
    elif ('PR19base' == args.command):
        readExcel.upload_data_PR19_base(cli_args)
    elif ('PR19update' == args.command):
        if (None == args.comment):
            print('error: the following arguments are required: -c/--comment')
            exit()
        actualsService.process_actuals(cli_args)

        
if __name__ == "__main__":
    main()