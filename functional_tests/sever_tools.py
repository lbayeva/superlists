#from os import path
#import subprocess
#     
#THIS_FOLDER = path.dirname(path.abspath(__file__))
#
#def create_session_on_server(host, email):
#    return subprocess.check_output(
#            [
#                'fab',
#                'create_session_on_server:email={}'.format(email),
#                '--host={}'.format(host),
#                '--hide=everything,status',
#            ],
#            cwd=THIS_FOLDER
#    ).decode().strip()
#
#def reset_database(host):
#    subprocess.check_call(
#             ['fab', 'reset_database', '--host={}'.format(host)],
#             cwd=THIS_FOLDER
#    )
#
from fabric.api import env, run

def _get_base_folder(host):
    return '~/sites/' + host

def _get_manage_dot_py(host):
    return '{path}/virtualenv/bin/python {path}/source/manage.py'.format(
                path=_get_base_folder(host)
            )

def reset_database():
    run('{manage_py} flush --noinput'.format(
            manage_py=_get_manage_dot_py(env.host)
    ))

def create_session_on_server(email):
    session_key = run('{manage_py} create_session {email}'.format(
        manage_py=_get_manage_dot_py(env.host),
        email=email,
    ))
    print(session_key)
