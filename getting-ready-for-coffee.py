#!/usr/bin/env python

import subprocess as sp

CDP_WORKSPACE_HOME = '$HOME/projects'
SSH_PRIVATE_KEY = '$HOME/.ssh/id_rsa'

def exec_interactive_cmd(cmd):
    proc = sp.Popen(cmd, shell=True, stdout=sp.PIPE)
    output=proc.communicate()[0].strip()
    return output

def softwares():
    return [
        'iterm2',
        'intellij-idea-ce',
        'atom',
        'maven',
        'blue-jeans',
        'aws-cli',

    ]

def projects():
    return [
        'cdp-analytics',
        'cdp-core',
        'cdp-schema',
        'cdp-stream',
        'dp-biz',
        'dp-tools',
        'dp-aws-tools'
    ]

def ssh_env():
    exec_interactive_cmd('ssh-agent; ssh-add '+SSH_PRIVATE_KEY)

def getting_ready_for_coffee():
    if True==True:
        exec_interactive_cmd('brew tap caskroom/cask')
        for k in softwares():
            result = exec_interactive_cmd('brew cask info '+k)
            if result.find('Error: Cask '):
                print('installing... '+ k)
                result = exec_interactive_cmd('brew install '+k)
            else:
                print('installing from cask... '+ k)
                result = exec_interactive_cmd('brew cask install '+k)
        exec_interactive_cmd('brew cleanup')

    ssh_env()
    for k in projects():
        ls = exec_interactive_cmd('cd '+CDP_WORKSPACE_HOME+'; ls | grep '+k)
        if ls==k:
            print('rebasing git repo... '+ k)
            exec_interactive_cmd('cd '+CDP_WORKSPACE_HOME+'/'+k+'; git pull -r')
        else:
            print('cloning git repo... '+ k)
            # pulling any repo only under dp-dev org
            exec_interactive_cmd('cd '+CDP_WORKSPACE_HOME+'; git clone git@code.espn.com:dp-dev/'+k+'.git')


if __name__ == '__main__':
    '''
    0. export environment variable HOME to /Users/<user>
    1. Install XCode from self serve
    2. Install brew from https://brew.sh/ 
    3. Get access to github repo and copy & paste ssh private key from ~/.ssh/id_rsa to your github account
    
    '''
    getting_ready_for_coffee()