{
    'name': 'Eyewear Shop',
    'version': '1.0',
    'category': 'Retail',
    'description': """
This module is for stylish and affordable eyewear. It will deal with various types of eyewear like Sunglasses, Contact Lenses, Specialty eyewear, etc.
The sales process involves creating sale orders, managing deliveries and invoicing. Additionally, they operate an eCommerce shop for online sales in the eyewear industry.
""",
    'depends': [
        'appointment_crm',
        'knowledge',
        'payment_demo',
        'purchase_stock',
        'sale_management',
        'website_appointment',
        'website_sale_comparison',
        'website_sale_loyalty',
        'website_sale_wishlist',
        'theme_paptic',
    ],
    'data': [
        'data/ir_attachment_pre.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_view.xml',
        'data/ir_actions_report.xml',
        'data/product_category.xml',
        'data/product_public_category.xml',
        'data/product_template.xml',
        'data/product_attribute.xml',
        'data/product_attribute_value.xml',
        'data/product_template_attribute_line.xml',
        'data/product_template_attribute_value.xml',
        'data/product_product.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/appointment_type.xml',
        'data/ir_model_data.xml',
    ],
    'demo': [
        'demo/res_config_settings.xml',
        'demo/website.xml',
        'demo/stock_lot.xml',
        'demo/res_partner.xml',
        'demo/loyalty_program.xml',
        'demo/loyalty_rule.xml',
        'demo/loyalty_reward.xml',
        'demo/crm_team.xml',
        'demo/crm_lead.xml',
        'demo/product_supplierinfo.xml',
        'demo/calendar_event.xml',
        'demo/purchase_order.xml',
        'demo/purchase_order_line.xml',
        'demo/purchase_order_confirm.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_confirm.xml',
        'demo/stock_warehouse_orderpoint.xml',
        'demo/website_ir_attachment.xml',
        'demo/website_view.xml',
        'demo/website_theme_apply.xml',
    ],
    'license': 'OPL-1',
    'images': ['images/main.png'],
    'maintenance_loc': 0,
}
