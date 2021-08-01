<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

InspIRCd supports five types of mode:

Type      | Parameter when adding?       | Parameter when removing?     | Can be set multiple times?                                        | Description
--------- | ---------------------------- | ---------------------------- | ----------------------------------------------------------------- | -----------
Switch    | No                           | No                           | No                                                                | Toggles the behaviour of a feature on a channel or user.
Parameter | Yes                          | No                           | No                                                                | Enables and configures the behaviour of a feature on a channel or user.
ParamBoth | Yes                          | Yes                          | No                                                                | The same as a Parameter mode only the parameter must be specified to remove it.
Prefix    | Yes; channel member nickname | Yes; channel member nickname | Yes; once per channel member                                      | Grants/revokes a status rank to the user specified in the parameter.
List      | Yes                          | Yes                          | Yes; up to the [maximum list size](/3/configuration/#ltmaxlistgt) | Adds/removes entries from a list.
