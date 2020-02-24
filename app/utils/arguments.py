from argparse import ArgumentParser, RawDescriptionHelpFormatter


def parse_arguments():
    args_parser = ArgumentParser(
        prog='Such Wow Game',
        formatter_class=RawDescriptionHelpFormatter,
        description='Such Wow Game.',
        epilog='Author: tuenut'
    )

    args_parser.add_argument(
        '--editor-mode',
        action='store_true',
        help="Start app in editor mode."
    )

    parsed_arguments = args_parser.parse_args()

    return parsed_arguments