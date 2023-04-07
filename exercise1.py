#!/usr/bin/python3

import re

line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
re.search(r"ticky: INFO: ([w ]*) ", line)
# Output: <_sre.SRE_Match object; span=(29, 57), match='ticky: INFO: Created ticket '>

line1 = "May 27 11:45:40 ubuntu.local ticky: ERROR: Errorcreatingticket [#1234] (username)"
re.search(r"ticky: ERROR: ([\w ]*) ", line1)
# Output: <_sre.SRE_Match object; span=(29, 65), match='ticky: ERROR: Errorcreatingticket '>
