from .threat_intel_adapter import ThreatIntelAdapter
from .device_fingerprint_adapter import DeviceFingerprintAdapter
from .geoip_adapter import GeoIPAdapter
from .case_management_adapter import CaseManagementAdapter
from .chatbot_adapter import ChatbotAdapter
from .payment_gateway_adapter import PaymentGatewayAdapter
from .blockchain_adapter import BlockchainAdapter
from .data_masking_adapter import DataMaskingAdapter
from .rule_engine_adapter import RuleEngineAdapter
from .policy_versioning_adapter import PolicyVersioningAdapter
from .risk_score_adapter import RiskScoreAdapter
from .portfolio_analytics_adapter import PortfolioAnalyticsAdapter
from .cloud_security_adapter import CloudSecurityAdapter
from .vulnerability_scanner_adapter import VulnerabilityScannerAdapter
from .data_lineage_adapter import DataLineageAdapter
from .data_catalog_adapter import DataCatalogAdapter
from .synthetic_data_adapter import SyntheticDataAdapter
from .reg_change_adapter import RegChangeAdapter
from .arize_adapter import ArizeAdapter
from .whylogs_adapter import WhylogsAdapter
from .great_expectations_adapter import GreatExpectationsAdapter
from .monte_carlo_adapter import MonteCarloAdapter
from .centralized_observability_dashboard_adapter import CentralizedObservabilityDashboardAdapter
from .pagerduty_adapter import PagerDutyAdapter
from .iam_adapter import IAMAdapter
from .reg_reporting_adapter import RegReportingAdapter
from .audit_log_adapter import AuditLogAdapter
from .kafka_adapter import KafkaAdapter
from .sanctions_list_adapter import SanctionsListAdapter
from .shap_adapter import SHAPAdapter
from .consent_management_adapter import ConsentManagementAdapter
from .api_gateway_adapter import APIGatewayAdapter

from .fivetran_adapter import FivetranAdapter
from .aws_glue_adapter import AWSGlueAdapter
from .dbt_adapter import DBTAdapter
from .postgres_adapter import PostgresAdapter
from .dynamodb_adapter import DynamoDBAdapter
from .snowflake_adapter import SnowflakeAdapter

from .airflow_adapter import AirflowAdapter
from .mcp_server_adapter import MCPServerAdapter
from .github_mcp_adapter import GitHubMCPAdapter
from .aws_databricks_mcp_adapter import AWSDatabricksMCPAdapter
from .fastapi_serving_adapter import FastAPIServingAdapter
from .torchserve_adapter import TorchServeAdapter
from .tensorflow_serving_adapter import TensorFlowServingAdapter
from .kubeflow_adapter import KubeflowAdapter
from .model_gateway_adapter import ModelGatewayAdapter

class OrchestratorAdapter:
    """
    Orchestrates the ETL pipeline: ingestion, transformation, and validation using all adapters.
    """
    def __init__(self):
        self.fivetran = FivetranAdapter()
        self.glue = AWSGlueAdapter()
        self.dbt = DBTAdapter()
        self.postgres = PostgresAdapter()
        self.dynamodb = DynamoDBAdapter()
        self.snowflake = SnowflakeAdapter()
        self.threat_intel = ThreatIntelAdapter()
        self.device_fingerprint = DeviceFingerprintAdapter()
        self.geoip = GeoIPAdapter()
        self.case_management = CaseManagementAdapter()
        self.chatbot = ChatbotAdapter()
        self.payment_gateway = PaymentGatewayAdapter()
        self.blockchain = BlockchainAdapter()
        self.data_masking = DataMaskingAdapter()
        self.rule_engine = RuleEngineAdapter()
        self.policy_versioning = PolicyVersioningAdapter()
        self.risk_score = RiskScoreAdapter()
        self.portfolio_analytics = PortfolioAnalyticsAdapter()
        self.cloud_security = CloudSecurityAdapter()
        self.vulnerability_scanner = VulnerabilityScannerAdapter()
        self.data_lineage = DataLineageAdapter()
        self.data_catalog = DataCatalogAdapter()
        self.synthetic_data = SyntheticDataAdapter()
        self.reg_change = RegChangeAdapter()
        self.airflow = AirflowAdapter()
        self.mcp_server = MCPServerAdapter()
        self.github_mcp = GitHubMCPAdapter()
        self.aws_databricks_mcp = AWSDatabricksMCPAdapter()
        self.fastapi_serving = FastAPIServingAdapter()
        self.torchserve = TorchServeAdapter()
        self.tensorflow_serving = TensorFlowServingAdapter()
        self.kubeflow = KubeflowAdapter()
        self.model_gateway = ModelGatewayAdapter()
        self.pagerduty = PagerDutyAdapter()
        self.iam = IAMAdapter()
        self.reg_reporting = RegReportingAdapter()
        self.audit_log = AuditLogAdapter()
        self.kafka = KafkaAdapter()
        self.sanctions_list = SanctionsListAdapter()
        self.shap = SHAPAdapter()
        self.consent_management = ConsentManagementAdapter()
        self.api_gateway = APIGatewayAdapter()
        self.arize = ArizeAdapter()
        self.whylogs = WhylogsAdapter()
        self.great_expectations = GreatExpectationsAdapter()
        self.monte_carlo = MonteCarloAdapter()
        self.centralized_observability_dashboard = CentralizedObservabilityDashboardAdapter()

    def run_pipeline(self):
        # Ingestion & Transformation
        fivetran_data = self.fivetran.transform(self.fivetran.fetch())
        glue_data = self.glue.transform(self.glue.fetch())
        dbt_data = self.dbt.transform(self.dbt.fetch())
        pg_data = self.postgres.transform(self.postgres.fetch())
        dy_data = self.dynamodb.transform(self.dynamodb.fetch())
        sf_data = self.snowflake.transform(self.snowflake.fetch())
        threat_intel_data = self.threat_intel.transform(self.threat_intel.fetch())
        device_fingerprint_data = self.device_fingerprint.transform(self.device_fingerprint.fetch())
        geoip_data = self.geoip.transform(self.geoip.fetch())
        case_management_data = self.case_management.transform(self.case_management.fetch())
        chatbot_data = self.chatbot.transform(self.chatbot.fetch())
        payment_gateway_data = self.payment_gateway.transform(self.payment_gateway.fetch())
        blockchain_data = self.blockchain.transform(self.blockchain.fetch())
        data_masking_data = self.data_masking.transform(self.data_masking.fetch())
        rule_engine_data = self.rule_engine.transform(self.rule_engine.fetch())
        policy_versioning_data = self.policy_versioning.transform(self.policy_versioning.fetch())
        risk_score_data = self.risk_score.transform(self.risk_score.fetch())
        portfolio_analytics_data = self.portfolio_analytics.transform(self.portfolio_analytics.fetch())
        cloud_security_data = self.cloud_security.transform(self.cloud_security.fetch())
        vulnerability_scanner_data = self.vulnerability_scanner.transform(self.vulnerability_scanner.fetch())
        data_lineage_data = self.data_lineage.transform(self.data_lineage.fetch())
        data_catalog_data = self.data_catalog.transform(self.data_catalog.fetch())
        synthetic_data_data = self.synthetic_data.transform(self.synthetic_data.fetch())
        reg_change_data = self.reg_change.transform(self.reg_change.fetch())
        airflow_data = self.airflow.transform(self.airflow.fetch())
        mcp_server_data = self.mcp_server.transform(self.mcp_server.fetch())
        github_mcp_data = self.github_mcp.transform(self.github_mcp.fetch())
        aws_databricks_mcp_data = self.aws_databricks_mcp.transform(self.aws_databricks_mcp.fetch())
        fastapi_serving_data = self.fastapi_serving.transform(self.fastapi_serving.fetch())
        torchserve_data = self.torchserve.transform(self.torchserve.fetch())
        tensorflow_serving_data = self.tensorflow_serving.transform(self.tensorflow_serving.fetch())
        kubeflow_data = self.kubeflow.transform(self.kubeflow.fetch())
        model_gateway_data = self.model_gateway.transform(self.model_gateway.fetch())
        arize_data = self.arize.transform(self.arize.fetch())
        whylogs_data = self.whylogs.transform(self.whylogs.fetch())
        great_expectations_data = self.great_expectations.transform(self.great_expectations.fetch())
        monte_carlo_data = self.monte_carlo.transform(self.monte_carlo.fetch())
        centralized_observability_dashboard_data = self.centralized_observability_dashboard.transform(self.centralized_observability_dashboard.fetch())
        pagerduty_data = self.pagerduty.transform(self.pagerduty.fetch())
        iam_data = self.iam.transform(self.iam.fetch())
        reg_reporting_data = self.reg_reporting.transform(self.reg_reporting.fetch())
        audit_log_data = self.audit_log.transform(self.audit_log.fetch())
        kafka_data = self.kafka.transform(self.kafka.fetch())
        sanctions_list_data = self.sanctions_list.transform(self.sanctions_list.fetch())
        shap_data = self.shap.transform(self.shap.fetch())
        consent_management_data = self.consent_management.transform(self.consent_management.fetch())
        api_gateway_data = self.api_gateway.transform(self.api_gateway.fetch())
        # Validation
        results = {
            "fivetran": {"data": fivetran_data, "valid": self.fivetran.validate(fivetran_data)},
            "glue": {"data": glue_data, "valid": self.glue.validate(glue_data)},
            "dbt": {"data": dbt_data, "valid": self.dbt.validate(dbt_data)},
            "postgres": {"data": pg_data, "valid": self.postgres.validate(pg_data)},
            "dynamodb": {"data": dy_data, "valid": self.dynamodb.validate(dy_data)},
            "snowflake": {"data": sf_data, "valid": self.snowflake.validate(sf_data)},
            "threat_intel": {"data": threat_intel_data, "valid": self.threat_intel.validate(threat_intel_data)},
            "device_fingerprint": {"data": device_fingerprint_data, "valid": self.device_fingerprint.validate(device_fingerprint_data)},
            "geoip": {"data": geoip_data, "valid": self.geoip.validate(geoip_data)},
            "case_management": {"data": case_management_data, "valid": self.case_management.validate(case_management_data)},
            "chatbot": {"data": chatbot_data, "valid": self.chatbot.validate(chatbot_data)},
            "payment_gateway": {"data": payment_gateway_data, "valid": self.payment_gateway.validate(payment_gateway_data)},
            "blockchain": {"data": blockchain_data, "valid": self.blockchain.validate(blockchain_data)},
            "data_masking": {"data": data_masking_data, "valid": self.data_masking.validate(data_masking_data)},
            "rule_engine": {"data": rule_engine_data, "valid": self.rule_engine.validate(rule_engine_data)},
            "policy_versioning": {"data": policy_versioning_data, "valid": self.policy_versioning.validate(policy_versioning_data)},
            "risk_score": {"data": risk_score_data, "valid": self.risk_score.validate(risk_score_data)},
            "portfolio_analytics": {"data": portfolio_analytics_data, "valid": self.portfolio_analytics.validate(portfolio_analytics_data)},
            "cloud_security": {"data": cloud_security_data, "valid": self.cloud_security.validate(cloud_security_data)},
            "vulnerability_scanner": {"data": vulnerability_scanner_data, "valid": self.vulnerability_scanner.validate(vulnerability_scanner_data)},
            "data_lineage": {"data": data_lineage_data, "valid": self.data_lineage.validate(data_lineage_data)},
            "data_catalog": {"data": data_catalog_data, "valid": self.data_catalog.validate(data_catalog_data)},
            "synthetic_data": {"data": synthetic_data_data, "valid": self.synthetic_data.validate(synthetic_data_data)},
            "reg_change": {"data": reg_change_data, "valid": self.reg_change.validate(reg_change_data)},
            "airflow": {"data": airflow_data, "valid": self.airflow.validate(airflow_data)},
            "mcp_server": {"data": mcp_server_data, "valid": self.mcp_server.validate(mcp_server_data)},
            "github_mcp": {"data": github_mcp_data, "valid": self.github_mcp.validate(github_mcp_data)},
            "aws_databricks_mcp": {"data": aws_databricks_mcp_data, "valid": self.aws_databricks_mcp.validate(aws_databricks_mcp_data)},
            "fastapi_serving": {"data": fastapi_serving_data, "valid": self.fastapi_serving.validate(fastapi_serving_data)},
            "torchserve": {"data": torchserve_data, "valid": self.torchserve.validate(torchserve_data)},
            "tensorflow_serving": {"data": tensorflow_serving_data, "valid": self.tensorflow_serving.validate(tensorflow_serving_data)},
            "kubeflow": {"data": kubeflow_data, "valid": self.kubeflow.validate(kubeflow_data)},
            "model_gateway": {"data": model_gateway_data, "valid": self.model_gateway.validate(model_gateway_data)},
            "arize": {"data": arize_data, "valid": self.arize.validate(arize_data)},
            "whylogs": {"data": whylogs_data, "valid": self.whylogs.validate(whylogs_data)},
            "great_expectations": {"data": great_expectations_data, "valid": self.great_expectations.validate(great_expectations_data)},
            "monte_carlo": {"data": monte_carlo_data, "valid": self.monte_carlo.validate(monte_carlo_data)},
            "centralized_observability_dashboard": {"data": centralized_observability_dashboard_data, "valid": self.centralized_observability_dashboard.validate(centralized_observability_dashboard_data)},
            "pagerduty": {"data": pagerduty_data, "valid": self.pagerduty.validate(pagerduty_data)},
            "iam": {"data": iam_data, "valid": self.iam.validate(iam_data)},
            "reg_reporting": {"data": reg_reporting_data, "valid": self.reg_reporting.validate(reg_reporting_data)},
            "audit_log": {"data": audit_log_data, "valid": self.audit_log.validate(audit_log_data)},
            "kafka": {"data": kafka_data, "valid": self.kafka.validate(kafka_data)},
            "sanctions_list": {"data": sanctions_list_data, "valid": self.sanctions_list.validate(sanctions_list_data)},
            "shap": {"data": shap_data, "valid": self.shap.validate(shap_data)},
            "consent_management": {"data": consent_management_data, "valid": self.consent_management.validate(consent_management_data)},
            "api_gateway": {"data": api_gateway_data, "valid": self.api_gateway.validate(api_gateway_data)}
        }
        return results
