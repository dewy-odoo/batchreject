from odoo import api, models, fields

class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    def action_batch_reject(self):
        return {
            'type': 'ir.actions.act_window',
            'name': ('Refuse Reason'),
            'res_model': 'applicant.get.refuse.reason',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_applicant_ids': self.ids, 'active_test': False},
            'views': [[False, 'form']]
        }