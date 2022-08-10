# github repo automation

inspired by Kalle Halden's script to make the same automation script on my own

## install & setup

```bash
git clone "https://github.com/bruhtazor/init-automation.git"
cd init-automation
pip install -r requirements.txt
source ~/path/to/folder/.command.sh
```

## access token 

for the script to access your github account you're going to need to create an access token

github's doc on how to do that : 
https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

once you have your token find the following line and put your token

```python
#variables used for github access
access_token = ""
```
## last step

last step is to enter your username in the .command.sh file and then you're ready to go

```bash
git remote add origin git@github.com:<your username>/$1.git
```
## WIP
the code needs improvements and I'm working on it, any pull requests are welcome