import sys
import argparse
import converter


def main(argv):
    parser = argparse.ArgumentParser(
        description="A translator for traditional and simplified Chinese"
    )
    parser.add_argument(
        "-ts",
        "--trad2simp",
        action="store_true",
        default=False,
        help="Convert string from traditional to simplified",
    )
    parser.add_argument(
        "-st",
        "--simp2trad",
        action="store_true",
        default=False,
        help="Convert string from simplified to traditional",
    )
    parser.add_argument(
        "-ni",
        "--noidiom",
        action="store_true",
        default=False,
        help="Do not convert into local idioms when translating",
    )
    parser.add_argument("input", type=str)
    args = parser.parse_args()

    conv = None
    if args.trad2simp:
        conv = converter.Converter("ts", args.noidiom)
    elif args.simp2trad:
        conv = converter.Converter("st", args.noidiom)
    else:
        print("Please specify one option from '-ts' and '-st'")
        return

    print(conv.convert(args.input))


if __name__ == "__main__":
    main(sys.argv)
