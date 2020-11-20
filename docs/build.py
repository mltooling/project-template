import os

from universal_build import build_utils
from universal_build.helpers import build_mkdocs

HERE = os.path.abspath(os.path.dirname(__file__))


def main(args: dict):
    # set current path as working dir
    os.chdir(HERE)

    if args.get(build_utils.FLAG_MAKE):
        # Install pipenv dev requirements
        build_mkdocs.install_build_env()
        # Build mkdocs documentation
        build_mkdocs.build_mkdocs()

    if args.get(build_utils.FLAG_CHECK):
        build_mkdocs.lint_markdown()

    if args.get(build_utils.FLAG_RELEASE):
        # Deploy to Github pages
        build_mkdocs.deploy_gh_pages()
        # Lock pipenv requirements
        build_utils.run("pipenv lock")

    if args.get(build_utils.FLAG_RUN):
        build_mkdocs.run_dev_mode()


if __name__ == "__main__":
    args = build_utils.get_sanitized_arguments()
    main(args)
