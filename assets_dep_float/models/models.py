# -*- coding: utf-8 -*-
# See __manifest.py file for full copyright and licensing details.
from odoo import api, fields, models, _

class AccountAssetCategory(models.Model):
    _inherit = 'account.asset.category'

    method_progress_factor = fields.Float(string=' New Declining Factor', default=0.3, digits=(16, 8),)

class AccountAsset(models.Model):
    _inherit = 'account.asset.asset'

    method_progress_factor = fields.Float(string=' New Declining Factor', default=0.3, digits=(16, 8),)
