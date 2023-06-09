{
    'name': 'PostgreSQL Query Deluxe',
    'description': 'Execute postgreSQL query into Odoo interface',
    'author': '',
    'depends': ['base', 'mail'],
    'application': True,
    'version': '13.0.1.0.3',
    'license': 'AGPL-3',
    'support': '',
    'website': '',
    'installable': True,

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/query_deluxe_views.xml',

        'wizard/pdforientation.xml',

        'report/print_pdf.xml',

        'datas/data.xml'
    ],

    'images': ['static/description/banner.gif']
}
