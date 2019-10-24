# -*- coding: utf-8 -*-
from odoo import http

# class ReceptionCheck(http.Controller):
#     @http.route('/reception_check/reception_check/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reception_check/reception_check/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('reception_check.listing', {
#             'root': '/reception_check/reception_check',
#             'objects': http.request.env['reception_check.reception_check'].search([]),
#         })

#     @http.route('/reception_check/reception_check/objects/<model("reception_check.reception_check"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reception_check.object', {
#             'object': obj
#         })