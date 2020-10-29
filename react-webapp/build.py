from universal_build import build_utils

args = build_utils.get_sanitized_arguments()

build_utils.log("Install essentials")
build_utils.run("yarn install")

if args[build_utils.FLAG_CHECK]:
    build_utils.log("Run linters:")
    js_linting_completed_process = build_utils.run("yarn run lint:js")
    style_linting_completed_process = build_utils.run("yarn run lint:css")

    if (
        js_linting_completed_process.returncode > 0
        or style_linting_completed_process.returncode > 0
    ):
        build_utils.log("One of the linters threw an error")
        build_utils.exit_process(1)

    build_utils.log("No linter problems")
