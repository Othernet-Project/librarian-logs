import datetime

from os.path import basename, dirname, splitext

from bottle import request, static_file

from librarian_version.version import get_base_version


def send_logfile(log_path):
    version = get_base_version(request.app.config) or ''
    log_dir = dirname(log_path)
    filename = basename(log_path)
    (name, ext) = splitext(filename)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    params = dict(name=name, version=version, timestamp=timestamp, ext=ext)
    new_filename = '{name}_{version}_{timestamp}{ext}'.format(**params)
    return static_file(filename, root=log_dir, download=new_filename)


def send_applog():
    log_path = request.app.config['logging.output']
    return send_logfile(log_path)


def send_syslog():
    log_path = request.app.config['logging.syslog']
    return send_logfile(log_path)


def routes(config):
    app_name = config['app.name']
    opts = dict(no_i18n=True, unlocked=True, skip=config['app.skip_plugins'])
    return (
        ('sys:app_log', send_applog, 'GET', '/{0}.log'.format(app_name), opts),
        ('sys:syslog', send_syslog, 'GET', '/syslog', opts),
    )
