# coding=utf-8

from fabric.api import env
from fabric.api import roles, task, run, cd

env.roledefs = {'production': ['starenka@galanta-uctovnictvo.sk']}


@roles('production')
@task
def deploy():
    BRANCH = 'master'
    APP_DIR = '/www/galanta-uctovnictvo.sk'
    NODENV_CMD = '~/.nodenv/bin/nodenv'
    NPM_CMD = '~/.nodenv/shims/npm'

    with cd(APP_DIR):
        run('git fetch')
        run('git reset --hard origin/%s' % BRANCH)

        run('yes | %s install' % NPM_CMD)
        run('%s run build' % NPM_CMD)
