import os

from universal_build import build_utils

DEPENDENCY_HINT_MSG = {
    "Please make sure you have the dependencies installed. "
    "To install all dependencies, run: \n"
    "pip install mkdocs mkdocs-material pygments pymdown-extensions markdown-include"
}

HERE = os.path.abspath(os.path.dirname(__file__))
# set current path as working dir
os.chdir(HERE)

args = build_utils.get_sanitized_arguments()

if args[build_utils.FLAG_MAKE]:
    build_utils.log("Build documentation:")
    exit_code = build_utils.run("mkdocs build").returncode
    if exit_code > 0:
        build_utils.log(f"Failed to build mkdocs documentation. {DEPENDENCY_HINT_MSG}")
        build_utils.exit_process(exit_code)

if args[build_utils.FLAG_CHECK]:
    build_utils.log("Run linters and style checks:")
    build_utils.run(
        "markdownlint --config='.markdown-lint.yml' ./docs", exit_on_error=True
    )

if args[build_utils.FLAG_RELEASE]:
    build_utils.log("Release documentation:")
    build_utils.run("mkdocs gh-deploy --clean", exit_on_error=True, timeout=120)

if args[build_utils.FLAG_RUN]:
    build_utils.log("Run docs in development mode (http://localhost:8001):")
    exit_code = build_utils.run(
        "mkdocs serve --dev-addr 0.0.0.0:8001", exit_on_error=True
    )
    if exit_code > 0:
        build_utils.log(f"Failed to run mkdocs documentation. {DEPENDENCY_HINT_MSG}")
        build_utils.exit_process(exit_code)
