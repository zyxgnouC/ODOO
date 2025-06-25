{
    'name': 'VCS Product Manual Category',
    'version': '18.0.1.0.1',
    'summary': "Create a dynamic block that displays a list of products according to categories set by the admin.",
    'author': 'cuong',
    'website': 'https://www.valleycampusgagon.com/',
    'category': 'Website',
    'depends': ['website_sale', 'product', 'web_editor'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_manual_category_views.xml',
        'views/product_template_views.xml',
        'views/snippets/custom_vcs_product_manual_category_snippet.xml',
        'views/snippets/custom_vcs_product_manual_category_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'custom_vcs_Product_manual/static/src/css/product_manual.css',
            'custom_vcs_Product_manual/static/src/js/product_manual.js',
        ],
        'website.assets_wysiwyg': [
            'custom_vcs_Product_manual/static/src/js/option.js',
        ],
        'web.assets_qweb': [
            'custom_vcs_Product_manual/static/src/**/*.xml',
        ],
        'web.assets_backend': [
            'custom_vcs_Product_manual/static/src/xml/vcs_custom_product_manual_template.xml',
        ],
    },
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}