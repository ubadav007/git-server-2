("Vikas git commands")
sudo su -  -Switch to super user
yum install git -y  - To install git 
git --version - To check if git is installed
mkdir git-15-02 - To make a folder
cd git-15-02/ - To go inside the folder 
pwd - check the path where you are currently
git init - Initialize an empty git repo .git folder is created
ls -la  - See the hidden .git folder
nano sample.py - Create a sample file 
cat sample.py - View the content
git status - Check which file has been changed .It reflects in red colour.
git add sample.py - To move from working area to staging arae
git status - Check if file has moved to staging area
git commit -m "First commit" - To move the changes from staging area to local branch
git config --global user.name "vikas99341"
git config --global user.email "vikasisinlove@gmail.com"
git config --list  - to congiure your git hub with git 
git branch - To check on which branch you are 
git branch -M main -  To make main as my default branch instead of master
git branch - To check that branch changed from master to main
git remote add origin https://github.com/vikas99341/git-15-02.git - Adding remote path (use existing repo or add new and use URL)
git remote -v - Checking the remote path
git push -u origin main - Pushing the chages from local to git hub 
