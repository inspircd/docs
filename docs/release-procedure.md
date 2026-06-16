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

* [ ] Close the [release milestone](https://github.com/inspircd/inspircd/milestones) on GitHub.
* [ ] Run `vendor/update` to check that the vendored third-party dependencies are up to date.
* [ ] Run `tools/mkauthors` to update the authors file.
* [ ] Run `tools/mkdescriptions` to update the module descriptions.
* [ ] Run `tools/mkheaders` to update the copyright headers.
* [ ] If ABI breakages have been made then update `MODULE_ABI` in `include/moduledefs.h`.
* [ ] Update the version in `src/version.sh` (v4) or `src/cmake/version.cmake` (v5).
* [ ] Commit the changes to `include/moduledefs.h`, `src/version.sh`, and `src/cmake/version.cmake` with the message `Release VERSION.`.
* [ ] Ensure that the branch tip builds with no warnings. Checking [GitHub Actions](https://github.com/inspircd/inspircd/actions) is helpful as it builds with `-Werror`.
* [ ] Tag the release with `git tag VERSION`.
* [ ] Run `git push UPSTREAM BRANCH` and `git push UPSTREAM VERSION`.
* [ ] Add a [GitHub release](https://github.com/inspircd/inspircd/tags) for the VERSION tag.
* [ ] Build UNIX packages for the release using [the package builder](https://github.com/inspircd/package-builder).
* [ ] Update the change log and the version in `extra.releases` on the documentation site.
* [ ] If the release fixes a security vulnerability then create an advisory on the documentation site.
* [ ] Create a news post on the website using the change log from the previous step.
* [ ] Mark the new news post as featured and unmark the previous one.
* [ ] Run the [API documentation workflow](https://github.com/inspircd/api-docs/actions/workflows/build.yml).
* [ ] Update `INSP_VERSION` in the [Docker container build script](https://github.com/inspircd/docker/blob/master/.github/workflows/build-container.yml).
* [ ] Update the topic in the InspIRCd IRC channels.
* [ ] Post a link to the news post on the [InspIRCd social media accounts](/support).
* [ ] Email package maintainers informing them of the release (if not already done in advance).
