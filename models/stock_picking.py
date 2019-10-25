from odoo import models, fields, api


class StockPicking(models.Model):

    _inherit = 'stock.picking'

    check_list_responses = fields.One2many(
        'check.list.response',
        'picking_id',
        'check list'
    )

    @api.model
    def create(self, val_list):

        check_list_items = self.env['check.list.item']

        picking = super(self).create(val_list)
        responses = []
        for item in check_list_items:
            responses.append({
                'item': item,
                'picking_id': picking
            })

        self.env['check.list.response'].create(responses)

        return picking
