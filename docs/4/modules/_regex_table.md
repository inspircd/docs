<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

The following regular expression engines are included with InspIRCd:

Engine   | Module                                  | Description
-------- | --------------------------------------- | -----------
glob     | [regex_glob](/4/modules/regex_glob)     | Matches using a glob pattern.
pcre     | [regex_pcre2](/4/modules/regex_pcre2)   | Matches using a [PCRE](https://www.debuggex.com/cheatsheet/regex/pcre) regular expression.
posix    | [regex_posix](/4/modules/regex_posix)   | Matches using a [POSIX](http://man7.org/linux/man-pages/man7/regex.7.html) regular expression.
re2      | [regex_re2](/4/modules/regex_re2)       | Matches using a [RE2](https://github.com/google/re2/wiki/Syntax) regular expression.
stdregex | [regex_stdlib](/4/modules/regex_stdlib) | Matches using a [C++11 `std::regex`](http://cpprocks.com/files/c++11-regex-cheatsheet.pdf) regular expression.
