---
title: Windows FAQs
---

## Windows FAQs

### Does InspIRCd run on Windows?

Yes. InspIRCd runs natively on Windows. We also ship an easy-to-use installer that is recommended over building from source.

### Where does InspIRCd install to?

By default InspIRCd installs into `C:\Program Files\InspIRCd` on 32-bit Windows and `C:\Program Files (x86)\InspIRCd` on 64-bit Windows. You may change this at install time.

### How do I use a module that is not included with the installer?

If you want to use a third-party module or an extra module that is not built by the installer you must build your entire server from scratch. More details about how to do this can be found by downloading the InspIRCd source code and reading `win\README`.

### My antivirus claims that InspIRCd is malware!

This is a false positive. IRC software is often mistaken for malware as it used to be common for cybercriminals to use IRC servers to control their botnets.

If your antivirus software is claiming that InspIRCd is malware you should probably report it to your antivirus vendor as a false-positive or switch to a different antivirus program.
