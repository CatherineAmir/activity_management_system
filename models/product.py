from odoo import fields, models, api


class Product(models.Model):
    _inherit = 'product.template'

    configuration_slot_ids=fields.One2many('activity.slot.configuration', 'product_id')

    # def _set_default_country(self):
    #     return 65
    # country_id = fields.Many2one('res.country',default=_set_default_country,string="Country")
    # state = fields.Many2one('res.country.state',string="Government")
    city=fields.Char(string="City")
    location=fields.Char(string="Location")


