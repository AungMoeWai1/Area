from odoo import models, fields, api

class Users(models.Model):
    _inherit = 'res.users'

    area_id = fields.Many2one('res.area', string="Area", compute="_compute_area", store=True)
    area_ids = fields.Many2many('res.area', string='Areas')

    @api.depends('area_ids')
    def _compute_area(self):
        for record in self:
            if record.area_ids:
                record.area_id = record.area_ids[0]
