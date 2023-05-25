import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Available Options")
    parser.add_argument("-p", "--prompt", dest="prompt", required=True)
    args = vars(parser.parse_args())
    return args
