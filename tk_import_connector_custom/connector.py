# -*- coding: utf-8 -*-
from openerp.addons.connector.connector import install_in_connector, Environment

install_in_connector()


def get_environment(session, backend_id):
    """ Create an environment to work with. """
    backend_record = session.browse('taktik.importer.backend.custom', backend_id)
    env = Environment(backend_record, session, 'taktik.importer.model.custom')
    with env.session.change_context(lang='en_US'):
        return env
