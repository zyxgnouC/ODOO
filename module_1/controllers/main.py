# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class ProductManualController(http.Controller):
    @http.route('/product_manual/get_data', type='json', auth="public", website=True)
    def get_product_manual_data(self, params):
        """
        Fetch product manual data for a specific category by ID.
        """
        category_id = int(params.get('category_id'))
        category = request.env['product.manual.category'].browse(category_id)
        products = category.product_ids.sorted(key=lambda p: p.sequence)

        return {
            'name': category.name,
            'background_color': category.background_color,
            'border_color': category.border_color,
            'products': [{
                'id': product.id,
                'name': product.name,
                'image_url': f'/web/image/product.template/{product.id}/image_128',
                'product_url': getattr(product, 'redirect_url', f'/shop/product/{product.id}'),
                'manual_link': product.manual_link,
            } for product in products],
        }

    @http.route('/product_manual/categories', type='json', auth="public", website=True)
    def get_categories(self, **kwargs):
        """
        Fetch all product manual categories for the current website.
        """
        website_id = request.website.id
        categories = request.env['product.manual.category'].search([
            '|',
            ('website_ids', 'in', website_id),
            ('website_ids', '=', False)
        ])
        return [{'id': category.id, 'name': category.name} for category in categories]