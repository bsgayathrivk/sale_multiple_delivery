# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderDelivery(http.Controller):
#     @http.route('/sale_order_delivery/sale_order_delivery', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_delivery/sale_order_delivery/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_delivery.listing', {
#             'root': '/sale_order_delivery/sale_order_delivery',
#             'objects': http.request.env['sale_order_delivery.sale_order_delivery'].search([]),
#         })

#     @http.route('/sale_order_delivery/sale_order_delivery/objects/<model("sale_order_delivery.sale_order_delivery"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_delivery.object', {
#             'object': obj
#         })
