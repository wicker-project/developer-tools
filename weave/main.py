import jinja2 as j2
import argparse
from os import walk, path, remove
from pathlib import Path


def setup_parser(templates: dict[str, str]) -> argparse.ArgumentParser:
    # create parser
    parser = argparse.ArgumentParser(
        prog="Weave",
        description="Canned template CLI tool for Wicker Project software paradigms.")

    # load parser with args
    parser.add_argument("className", help="Name of class to use in templater")
    parser.add_argument("template",
                        help="name of selected template",
                        choices=templates.keys())
    parser.add_argument("-o", "--output")
    return parser


def report_result(user_args: argparse.Namespace, result: str) -> None:
    # if user specifies a target output file
    if user_args.output != None:
        original_filename: str = user_args.output.split(".")[0]
        output_file: str = user_args.output
        i: int = 1
        # loop over existing files with iteration counter until a new filename is generated
        while (path.exists(output_file)):
            # split by optional '.' and append counter to base name, and rebuild extension
            output_file = original_filename + \
                str(i) + "." + \
                ".".join(output_file.split(".")[1:])
            i += 1

        write_file = open(output_file, "w+")
        write_file.write(result)
        write_file.close()
        print(f"Result written to: {output_file}")

    # else just print to console
    else:
        print("=====================================================")
        print(
            f"Applied '{user_args.className}' to template: {user_args.template}")
        print("=====================================================")
        print(f"\n{result}\n")
        print("=====================================================")


if __name__ == "__main__":

    # starting vars
    template_dir: str = "./templates"

    # get current list of available templates from template folder
    template_files: dict[str, str] = {}
    for (dirpath, dirnames, filenames) in walk(template_dir):
        for file in filenames:
            # key is file basename, and value is current filepath
            template_files[Path(file).stem.split(".")[0]] = file

    # establish argument parser and get user data from it
    parser: argparse.ArgumentParser = setup_parser(template_files)
    user_args: argparse.Namespace = parser.parse_args()

    # create jinja environment
    env: j2.Environment = j2.Environment(
        loader=j2.FileSystemLoader("./templates"),
        autoescape=j2.select_autoescape())

    # handle output logic
    print(f"Output location: {user_args.output}")

    # handle template selection
    template: j2.Template = env.get_template(
        template_files[user_args.template])

    # generate output from template and className
    result: str = template.render(classname=user_args.className)

    # write to optional output file, or print to console
    report_result(user_args, result)
