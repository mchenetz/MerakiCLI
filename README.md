# MerakiCLI
MerakiCLI is a command line program that tokenizes the commands and sends them through REST to Meraki.

This is a work in progress. Error checking is needed and formatting is needed on data input. See bekow for examples.

# Instructions #
get: just type the actual path listed in the rest documentation minus the backslashes
put: add a json data value as first arg and then the REST path.
post: add a json data value as first arg and then the REST path.

# Examples: #
`python3 ./merakicli.py get networks L_000000000000000000 devices`

`python3 ./merakicli.py get networks L_000000000000000000 ssids 1`

`python3 ./merakicli.py put {\"name\”:\”test\"} networks L_000000000000000000 devices AAAA-BBBB-CCCC`

