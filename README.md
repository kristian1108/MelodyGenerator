#Magenta Melody Generator

This small bit of code acts as a simple wrapper around the Tensorflow
Magenta melody generation library. 

Users can find the full Magenta codebase here:
https://github.com/magenta/magenta

###Quickstart

####First, Create a New Virtual Environment
`virtualenv venv`

NOTE: This code expects Python 3.7+. If your base Python installation does not meet
this requirement, please ensure you're creating a virtualenv with the correct
version of Python. You can use this command to point virtualenv to the correct
version:

`virtualenv --python='/path/to/python3' venv`

####Second, Install Requirements
`pip install -r requirements.txt`

####Third, Generate A Melody!
`./new_melody.sh play`

Melodies are generated in sets of 10, which are saved in the included `melody_output`
directory. Each time you run this command, the program will randomly sample one
melody to play from these 10 generations.

###Maintenance
If your `melody_output` directory becomes unwieldy, you can easy clear it out 
by running 
`./new_melody.sh purge`