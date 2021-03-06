import logging 
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo import api, fields ,models
from odoo.exceptions import ValidationError 
from odoo.http import request
from collections import OrderedDict
from datetime import datetime

class sales_order(models.Model):
    _inherit="sale.order"
    tax_id=fields.Many2one("account.tax",string="Taxes")
    survey_sheet=fields.Many2one("survey.sheet",String="Survey Sheet")
    installation=fields.Float("Installation %")
    offer_num=fields.Float("Offer Number",default=1)
    offer_duration=fields.Selection([("week","Week"),("month","Month"),("year","Year")],String="Duration",default="week")
    install_value=fields.Float(compute='get_installion',string="Installation %")
    @api.onchange("tax_id","order_line")
    def get_taxes(self):
        if self.tax_id:
            for rec in self.order_line:
                rec.tax_id=self.tax_id
        
    @api.depends("order_line","installation")
    def get_installion(self):
        if self.installation  and self.order_line:
            total_price=0
            for rec in self.order_line:
                if rec.product_id.installation ==False:
                    total_price+=rec.price_unit*rec.product_uom_qty
            
            self.install_value=total_price*(self.installation/100)
            
        else:
            self.install_value=0
    @api.constrains("installation")
    def get_install_product(self):
        _logger.info("PPPPPPPPPPPPP")
        _logger.info(self.install_value)
        if self.installation:
            products=self.env['product.product'].search([('installation','=',True)])
            product_id=0
            for prod in products:
                product_id=prod.id
                break
            order_lines=self.env['sale.order.line'].search([("product_id","=",product_id),("order_id","=",self.id)])
            if product_id!=0:
                if order_lines:
                        order_lines.write({"price_unit":self.install_value})
                else:
                        self.order_line.create({"product_id":product_id,"name":prod.name,"price_unit":self.install_value,"order_id":self.id})
    


