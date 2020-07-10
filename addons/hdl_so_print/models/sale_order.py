import logging 
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo import api, fields ,models
from odoo.exceptions import ValidationError 
from odoo.http import request

class order(models.Model):
    _inherit='sale.order'
    survey_sheet=fields.Many2one("survey.sheet",String="Survey Sheet")
    installation=fields.Float("Installation")
    offer_num=fields.Float("Offer Number",default=1)
    offer_duration=fields.Selection([("week","Week"),("month","Month"),("year","Year")],String="Duration",default="week")