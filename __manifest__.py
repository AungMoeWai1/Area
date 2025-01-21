{
    "name": "Area",
    "author": "Aungmoewai",
    "installed_version": "1.0",
    "category": "Hidden",
    "license": 'LGPL-3',
    "summary": """
    Adding field of area field for each invoice to show the given configuration of user to show the respective area of user after selecting in the accounting of selection field
    """,
    "depends": ["base", "account"],
    "data": [
        # For Security
        "security/base_groups.xml",
        "security/ir.model.access.csv",
        "security/base_security.xml",

        "views/res_area_views.xml",
        "views/res_user_views.xml",
        "views/account_move_views.xml",
        "views/account_menuitem.xml",
    ],
    "installable": True,
    "application": False,
}
