# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class reception_check(models.Model):
#     _name = 'reception_check.reception_check'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
