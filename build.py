from universal_build import build_utils

args = build_utils.get_sanitized_arguments()

build_utils.build("react-webapp", args)
