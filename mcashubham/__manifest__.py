# -*- coding: utf-8 -*-
{
    'name': "SHUBHAM TEST",

    'summary': """
        Universal Tax v12.0
        """,

    'description': """
        - Apply a field in Sales, Purchase and Invoice module to calculate tax after the order lines are inserted.
        - Can be enabled from (**Note** : Charts of Accounts must be installed)
            
            Settings -> General Settings -> invoice
        
        - Maintains the global tax entries in accounts specified by you (**Note** : To see journal entries in Invoicing:
         (in debug mode))
            
            Settings -> users -> select user -> Check "Show Full Accounting Features")
        
        - Label given to you will be used as name given to tax field.
        - Also update the report PDF printout with global tax value.
    """,

    'author': "shubham",
    'website': "https://www.shub.com/",


    'category': 'Sales Management',
    'version': '1.1.1',
    'license': 'LGPL-3',
    'depends': ['base'],

    'data': [
        'views/shubtest.xml',
    ],

    'images': ['static/description/main.jpg'],

}
