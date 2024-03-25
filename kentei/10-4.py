import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--head")
parser.add_argument("body", nargs="+")
args = parser.parse_args()
print(args)
