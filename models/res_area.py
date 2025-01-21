from odoo import models,fields

class ResArea(models.Model):
    _name='res.area'
    _description = 'Areas'

    name = fields.Char(string='Area Name', required=True, store=True, readonly=False)
    color = fields.Integer(string='Color Index')