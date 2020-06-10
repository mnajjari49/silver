# See LICENSE file for full copyright and licensing details.

{
    'name': 'Whatsapp Account',
    'version': '13.0.0.1.0',
    'license': 'OPL-1',
    'author': "Alphasoft",
    'sequence': 1,
    'website': 'https://www.alphasoft.co.id/',
    'images':  ['images/main_screenshot.png'],
    'summary': 'This module is used for Whatsapp Account',
    'category': 'Extra Tools',
    'depends': ['base_automation', 'account', 'aos_whatsapp'],
    'data': [
        'data/invoice_data.xml',
        'views/account_invoice.xml',
        'views/account_payment.xml',
        'wizard/whatsapp_compose_view.xml',
    ],
    'external_dependencies': {'python': ['html2text']},
    'demo': [],
    'test': [],
    'css': [],
    'js': [],
    'price': 0,
    'currency': 'EUR',
    'installable': True,
    'application': False,
    'auto_install': False,
}