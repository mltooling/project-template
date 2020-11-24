from typing import Dict, List, Union

from universal_build import build_utils


def main(args: Dict[str, Union[str, bool, List[str]]]):
    """Execute all component builds."""
    # Build react webapp
    # build_utils.build("react-webapp", args)
    # Build python lib
    build_utils.build("python-lib", args)

    if args[build_utils.FLAG_MAKE]:
        # Duplicate api docs into the mkdocs documentation
        build_utils.duplicate_folder("./python-lib/docs/", "./docs/docs/api-docs/")

    # Build mkdocs documentation
    build_utils.build("docs", args)


if __name__ == "__main__":
    # Check for valid arguments
    args = build_utils.get_sanitized_arguments()

    if args[build_utils.FLAG_RELEASE] and not args[build_utils.FLAG_FORCE]:
        # Run main without release to see whether everthing can be built and all tests run through
        main({**args, build_utils.FLAG_RELEASE: False})
        # Run main again with only executing release with force flag
        main(
            {
                **args,
                build_utils.FLAG_MAKE: False,
                build_utils.FLAG_TEST: False,
                build_utils.FLAG_CHECK: False,
                build_utils.FLAG_FORCE: True,
            }
        )
    else:
        main(args)
