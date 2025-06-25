# -*- coding: utf-8 -*-
from odoo import models, fields

class ProductManualCategory(models.Model):
    _name = 'product.manual.category'
    _description = 'Product Manual Categories'

    name = fields.Char(string='Title', required=True)
    background_color = fields.Char(string='Background Color')
    border_color = fields.Char(string='Border Color')
    website_ids = fields.Many2many('website', string='Websites')
    category_id = fields.Char(string='Category ID')
    product_ids = fields.Many2many('product.template', string='Products')

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    manual_link = fields.Char(string='Product Manual Link')
    sequence = fields.Integer(string='Sequence', default=10)