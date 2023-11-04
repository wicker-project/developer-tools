import jinja2 as j2
import argparse


def setup_parser() -> argparse.ArgumentParser:
    # create parser
    parser = argparse.ArgumentParser(
        prog="Weave",
        description="Canned template CLI tool for Wicker Project software paradigms.")

    # load parser with args
    parser.add_argument("className")
    parser.add_argument("-t", "--template")
    parser.add_argument("-o", "--output")
    return parser


if __name__ == "__main__":
    # establish argument parser and get user data from it
    parser: argparse.ArgumentParser = setup_parser()
    user_args: argparse.Namespace = parser.parse_args()

    # create jinja environment
    env: j2.Environment = j2.Environment(
        loader=j2.FileSystemLoader("./templates"),
        autoescape=j2.select_autoescape())
    template: j2.Template = env.get_template(
        "RuleOfFiveCtors.hpp.j2")

    print(template.render(classname=user_args.className))
