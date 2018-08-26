"""This wrapper reads the options from hassio's add-on mechanism and then
executes pagekite with the appropriate arguments.

It is written in Python (compatible with both 2 and 3) for easier access to
configuration options, because Python needs to be available for PageKite
anyway."""

from __future__ import unicode_literals, print_function

import os
import sys

import json

config = json.load(open("/data/options.json"))

print("Read configuration:")
print(repr(config))

configerrors = False

kitename = config.get('kitename')
if not kitename or '<' in kitename or ' ' in kitename:
    print("Wrapper error: kitename has to be set to a custom name in the configuration.")
    configerrors = True

kitesecret = config.get('kitesecret')
if not kitesecret or kitesecret == u"<Fill this in from your pagekite account>":
    print("Wrapper error: kitesecret needs to be set.")
    configerrors = True

ssh = bool(config.get('ssh'))

if configerrors:
    sys.exit(1)

pagekiteargs = ["--clean", "--defaults", "--service_on", "http:" + kitename + ":localhost:8123:" + kitesecret]
if ssh:
    pagekiteargs.extend(["--service_on", "ssh:" + kitename + ":localhost:22:" + kitesecret])
pyargs = ["/src/pagekite.py"] + pagekiteargs
args = ["/usr/bin/python2"] + pyargs
# print("Execing", " ".join(args))
sys.stdout.flush()
os.execv(args[0], args)
