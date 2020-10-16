<h1 align="center">
    Project Template
</h1>

<p align="center">
    <strong>Template setup for project repositories.</strong>
</p>

<p align="center">
    <a href="https://hub.docker.com/r/mltooling/TODO" title="Docker Image Version"><img src="https://images.microbadger.com/badges/version/mltooling/TODO.svg"></a>
    <a href="https://hub.docker.com/r/mltooling/TODO" title="Docker Image Metadata"><img src="https://images.microbadger.com/badges/image/mltooling/TODO.svg"></a>
    <a href="https://hub.docker.com/r/mltooling/TODO" title="Docker Pulls"><img src="https://img.shields.io/docker/pulls/mltooling/TODO.svg"></a>
    <a href="https://github.com/mltooling/project-template/commits/" title="Last Commit"><img src="https://img.shields.io/github/last-commit/mltooling/project-template"></a>
    <a href="https://github.com/mltooling/project-template/blob/main/LICENSE" title="Project License"><img src="https://img.shields.io/badge/License-MIT-green.svg"></a>
    <a href="https://api.reuse.software/info/github.com/mltooling/project-template" title="REUSE status"><img src="https://api.reuse.software/badge/github.com/mltooling/project-template"></a>
</p>

<p align="center">
  <a href="#getting-started">Getting Started</a> •
  <a href="#features">Features & Screenshots</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#support--feedback">Support</a> •
  <a href="https://github.com/mltooling/project-template/issues/new?labels=bug&template=01_bug-report.md">Report a Bug</a> •
  <a href="#faq">FAQ</a> •
  <a href="#contribution">Contribution</a> •
  <a href="./CHANGELOG.md">Changelog</a>
</p>

Every project should contain a short description here to help users understand what it does. This description should cover a maximum of 4 lines. If there is a UI, you can also put a screenshot under this description.

## Highlights

- 📄 README template with predefined structure.
- 🗃 Labeling and issue organization system.
- 📝 Contribution guideline template.

## Getting Started

_This section should contain the simplest and most basic way to run and use the project, preferably with one command._

## Support & Feedback

This project is maintained by [Benjamin Räthlein](https://twitter.com/raethlein), [Lukas Masuch](https://twitter.com/LukasMasuch), and [Jan Kalkan](https://www.linkedin.com/in/jan-kalkan-b5390284/). Please understand that we won't be able to provide individual support via email. We also believe that help is much more valuable if it's shared publicly so that more people can benefit from it.

| Type                     | Channel                                              |
| ------------------------ | ------------------------------------------------------ |
| 🚨 **Bug Reports**       | <a href="https://github.com/mltooling/project-template/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+label%3Abug+sort%3Areactions-%2B1-desc+" title="Open Bug Report"><img src="https://img.shields.io/github/issues/mltooling/project-template/bug.svg?label=bug"></a>                                 |
| 🎁 **Feature Requests**  | <a href="https://github.com/mltooling/project-template/issues?q=is%3Aopen+is%3Aissue+label%3Afeature+sort%3Areactions-%2B1-desc" title="Open Feature Request"><img src="https://img.shields.io/github/issues/mltooling/project-template/feature.svg?label=feature"></a>                                 |
| 👩‍💻 **Usage Questions**   |  _tbd_ |
| 🗯 **General Discussion** | _tbd_ |
| ❓ **Other Requests** | <a href="mailto:team@mltooling.org" title="Email ML Tooling Team"><img src="https://img.shields.io/badge/email-ML Tooling-green?logo=mail.ru&style=flat-square&logoColor=white"></a> |

## Features

_Use this section for advertising the most important features and advantages of the project. Also, add screenshots or examples to showcase important features. The main purpose of this section is marketing._

## Documentation

_Either put the documentation here or use a deployed documentation site via mkdocs and link to the documentation._

Please refer to [our documentatation](#TODO) for information about deployment or usage.

## FAQ

<details>
<summary><b>This is the example description of an faq item</b> (click to expand...)</summary>
</details>

## Known Issues

<details>
<summary><b>This is the example description of a known issue</b> (click to expand...)</summary>
</details>

## Contributors

_TODO: Add sourcerer [hall of fame](https://github.com/sourcerer-io/hall-of-fame) here._

## Contribution

- Pull requests are encouraged and always welcome. Read our [contribution guidelines](https://github.com/mltooling/project-template/tree/main/CONTRIBUTING.md) and check out [help-wanted](https://github.com/mltooling/project-template/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+label%3A"help+wanted"+sort%3Areactions-%2B1-desc+) issues.
- Submit Github issues for any [feature request and enhancement](https://github.com/mltooling/project-template/issues/new?assignees=&labels=feature&template=02_feature-request.md&title=), [bugs](https://github.com/mltooling/project-template/issues/new?assignees=&labels=bug&template=01_bug-report.md&title=), or [documentation](https://github.com/mltooling/project-template/issues/new?assignees=&labels=documentation&template=03_documentation.md&title=) problems.
- By participating in this project, you agree to abide by its [Code of Conduct](https://github.com/mltooling/project-template/tree/main/CODE_OF_CONDUCT.md).
- The [development section](#development) below contains information on how to build and test the project after you have implemented some changes.

## Development

To simplify the process of building this project from scratch, we provide build-scripts that run all necessary steps (build, test, and release) within a containerized environment. While it is not recommended, you can also run the build process on your local environment by using the `--local` argument.

### Requirements

- Python, Docker

### Build

Execute this command in the project root folder to compile, assemble, and package all project components:

```bash
python build.py --build
```

You can also run the build for a specific (sub-)component by running the `build.py` script from the component folder. 

For additional script options, run:

```bash
python build.py --help
```

### Test

Once all the project artifacts are build, you can execute this command in the project root folder to run the integration and unit tests for all components:

```bash
python build.py --test
```

To only test a specific component, execute the `build.py` script in the root of the component folder. You can also combine the build and test steps into one command as shown below:

```bash
python build.py --build --test
```

### Release

To release a new version and publish all relevant artifacts to respective registries (e.g. Docker image to DockerHub), execute:

```bash
python build.py --build --test --release --version=<MAJOR.MINOR.PATCH>
```

To trigger the release, the version and test argument must be provided. The version format must follow the [Semantic Versioning](https://semver.org/) standard: `MAJOR.MINOR.PATCH`.

---

Licensed **MIT**. Created and maintained with ❤️ by developers from Berlin.
