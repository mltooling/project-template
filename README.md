<!-- markdownlint-disable MD033 MD041 -->
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
    <a href="https://github.com/mltooling/project-template/blob/main/LICENSE" title="Project License"><img src="https://img.shields.io/badge/License-MIT-green.svg"></a>
    <a href="https://api.reuse.software/info/github.com/mltooling/project-template" title="REUSE status"><img src="https://api.reuse.software/badge/github.com/sap/machine-learning-lab"></a>
    <a href="https://github.com/mltooling/project-template/actions?query=workflow%3Abuild-pipeline" title="Build status"><img src="https://github.com/mltooling/project-template/workflows/build-pipeline/badge.svg"></a>
</p>

<p align="center">
  <a href="#getting-started">Getting Started</a> •
  <a href="#features">Features & Screenshots</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#support--feedback">Support</a> •
  <a href="https://github.com/mltooling/project-template/issues/new?labels=bug&template=01_bug-report.md">Report a Bug</a> •
  <a href="#faq">FAQ</a> •
  <a href="#known-issues">Known Issues</a> •
  <a href="#contribution">Contribution</a> •
  <a href="https://github.com/mltooling/project-template/releases">Changelog</a>
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

Please refer to [our documentation](#TODO) for information about deployment or usage.

## FAQ

<details>
<summary><b>This is the example description of an faq item</b> (click to expand...)</summary>
</details>

## Known Issues

<details>
<summary><b>This is the example description of a known issue</b> (click to expand...)</summary>
</details>

## Contributors

_TODO: Add sourcerer [hall of fame](https://sourcerer.io/settings#hof) here._

## Contribution

- Pull requests are encouraged and always welcome. Read our [contribution guidelines](https://github.com/mltooling/project-template/tree/main/CONTRIBUTING.md) and check out [help-wanted](https://github.com/mltooling/project-template/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+label%3A"help+wanted"+sort%3Areactions-%2B1-desc+) issues.
- Submit Github issues for any [feature request and enhancement](https://github.com/mltooling/project-template/issues/new?assignees=&labels=feature&template=02_feature-request.md&title=), [bugs](https://github.com/mltooling/project-template/issues/new?assignees=&labels=bug&template=01_bug-report.md&title=), or [documentation](https://github.com/mltooling/project-template/issues/new?assignees=&labels=documentation&template=03_documentation.md&title=) problems.
- By participating in this project, you agree to abide by its [Code of Conduct](https://github.com/mltooling/project-template/blob/main/.github/CODE_OF_CONDUCT.md).
- The [development section](#development) below contains information on how to build and test the project after you have implemented some changes.

## Development

> _**Requirements**: [Docker](https://docs.docker.com/get-docker/) and [Act](https://github.com/nektos/act#installation) are required to be installed on your machine to execute the build process._

To simplify the process of building this project from scratch, we provide build-scripts that run all necessary steps (build, check, test, and release) within a containerized environment. To build and test your changes, execute the following command in the project root folder:

```bash
act -b -j build
```

Refer to our [contribution guides](https://github.com/mltooling/project-template/blob/main/CONTRIBUTING.md#development-instructions) for more detailed information on our build scripts and development process.

---

Licensed **MIT**. Created and maintained with ❤️ by developers from Berlin.

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fml-tooling%2Fml-hub.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fml-tooling%2Fml-hub?ref=badge_large)
