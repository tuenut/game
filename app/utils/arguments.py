from argparse import ArgumentParser, RawDescriptionHelpFormatter


def parse_arguments():
    args_parser = ArgumentParser(
        prog='Such Wow Game',
        formatter_class=RawDescriptionHelpFormatter,
        description='Such Wow Game.',
        epilog='Author: tuenut'
    )
    args_parser.add_argument(
        '--generate-repo',
        dest='generate_repo',
        default=None,
        type=str,
        choices=["json", "current"],
        help="Generate selected type of repository data."
    )

    parsed_arguments = args_parser.parse_args()

    return parsed_arguments