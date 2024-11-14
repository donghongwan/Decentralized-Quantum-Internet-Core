from flask import request, jsonify
from services.compliance_service import ComplianceService

class ComplianceController:
    def __init__(self, app):
        self.compliance_service = ComplianceService()
        app.add_url_rule('/compliance/<device_id>', 'check_compliance', self.check_compliance, methods=['GET'])

    def check_compliance(self, device_id):
        compliance_status = self.compliance_service.check_compliance(device_id)
        return jsonify(compliance_status), 200
