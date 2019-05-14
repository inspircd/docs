---
disable_toc: true
title: Release Procedure
---

## Release Procedure

Name       | Description
---------- | -------
`BRANCH`   | The branch on which the release is happening.
`PREVIOUS` | The previous release's version number or the previous branch if the release is the first on that branch.
`UPSTREAM` | The Git remote for the main InspIRCd repository.
`VERSION`  | The new release's version number.

1. Ensure that the branch tip builds with no warnings. Checking [Travis CI](https://travis-ci.com/inspircd/inspircd) is helpful as it builds with `-Werror`.
2. Update the version in `src/version.sh` and commit it.
3. Tag the release with `git tag VERSION`.
4. Run `git push UPSTREAM BRANCH` and `git push UPSTREAM VERSION`.
5. Add a [GitHub release](https://github.com/inspircd/inspircd/tags) for the VERSION on tag.
6. Generate a list of contributors for the news post using `git log --pretty='  - %aN' PREVIOUS...VERSION | sort -fu`
7. Create a news post on the website using the list of contributors from the previous step.
8. Mark the new news post as featured and unmark the old one.
9. Update the change log on the documentation site.
10. If the release is stable then update `misc.currentVersion` in the website config to VERSION.
11. Update the topic in `#InspIRCd` and `#InspIRCd.dev` on ChatSpike.
12. Post a link to the news post on the [InspIRCd Twitter account](https://twitter.com/InspIRCdTeam) and, if notable, on [/r/irc](https://old.reddit.com/r/irc/).
