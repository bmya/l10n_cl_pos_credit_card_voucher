# -*- coding: utf-8 -*-
from openerp import models, fields

class invoice_seller_field(models.Model):
    _inherit = "account.invoice"

    cc_voucher = fields.Char('Credit Card Voucher')


class account_journal(models.Model):
    _inherit = "account.journal"

    add_credit_card_voucher_number = fields.Boolean("Add credit card voucher number", default=False)
