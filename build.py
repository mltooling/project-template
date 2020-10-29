from typing import Dict, Union

from universal_build import build_utils


def main(args: Dict[str, Union[bool, str]]):
    build_utils.build("docs", args)
    build_utils.build("react-webapp", args)
    build_utils.build("java-service", args)
    build_utils.build("python-lib", args)


if __name__ == "__main__":
    # Check for valid arguments
    args = build_utils.get_sanitized_arguments()

    if args[build_utils.FLAG_RELEASE]:
        # Run main without release to see whether everthing can be built and all tests run through
        main({**args, "release": False})
        # Run main again with only executing release with force flag
        main({**args, "make": False, "test": False, "check": False, "force": True})
    else:
        main(args)
