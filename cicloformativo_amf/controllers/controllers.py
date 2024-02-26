# -*- coding: utf-8 -*-
# from odoo import http


# class CicloformativoAmf(http.Controller):
#     @http.route('/cicloformativo_amf/cicloformativo_amf', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cicloformativo_amf/cicloformativo_amf/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cicloformativo_amf.listing', {
#             'root': '/cicloformativo_amf/cicloformativo_amf',
#             'objects': http.request.env['cicloformativo_amf.cicloformativo_amf'].search([]),
#         })

#     @http.route('/cicloformativo_amf/cicloformativo_amf/objects/<model("cicloformativo_amf.cicloformativo_amf"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cicloformativo_amf.object', {
#             'object': obj
#         })

