#! /usr/bin/python3

import re
print(re.search(r"[a-zA-z]{5}", "a ghost"));
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"));
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"));
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"));
print(re.findall(r"\w{5,10}", "I realy like strawberries"));
print(re.findall(r"\w{5,}", "I realy like strawberries"));
print(re.search(r"s\w{,20}", "I realy like strawberries"));
