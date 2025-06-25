from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    estate_notes = fields.Text(string="Estate Remarks")
    die_number_id = fields.Char(string="Die Number")
    diameter = fields.Char("Diameter", index=True)
