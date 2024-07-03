from odoo import models, fields, api
from datetime import datetime


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    # pass

    def action_confirm(self):
        """This method creates one or more delivery orders based on the sale order lines.If multiple order lines contain the same product, they are grouped into a single delivery order."""

        if self:

            stock_picking_type_id = self.env['stock.picking.type'].search(
                [('code', '=', 'outgoing'), ('company_id', '=', self.env.company.id), ('name', '=', 'Delivery Orders')])
            product_location = self.env['stock.location'].search(
                [('name', '=', 'Stock'), ('company_id', '=', self.env.company.id)])

            stock_picking_dict = {}

            for lines in self.order_line:
                product_id = lines.product_id.id
                if product_id not in stock_picking_dict:

                    stock_picking = self.env['stock.picking'].create(
                        {
                            'name': 'WH/OUT' + str(str(self.id) + str(lines.id)),
                            'move_type': 'direct',
                            'company_id': self.company_id.id,
                            'location_id': product_location.id,
                            'location_dest_id': self.partner_id.property_stock_customer.id,
                            'partner_id': self.partner_id.id,
                            'date_done': datetime.now(),
                            'picking_type_id': stock_picking_type_id.id,
                            'origin': self.name
                        })
                    stock_picking_dict[product_id] = stock_picking
                else:
                    stock_picking = stock_picking_dict[product_id]

                stock_move = self.env['stock.move'].create({
                    'date': datetime.now(),
                    'company_id': self.company_id.id,
                    'product_id': lines.product_id.id,
                    'location_id': product_location.id,
                    'product_uom_qty': lines.product_uom_qty,
                    'partner_id': self.partner_id.id,
                    'location_dest_id': self.partner_id.property_stock_customer.id,
                    'name': lines.product_id.name,
                    'picking_id': stock_picking.id,
                    'origin': self.name,
                    'sale_line_id': lines.id,
                    'reference': stock_picking.name

                })

            # Confirm each stock picking
            for stock_picking in stock_picking_dict.values():
                stock_picking.action_confirm()
            self.write({'state': 'sale'})
        # val = super(SaleOrderInherit, self).action_confirm()
        return True

    def action_multiple_sale_order_delivery(self):
        """ for viewing the multiple delivery records of sale order"""

        stock_picking_records = self.env['stock.picking'].search([('origin', '=', self.name)])
        print("stock.........picking..........records.......",stock_picking_records)
        if stock_picking_records:
            picking_tree_view_id = self.env.ref('stock.vpicktree').id
            picking_form_view_id = self.env.ref('stock.view_picking_form').id

            return {
                'name': 'multiple delivery',
                'view_mode': 'tree,form',
                'views': [(picking_tree_view_id, 'tree'), (picking_form_view_id, 'form')],
                'res_model': 'stock.picking',
                'view_id': picking_tree_view_id,
                'type': 'ir.actions.act_window',
                'domain': [('id', 'in', stock_picking_records.ids)],
            }


