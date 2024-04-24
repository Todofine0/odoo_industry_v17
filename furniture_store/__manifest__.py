{
    'name': 'Furniture Store',
    'version': '1.0',
    'category': 'Retail',
    'description': """
This module sets up a furniture store for selling furniture like chairs, sofas, dining tables, ...
""",
    'depends': [
        'knowledge',
        'mrp',
        'pos_sale',
        'payment_demo',
        'sale_margin',
        'sale_purchase',
        'website_crm',
        'website_sale_stock',
        'theme_anelusia',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/knowledge_attachments.xml',
        'data/product_public_category.xml',
        'data/product_category.xml',
        'data/stock_route.xml',
        'data/pos_category.xml',
        'data/product_template.xml',
        'data/product_attribute.xml',
        'data/product_attribute_value.xml',
        'data/product_pricelist.xml',
        'data/product_pricelist_item.xml',
        'data/product_template_attribute_line.xml',
        'data/product_template_attribute_value.xml',
        'data/product_product.xml',
        'data/mrp_bom.xml',
        'data/mrp_bom_line.xml',
        'data/pos_payment_method.xml',
        'data/pos_config.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/mail_message.xml',
        'data/payment_provider_demo.xml',
    ],
    'demo': [
        'demo/pos_config.xml',
        'demo/res_partner.xml',
        'demo/crm_lead.xml',
        'demo/product_supplierinfo.xml',
        'demo/stock_quant.xml',
        'demo/purchase_order.xml',
        'demo/purchase_order_line.xml',
        'demo/purchase_order_confirm.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_confirm.xml',
        'demo/stock_picking_validation.xml',
        'demo/website_attachments.xml',
        'demo/website_view.xml',
        'demo/website.xml',
        'demo/website_page.xml',
        'demo/website_menu.xml',
        'demo/website_theme_apply.xml',
        'demo/payment_provider_demo.xml',
    ],
    'license': 'OPL-1',
    'images': ['images/main.png'],
}
