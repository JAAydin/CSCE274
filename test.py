import os
 
df = open("./Dockerfile", "r").readlines()

REPO_NAME = df[1]
DESCRIPTION = df[2]
MAINTAINER = df[3] 

def test_repo_name():
 assert REPO_NAME != 'ARG REPO_NAME="<REPO_NAME_HERE>"\n', 'FAILED: Should change the REPO_MAME arg in the Docketfile'

def test_description():
 assert DESCRIPTION != 'ARG DESCRIPTION="<DESCRIPTION_HERE>"\n', 'FAILED: Should change the DESCRIPTION arg in the Docketfile'

def test_maintainer():
 assert MAINTAINER != 'ARG MAINTAINER="<YOUR_FULL_NAME> (<YOUR_EMAIL_ADDRESS>)"\n', 'FAILED: Should change the MAINTAINER arg in the Docketfile'
