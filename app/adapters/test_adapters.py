from app.adapters.threat_intel_adapter import ThreatIntelAdapter
from app.adapters.device_fingerprint_adapter import DeviceFingerprintAdapter
from app.adapters.geoip_adapter import GeoIPAdapter
from app.adapters.case_management_adapter import CaseManagementAdapter
from app.adapters.chatbot_adapter import ChatbotAdapter
from app.adapters.payment_gateway_adapter import PaymentGatewayAdapter
from app.adapters.blockchain_adapter import BlockchainAdapter
from app.adapters.data_masking_adapter import DataMaskingAdapter
from app.adapters.rule_engine_adapter import RuleEngineAdapter
from app.adapters.policy_versioning_adapter import PolicyVersioningAdapter
from app.adapters.risk_score_adapter import RiskScoreAdapter
from app.adapters.portfolio_analytics_adapter import PortfolioAnalyticsAdapter
from app.adapters.cloud_security_adapter import CloudSecurityAdapter
from app.adapters.vulnerability_scanner_adapter import VulnerabilityScannerAdapter
from app.adapters.data_lineage_adapter import DataLineageAdapter
from app.adapters.data_catalog_adapter import DataCatalogAdapter
from app.adapters.synthetic_data_adapter import SyntheticDataAdapter
from app.adapters.reg_change_adapter import RegChangeAdapter
import os
def count_adapter_classes():
    adapter_dir = os.path.dirname(__file__)
    count = 0
    for fname in os.listdir(adapter_dir):
        if fname.endswith('_adapter.py') and fname != 'base_adapter.py' and fname != 'test_adapters.py':
            with open(os.path.join(adapter_dir, fname), 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip().startswith('class ') and 'BaseAdapter' in line:
                        count += 1
                        break
    return count

def count_test_functions():
    count = 0
    with open(__file__, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip().startswith('def test_'):
                count += 1
    return count
def test_threat_intel_adapter():
    adapter = ThreatIntelAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("ThreatIntelAdapter:", transformed, "Valid:", valid)

def test_device_fingerprint_adapter():
    adapter = DeviceFingerprintAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("DeviceFingerprintAdapter:", transformed, "Valid:", valid)

def test_geoip_adapter():
    adapter = GeoIPAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("GeoIPAdapter:", transformed, "Valid:", valid)

def test_case_management_adapter():
    adapter = CaseManagementAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("CaseManagementAdapter:", transformed, "Valid:", valid)

def test_chatbot_adapter():
    adapter = ChatbotAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("ChatbotAdapter:", transformed, "Valid:", valid)

def test_payment_gateway_adapter():
    adapter = PaymentGatewayAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("PaymentGatewayAdapter:", transformed, "Valid:", valid)

def test_blockchain_adapter():
    adapter = BlockchainAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("BlockchainAdapter:", transformed, "Valid:", valid)

def test_data_masking_adapter():
    adapter = DataMaskingAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("DataMaskingAdapter:", transformed, "Valid:", valid)

def test_rule_engine_adapter():
    adapter = RuleEngineAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("RuleEngineAdapter:", transformed, "Valid:", valid)

def test_policy_versioning_adapter():
    adapter = PolicyVersioningAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("PolicyVersioningAdapter:", transformed, "Valid:", valid)

def test_risk_score_adapter():
    adapter = RiskScoreAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("RiskScoreAdapter:", transformed, "Valid:", valid)

def test_portfolio_analytics_adapter():
    adapter = PortfolioAnalyticsAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("PortfolioAnalyticsAdapter:", transformed, "Valid:", valid)

def test_cloud_security_adapter():
    adapter = CloudSecurityAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("CloudSecurityAdapter:", transformed, "Valid:", valid)

def test_vulnerability_scanner_adapter():
    adapter = VulnerabilityScannerAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("VulnerabilityScannerAdapter:", transformed, "Valid:", valid)

def test_data_lineage_adapter():
    adapter = DataLineageAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("DataLineageAdapter:", transformed, "Valid:", valid)

def test_data_catalog_adapter():
    adapter = DataCatalogAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("DataCatalogAdapter:", transformed, "Valid:", valid)

def test_synthetic_data_adapter():
    adapter = SyntheticDataAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("SyntheticDataAdapter:", transformed, "Valid:", valid)

def test_reg_change_adapter():
    adapter = RegChangeAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("RegChangeAdapter:", transformed, "Valid:", valid)
from app.adapters.pagerduty_adapter import PagerDutyAdapter
from app.adapters.iam_adapter import IAMAdapter
from app.adapters.reg_reporting_adapter import RegReportingAdapter
from app.adapters.audit_log_adapter import AuditLogAdapter
from app.adapters.kafka_adapter import KafkaAdapter
from app.adapters.sanctions_list_adapter import SanctionsListAdapter
from app.adapters.shap_adapter import SHAPAdapter
from app.adapters.consent_management_adapter import ConsentManagementAdapter
from app.adapters.api_gateway_adapter import APIGatewayAdapter
def test_pagerduty_adapter():
    adapter = PagerDutyAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("PagerDutyAdapter:", transformed, "Valid:", valid)

def test_iam_adapter():
    adapter = IAMAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("IAMAdapter:", transformed, "Valid:", valid)

def test_reg_reporting_adapter():
    adapter = RegReportingAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("RegReportingAdapter:", transformed, "Valid:", valid)

def test_audit_log_adapter():
    adapter = AuditLogAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("AuditLogAdapter:", transformed, "Valid:", valid)

def test_kafka_adapter():
    adapter = KafkaAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("KafkaAdapter:", transformed, "Valid:", valid)

def test_sanctions_list_adapter():
    adapter = SanctionsListAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("SanctionsListAdapter:", transformed, "Valid:", valid)

def test_shap_adapter():
    adapter = SHAPAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("SHAPAdapter:", transformed, "Valid:", valid)

def test_consent_management_adapter():
    adapter = ConsentManagementAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("ConsentManagementAdapter:", transformed, "Valid:", valid)

def test_api_gateway_adapter():
    adapter = APIGatewayAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("APIGatewayAdapter:", transformed, "Valid:", valid)
from app.adapters.arize_adapter import ArizeAdapter
from app.adapters.whylogs_adapter import WhylogsAdapter
from app.adapters.great_expectations_adapter import GreatExpectationsAdapter
from app.adapters.monte_carlo_adapter import MonteCarloAdapter
from app.adapters.centralized_observability_dashboard_adapter import CentralizedObservabilityDashboardAdapter
def test_arize_adapter():
    adapter = ArizeAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("ArizeAdapter:", transformed, "Valid:", valid)

def test_whylogs_adapter():
    adapter = WhylogsAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("WhylogsAdapter:", transformed, "Valid:", valid)

def test_great_expectations_adapter():
    adapter = GreatExpectationsAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("GreatExpectationsAdapter:", transformed, "Valid:", valid)

def test_monte_carlo_adapter():
    adapter = MonteCarloAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("MonteCarloAdapter:", transformed, "Valid:", valid)

def test_centralized_observability_dashboard_adapter():
    adapter = CentralizedObservabilityDashboardAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("CentralizedObservabilityDashboardAdapter:", transformed, "Valid:", valid)
from app.adapters.fastapi_serving_adapter import FastAPIServingAdapter
from app.adapters.torchserve_adapter import TorchServeAdapter
from app.adapters.tensorflow_serving_adapter import TensorFlowServingAdapter
from app.adapters.kubeflow_adapter import KubeflowAdapter
from app.adapters.model_gateway_adapter import ModelGatewayAdapter
def test_fastapi_serving_adapter():
    adapter = FastAPIServingAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("FastAPIServingAdapter:", transformed, "Valid:", valid)

def test_torchserve_adapter():
    adapter = TorchServeAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("TorchServeAdapter:", transformed, "Valid:", valid)

def test_tensorflow_serving_adapter():
    adapter = TensorFlowServingAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("TensorFlowServingAdapter:", transformed, "Valid:", valid)

def test_kubeflow_adapter():
    adapter = KubeflowAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("KubeflowAdapter:", transformed, "Valid:", valid)

def test_model_gateway_adapter():
    adapter = ModelGatewayAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("ModelGatewayAdapter:", transformed, "Valid:", valid)
from app.adapters.airflow_adapter import AirflowAdapter
from app.adapters.mcp_server_adapter import MCPServerAdapter
from app.adapters.github_mcp_adapter import GitHubMCPAdapter
from app.adapters.aws_databricks_mcp_adapter import AWSDatabricksMCPAdapter
def test_airflow_adapter():
    adapter = AirflowAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("AirflowAdapter:", transformed, "Valid:", valid)

def test_mcp_server_adapter():
    adapter = MCPServerAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("MCPServerAdapter:", transformed, "Valid:", valid)

def test_github_mcp_adapter():
    adapter = GitHubMCPAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("GitHubMCPAdapter:", transformed, "Valid:", valid)

def test_aws_databricks_mcp_adapter():
    adapter = AWSDatabricksMCPAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("AWSDatabricksMCPAdapter:", transformed, "Valid:", valid)

from app.adapters.postgres_adapter import PostgresAdapter
from app.adapters.dynamodb_adapter import DynamoDBAdapter
from app.adapters.snowflake_adapter import SnowflakeAdapter
from app.adapters.fivetran_adapter import FivetranAdapter
from app.adapters.aws_glue_adapter import AWSGlueAdapter
from app.adapters.dbt_adapter import DBTAdapter
from app.adapters.orchestrator_adapter import OrchestratorAdapter


def test_postgres_adapter():
    adapter = PostgresAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("PostgresAdapter:", transformed, "Valid:", valid)

def test_dynamodb_adapter():
    adapter = DynamoDBAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("DynamoDBAdapter:", transformed, "Valid:", valid)

def test_snowflake_adapter():
    adapter = SnowflakeAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("SnowflakeAdapter:", transformed, "Valid:", valid)

def test_fivetran_adapter():
    adapter = FivetranAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("FivetranAdapter:", transformed, "Valid:", valid)

def test_aws_glue_adapter():
    adapter = AWSGlueAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("AWSGlueAdapter:", transformed, "Valid:", valid)

def test_dbt_adapter():
    adapter = DBTAdapter()
    adapter.connect()
    data = adapter.fetch()
    transformed = adapter.transform(data)
    valid = adapter.validate(transformed)
    print("DBTAdapter:", transformed, "Valid:", valid)

def test_orchestrator_adapter():
    orchestrator = OrchestratorAdapter()
    results = orchestrator.run_pipeline()
    print("OrchestratorAdapter Results:", results)

if __name__ == "__main__":
    test_postgres_adapter()
    test_dynamodb_adapter()
    test_snowflake_adapter()
    test_fivetran_adapter()
    test_aws_glue_adapter()
    test_dbt_adapter()
    test_orchestrator_adapter()
    test_airflow_adapter()
    test_mcp_server_adapter()
    test_github_mcp_adapter()
    test_aws_databricks_mcp_adapter()
    test_fastapi_serving_adapter()
    test_torchserve_adapter()
    test_tensorflow_serving_adapter()
    test_kubeflow_adapter()
    test_model_gateway_adapter()
    test_arize_adapter()
    test_whylogs_adapter()
    test_great_expectations_adapter()
    test_monte_carlo_adapter()
    test_centralized_observability_dashboard_adapter()
    test_pagerduty_adapter()
    test_iam_adapter()
    test_reg_reporting_adapter()
    test_audit_log_adapter()
    test_kafka_adapter()
    test_sanctions_list_adapter()
    test_shap_adapter()
    test_consent_management_adapter()
    test_api_gateway_adapter()
    test_threat_intel_adapter()
    test_device_fingerprint_adapter()
    test_geoip_adapter()
    test_case_management_adapter()
    test_chatbot_adapter()
    test_payment_gateway_adapter()
    test_blockchain_adapter()
    test_data_masking_adapter()
    test_rule_engine_adapter()
    test_policy_versioning_adapter()
    test_risk_score_adapter()
    test_portfolio_analytics_adapter()
    test_cloud_security_adapter()
    test_vulnerability_scanner_adapter()
    test_data_lineage_adapter()
    test_data_catalog_adapter()
    test_synthetic_data_adapter()
    test_reg_change_adapter()
    total_adapters = count_adapter_classes()
    total_tests = count_test_functions()
    print(f"\nSummary: {total_adapters} adapter classes present, {total_tests} test functions found.")
