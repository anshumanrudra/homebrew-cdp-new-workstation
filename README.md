## homebrew-cdp-new-workstation (beta)
It is a developer's utility to automate a new workstation setup to install/update configured s/w apps, clone/rebase git repo.


#### pre-requisites
1. export environment variable HOME to /Users/your_userId
2. Install Xcode from self serve
3. Install brew from https://brew.sh/
4. Get access to github repo https://code.espn.com

    4.1. generate ssh key pair through cmd line <code>ssh-keygen -t rsa -b 4096 -C your_email@espn.com</code> to file ~/.ssh/id_rsa
    
    4.2. copy & paste ssh private key from ~/.ssh/id_rsa to your github account
#### how to run for now?
1. clone the repository from https://github.com/anshumanrudra/homebrew-cdp-new-workstation

2. trigger the below code in your favorite terminal

<code>python getting-ready-for-coffee.py</code>

#### open for feedback