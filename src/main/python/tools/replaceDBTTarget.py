import argparse
import os


def get_profiles_file():
    profiles_file = os.environ['USERPROFILE'] + '/.dbt/profiles.yml'
    return profiles_file


def replace_in_file(file_name, from_target, to_target):
    fin = open(file_name, "rt")
    data = fin.read()
    fin.close()

    data = data.replace('target: ' + from_target, 'target: ' + to_target)

    fin = open(file_name, "wt")
    fin.write(data)
    fin.close()


def parse_cli():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument('--from_target',
                        required=True,
                        action='store',
                        type=str,
                        dest='from_target')

    parser.add_argument('--to_target',
                        required=True,
                        action='store',
                        type=str,
                        dest='to_target')

    cli_args = parser.parse_args()
    # print(vars(cli_args))
    return cli_args


def main():
    cli_args = parse_cli()
    profiles_file = get_profiles_file()
    replace_in_file(profiles_file, cli_args.from_target, cli_args.to_target)


if __name__ == "__main__":
    main()
