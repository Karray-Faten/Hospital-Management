# -*- coding: utf-8 -*-


{
    'name': 'Hospital',
    'author': 'Faten KARRAY',
    'version': '1.0',
    'category': 'Hospital',
    # lower the sequence value the module will be listed first
    'sequence': 4,
    'summary': 'Hospital management system',
    'description': """
Hospital management system
==========================

The Hospital management module is used to manage hospitals, doctors, patients, and their appointments.

Key Features
------------
* Manage your Patients and their Appointments.
""",
    'website': 'https://github.com/Karray-Faten/Hospital-Management.git',
    'depends': [
        'mail',
    ],
    'data': [
        # 'security/ir.model.access.csv',

        #'data/ir_cron_data.xml',

        #'wizard/views.xml',

        # 'views/menu_views.xml',
    ],
    'demo': [
    ],
    'images': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {
        'web.assets_backend': [
        ],
        'web.assets_tests': [
        ],
        'web.qunit_suite_tests': [

        ],
    },
    'license': 'LGPL-3',
}
