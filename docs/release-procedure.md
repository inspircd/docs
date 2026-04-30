---
disable_toc: true
title: Release Procedure
---

## Release Procedure

Name       | Description
---------- | -------
`BRANCH`   | The branch on which the release is happening.
`UPSTREAM` | The Git remote for the main InspIRCd repository.
`VERSION`  | The new release's version number.

0. Close the [release milestone](https://github.com/inspircd/inspircd/milestones) on GitHub.
0. Run `vendor/update` to check that the vendored third-party dependencies are up to date.
0. Run `tools/mkauthors` to update the authors file.
0. Run `tools/mkdescriptions` to update the module descriptions.
0. Run `tools/mkheaders` to update the copyright headers.
0. If ABI breakages have been made then update `MODULE_ABI` in `include/moduledefs.h`.
0. Update the version in `src/version.sh` (v4) or `src/cmake/version.cmake` (v5).
0. Commit the changes to `include/moduledefs.h`, `src/version.sh`, and `src/cmake/version.cmake`` with the message `Release VERSION.`.
0. Ensure that the branch tip builds with no warnings. Checking [GitHub Actions](https://github.com/inspircd/inspircd/actions) is helpful as it builds with `-Werror`.
0. Tag the release with `git tag VERSION`.
0. Run `git push UPSTREAM BRANCH` and `git push UPSTREAM VERSION`.
0. Add a [GitHub release](https://github.com/inspircd/inspircd/tags) for the VERSION tag.
0. Update the change log on the documentation site.
0. If the release fixes a security vulnerability then create an advisory on the documentation site.
0. Create a news post on the website using the change log from the previous step.
0. Mark the new news post as featured and unmark the previous one.
0. Run the [API documentation workflow](https://github.com/inspircd/api-docs/actions/workflows/build.yml).
0. Update `INSP_VERSION` in the [Docker container build script](https://github.com/inspircd/docker/blob/master/.github/workflows/build-container.yml).
0. Update the topic in the InspIRCd IRC channels.
0. Post a link to the news post on the [InspIRCd social media accounts](/support).
0. Email package maintainers informing them of the release (if not already done in advance).
