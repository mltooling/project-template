import nox

# TODO: Remove duplicate declaration (setup.py, noxfile.py, build.py)
MAIN_PACKAGE = "template_package"


@nox.session(python=["3.8", "3.7", "3.6"])
def test(session):
    session.run(
        "pip",
        "install",
        "-e" ".[dev]",
    )
    # Execute tests with coverage check
    session.run(
        "python",
        "-m",
        "pytest",
        "-s",
        f"--cov={MAIN_PACKAGE}",
        "--cov-report=xml",
        "--cov-report",
        "term",
        "--cov-report=html",
        "tests",
    )
