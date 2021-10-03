# -*- coding: utf-8 -*-
# from odoo import http


# class KokoNetworks(http.Controller):
#     @http.route('/koko_networks/koko_networks/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/koko_networks/koko_networks/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('koko_networks.listing', {
#             'root': '/koko_networks/koko_networks',
#             'objects': http.request.env['koko_networks.koko_networks'].search([]),
#         })

#     @http.route('/koko_networks/koko_networks/objects/<model("koko_networks.koko_networks"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('koko_networks.object', {
#             'object': obj
#         })
