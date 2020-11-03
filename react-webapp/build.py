from universal_build import build_utils

args = build_utils.get_sanitized_arguments()

build_utils.log("Install essentials")
build_utils.run("yarn install")

if args[build_utils.FLAG_CHECK]:
    build_utils.log("Run linters:")
    build_utils.run("yarn run lint:js", exit_on_error=True)
    build_utils.run("yarn run lint:css", exit_on_error=True)
    build_utils.log("No linter problems")

if args[build_utils.FLAG_MAKE]:
    build_utils.log("Build the webapp:")
    build_utils.run("yarn build", exit_on_error=True)

if args[build_utils.FLAG_TEST]:
    build_utils.log("Test the webapp:")
    build_utils.run("yarn test a --watchAll=false", exit_on_error=True)
