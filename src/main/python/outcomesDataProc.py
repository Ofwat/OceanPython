import argparse

from service import actualsService
from service import pr14BaseService
from service import pr14BaseSubmeasureService
from service import pr19BaseApp1Service
from service import pr19BaseApp1bService


def main():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument('command',
                        metavar='command',
                        action='store',
                        choices=['PR14base', 'PR14basesubmeasures', 'PR19baseapp1', 'PR19actualupdate',
                                 'PR19baseapp1b'],
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

    if 'PR14base' == cli_args.command:
        pr14BaseService.upload_data_PR14_base(cli_args)
    elif 'PR14basesubmeasures' == cli_args.command:
        pr14BaseSubmeasureService.upload_data_PR14_submeasues(cli_args)
    elif 'PR19baseapp1' == cli_args.command:
        pr19BaseApp1Service.upload_data_PR19_base(cli_args)
    elif 'PR19baseapp1b' == cli_args.command:
        pr19BaseApp1bService.upload_data_PR19_App1b_base(cli_args)
    elif 'PR19actualupdate' == cli_args.command:
        if cli_args.comment is None:
            print('error: the following arguments are required: -c/--comment')
            exit()
        actualsService.process_actuals(cli_args)


if __name__ == "__main__":
    main()
