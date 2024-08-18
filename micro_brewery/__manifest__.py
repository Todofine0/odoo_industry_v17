{
    'name': 'Micro Brewery',
    'version': '1.0',
    'category': 'Manufacturing',
    'description': """
This module is a setup specific to support the business activities of a microbrewery such as Crafting Beer, Outside Sales, a local Bar, a local Shop and an ecommerce website.
""",
    'depends': [
        'account',
        'appointment_crm',
        'knowledge',
        'mrp_plm',
        'mrp_subcontracting',
        'pos_restaurant',
        'pos_sale',
        'sale_purchase',
        'web_studio',
        'website_appointment',
        'website_sale_stock',
        'theme_bistro',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/product_category.xml',
        'data/ir_attachment_pre.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_view.xml',
        'data/product_public_category.xml',
        'data/uom_uom.xml',
        'data/restaurant_floor.xml',
        'data/restaurant_table.xml',
        'data/product_pricelist.xml',
        'data/product_pricelist_item.xml',
        'data/pos_category.xml',
        'data/pos_config.xml',
        'data/website_base_unit.xml',
        'data/product_template.xml',
        'data/product_attribute.xml',
        'data/product_attribute_value.xml',
        'data/product_template_attribute_line.xml',
        'data/product_template_attribute_value.xml',
        'data/product_product.xml',
        'data/mrp_bom_byproduct.xml',
        'data/mrp_bom.xml',
        'data/mrp_bom_line.xml',
        'data/mrp_workcenter.xml',
        'data/mrp_routing_workcenter.xml',
        'data/sale_order_template.xml',
        'data/sale_order_template_line.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/mail_message.xml',
        'data/knowledge_article_favorite.xml',
        'data/quality_point.xml',
        'data/appointment_type.xml',
        'data/website_view.xml',
        'data/ir_model_data.xml',
    ],
    'demo': [
        'demo/website.xml',
        'demo/res_partner.xml',
        'demo/mrp_bom.xml',
        'demo/crm_lead.xml',
        'demo/pos_config.xml',
        'demo/appointment_type.xml',
        'demo/product_supplierinfo.xml',
        'demo/product_template.xml',
        'demo/stock_lot.xml',
        'demo/stock_quant.xml',
        'demo/stock_warehouse_orderpoint.xml',
        'demo/mrp_orderpoint_post.xml',
        'demo/mrp_production.xml',
        'demo/purchase_order.xml',
        'demo/purchase_order_line.xml',
        'demo/purchase_order_post.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_confirm.xml',
        'demo/website_attachment.xml',
        'demo/website_view.xml',
        'demo/website_page.xml',
        'demo/website_menu.xml',
        'demo/website_theme_apply.xml',
        'demo/payment_provider_demo_post.xml',
    ],
    'license': 'OPL-1',
    'images': ['images/main.png'],
}
