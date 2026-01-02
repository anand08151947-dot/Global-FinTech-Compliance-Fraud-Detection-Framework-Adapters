from mock_api import mock_transaction_api, mock_user_profile_api, mock_fraud_check_api
from agent_visualization import generate_sequence_diagram, generate_mermaid_sequence
from app.adapters.iam_adapter import IAMAdapter
from app.adapters.consent_management_adapter import ConsentManagementAdapter
from app.adapters.data_masking_adapter import DataMaskingAdapter
from app.adapters.cloud_security_adapter import CloudSecurityAdapter
from app.adapters.vulnerability_scanner_adapter import VulnerabilityScannerAdapter
from app.adapters.reg_reporting_adapter import RegReportingAdapter
from app.adapters.case_management_adapter import CaseManagementAdapter
from app.adapters.portfolio_analytics_adapter import PortfolioAnalyticsAdapter
from app.adapters.chatbot_adapter import ChatbotAdapter
from app.adapters.payment_gateway_adapter import PaymentGatewayAdapter
from app.adapters.blockchain_adapter import BlockchainAdapter
from app.adapters.data_lineage_adapter import DataLineageAdapter
from app.adapters.data_catalog_adapter import DataCatalogAdapter
from app.adapters.synthetic_data_adapter import SyntheticDataAdapter
from app.adapters.api_gateway_adapter import APIGatewayAdapter
from app.adapters.mcp_server_adapter import MCPServerAdapter
from app.adapters.github_mcp_adapter import GitHubMCPAdapter
from app.adapters.aws_databricks_mcp_adapter import AWSDatabricksMCPAdapter
"""
Multi-Agent Agentic AI Simulation for FinTech Compliance & Fraud Detection
Each agent is a function representing a real-world service. The Supervisor coordinates the flow, simulating collaboration and orchestration.
"""
import threading
import queue
import random
import time
import uuid
from agent_logging import agent_logger
from app.adapters.fivetran_adapter import FivetranAdapter
from app.adapters.aws_glue_adapter import AWSGlueAdapter
from app.adapters.dbt_adapter import DBTAdapter
from app.adapters.postgres_adapter import PostgresAdapter
from app.adapters.dynamodb_adapter import DynamoDBAdapter

from app.adapters.snowflake_adapter import SnowflakeAdapter
from app.adapters.sanctions_list_adapter import SanctionsListAdapter
from app.adapters.reg_change_adapter import RegChangeAdapter
from app.adapters.policy_versioning_adapter import PolicyVersioningAdapter
from app.adapters.threat_intel_adapter import ThreatIntelAdapter
from app.adapters.device_fingerprint_adapter import DeviceFingerprintAdapter
from app.adapters.geoip_adapter import GeoIPAdapter
from app.adapters.rule_engine_adapter import RuleEngineAdapter
from app.adapters.risk_score_adapter import RiskScoreAdapter
from app.adapters.fastapi_serving_adapter import FastAPIServingAdapter
from app.adapters.torchserve_adapter import TorchServeAdapter
from app.adapters.tensorflow_serving_adapter import TensorFlowServingAdapter
from app.adapters.kubeflow_adapter import KubeflowAdapter
from app.adapters.shap_adapter import SHAPAdapter
from app.adapters.arize_adapter import ArizeAdapter
from app.adapters.whylogs_adapter import WhylogsAdapter
from app.adapters.monte_carlo_adapter import MonteCarloAdapter
from app.adapters.great_expectations_adapter import GreatExpectationsAdapter
from app.adapters.centralized_observability_dashboard_adapter import CentralizedObservabilityDashboardAdapter
from app.adapters.pagerduty_adapter import PagerDutyAdapter
from app.adapters.audit_log_adapter import AuditLogAdapter
from app.adapters.kafka_adapter import KafkaAdapter

def access_security_agent(in_q, out_q, fail_rate=0.1):
    retries = 2
    data = in_q.get()
    print("[AGENT][Access/Security][Input]", data)
    for attempt in range(retries):
        try:
            print(f"[Access/Security Agent] Enforcing access, consent, and security... (attempt {attempt+1})")
            if random.random() < fail_rate:
                raise Exception("Random Access/Security failure!")
            iam = IAMAdapter()
            consent = ConsentManagementAdapter()
            masking = DataMaskingAdapter()
            cloud = CloudSecurityAdapter()
            vuln = VulnerabilityScannerAdapter()
            result = {
                "iam": iam.validate(iam.transform(iam.fetch())),
                "consent": consent.validate(consent.transform(consent.fetch())),
                "masking": masking.validate(masking.transform(masking.fetch())),
                "cloud": cloud.validate(cloud.transform(cloud.fetch())),
                "vuln": vuln.validate(vuln.transform(vuln.fetch())),
            }
            print("[AGENT][Access/Security][Output]", result)
            out_q.put(("access", result))
            return
        except Exception as e:
            print(f"[Access/Security Agent] Error: {e}")
            time.sleep(1)
    out_q.put(("access_error", "Access/Security failed after retries"))

def reporting_case_agent(in_q, out_q, fail_rate=0.1):
    retries = 2
    data = in_q.get()
    print("[AGENT][Reporting/Case][Input]", data)
    for attempt in range(retries):
        try:
            print(f"[Reporting/Case Agent] Generating reports and managing cases... (attempt {attempt+1})")
            if random.random() < fail_rate:
                raise Exception("Random Reporting/Case failure!")
            reg = RegReportingAdapter()
            case = CaseManagementAdapter()
            portfolio = PortfolioAnalyticsAdapter()
            chatbot = ChatbotAdapter()
            payment = PaymentGatewayAdapter()
            blockchain = BlockchainAdapter()
            data_lineage = DataLineageAdapter()
            data_catalog = DataCatalogAdapter()
            synthetic = SyntheticDataAdapter()
            api_gateway = APIGatewayAdapter()
            mcp = MCPServerAdapter()
            github = GitHubMCPAdapter()
            awsdb = AWSDatabricksMCPAdapter()
            result = {
                "reg": reg.validate(reg.transform(reg.fetch())),
                "case": case.validate(case.transform(case.fetch())),
                "portfolio": portfolio.validate(portfolio.transform(portfolio.fetch())),
                "chatbot": chatbot.validate(chatbot.transform(chatbot.fetch())),
                "payment": payment.validate(payment.transform(payment.fetch())),
                "blockchain": blockchain.validate(blockchain.transform(blockchain.fetch())),
                "data_lineage": data_lineage.validate(data_lineage.transform(data_lineage.fetch())),
                "data_catalog": data_catalog.validate(data_catalog.transform(data_catalog.fetch())),
                "synthetic": synthetic.validate(synthetic.transform(synthetic.fetch())),
                "api_gateway": api_gateway.validate(api_gateway.transform(api_gateway.fetch())),
                "mcp": mcp.validate(mcp.transform(mcp.fetch())),
                "github": github.validate(github.transform(github.fetch())),
                "awsdb": awsdb.validate(awsdb.transform(awsdb.fetch())),
            }
            print("[AGENT][Reporting/Case][Output]", result)
            out_q.put(("reporting", result))
            return
        except Exception as e:
            print(f"[Reporting/Case Agent] Error: {e}")
            time.sleep(1)
    out_q.put(("reporting_error", "Reporting/Case failed after retries"))


def supervisor_agent(etl_fail=0.2, compliance_fail=0.15, fraud_fail=0.15, mlops_fail=0.1, monitoring_fail=0.1, access_fail=0.1, reporting_fail=0.1):
    print("\n[Supervisor Agent] Starting multi-agent orchestration with real-time monitoring, more message types, and agent-to-agent requests...\n")
    agent_timeout = 8  # seconds, can be tuned
    def etl_agent(out_q, fail_rate=0.2):
        retries = 3
        data = None  # ETL agent does not use input queue, but for consistency
        print("[AGENT][ETL][Input]", data)
        for attempt in range(retries):
            try:
                print(f"[ETL Agent] Ingesting and transforming data... (attempt {attempt+1})")
                if random.random() < fail_rate:
                    raise Exception("Random ETL failure!")
                # Use mock transaction and user profile APIs
                transaction = mock_transaction_api()
                print("[MOCK DATA][Transaction]", transaction)
                user_profile = mock_user_profile_api(transaction["user_id"])
                print("[MOCK DATA][UserProfile]", user_profile)
                fivetran = FivetranAdapter()
                glue = AWSGlueAdapter()
                dbt = DBTAdapter()
                pg = PostgresAdapter()
                dy = DynamoDBAdapter()
                sf = SnowflakeAdapter()
                etl_data = {
                    "transaction": transaction,
                    "user_profile": user_profile,
                    "fivetran": fivetran.transform(fivetran.fetch()),
                    "glue": glue.transform(glue.fetch()),
                    "dbt": dbt.transform(dbt.fetch()),
                    "postgres": pg.transform(pg.fetch()),
                    "dynamodb": dy.transform(dy.fetch()),
                    "snowflake": sf.transform(sf.fetch()),
                }
                print("[AGENT][ETL][Output]", etl_data)
                out_q.put(("etl", etl_data))
                return
            except Exception as e:
                print(f"[ETL Agent] Error: {e}")
                time.sleep(1)
        out_q.put(("etl_error", "ETL failed after retries"))

    def compliance_agent(in_q, out_q, fraud_in_q, monitoring_in_q, fail_rate=0.15):
        retries = 2
        data = in_q.get()
        print("[AGENT][Compliance][Input]", data)
        for attempt in range(retries):
            try:
                print(f"[Compliance Agent] Running compliance checks... (attempt {attempt+1})")
                if random.random() < fail_rate:
                    raise Exception("Random Compliance failure!")
                # Use mock user profile for KYC and risk
                user_profile = data.get("user_profile", {})
                kyc_status = user_profile.get("kyc_status", "pending")
                risk_score = user_profile.get("risk_score", 50)
                sanctions = SanctionsListAdapter()
                reg_change = RegChangeAdapter()
                policy = PolicyVersioningAdapter()
                result = {
                    "sanctions": sanctions.validate(sanctions.transform(sanctions.fetch())),
                    "reg_change": reg_change.validate(reg_change.transform(reg_change.fetch())),
                    "policy": policy.validate(policy.transform(policy.fetch())),
                    "kyc_status": kyc_status,
                    "risk_score": risk_score
                }
                if fraud_in_q:
                    if not result["sanctions"] or kyc_status != "verified":
                        fraud_in_q.put({"type": "compliance_alert", "msg": f"Sanctions failed or KYC not verified! (KYC: {kyc_status})", "id": str(uuid.uuid4())})
                    else:
                        fraud_in_q.put({"type": "compliance_info", "msg": "Sanctions passed and KYC verified.", "id": str(uuid.uuid4())})
                if monitoring_in_q:
                    monitoring_in_q.put({"type": "audit_log", "msg": "Compliance check complete.", "id": str(uuid.uuid4())})
                if not result["policy"] and hasattr(compliance_agent, "mlops_in_q"):
                    compliance_agent.mlops_in_q.put({"type": "explain_request", "msg": "Why did policy validation fail?", "from": "compliance", "id": str(uuid.uuid4())})
                print("[AGENT][Compliance][Output]", result)
                out_q.put(("compliance", result))
                return
            except Exception as e:
                print(f"[Compliance Agent] Error: {e}")
                time.sleep(1)
        if monitoring_in_q:
            monitoring_in_q.put({"type": "escalation", "msg": "Compliance failed after retries!", "id": str(uuid.uuid4())})
        out_q.put(("compliance_error", "Compliance failed after retries"))

    def fraud_agent(in_q, out_q, monitoring_in_q, fail_rate=0.15):
        retries = 2
        data = in_q.get()
        print("[AGENT][Fraud][Input]", data)
        transaction = None
        user_profile = None
        if isinstance(data, dict):
            transaction = data.get("transaction")
            user_profile = data.get("user_profile")
        for attempt in range(retries):
            try:
                if isinstance(data, dict) and "type" in data:
                    if data["type"] == "compliance_alert":
                        print(f"[Fraud Agent] Received alert from Compliance: {data['msg']}")
                    elif data["type"] == "compliance_info":
                        print(f"[Fraud Agent] Received info from Compliance: {data['msg']}")
                print(f"[Fraud Agent] Running fraud detection... (attempt {attempt+1})")
                if random.random() < fail_rate:
                    raise Exception("Random Fraud failure!")
                # Use mock fraud check API if transaction and user_profile are present
                fraud_result = None
                if transaction and user_profile:
                    fraud_result = mock_fraud_check_api(transaction, user_profile)
                    print("[MOCK DATA][FraudCheck]", fraud_result)
                threat = ThreatIntelAdapter()
                device = DeviceFingerprintAdapter()
                geoip = GeoIPAdapter()
                rule = RuleEngineAdapter()
                risk = RiskScoreAdapter()
                result = {
                    "threat": threat.validate(threat.transform(threat.fetch())),
                    "device": device.validate(device.transform(device.fetch())),
                    "geoip": geoip.validate(geoip.transform(geoip.fetch())),
                    "rule": rule.validate(rule.transform(rule.fetch())),
                    "risk": risk.validate(risk.transform(risk.fetch())),
                    "mock_fraud": fraud_result
                }
                if monitoring_in_q and (not result["geoip"] or not result["rule"] or (fraud_result and fraud_result["flagged"])):
                    monitoring_in_q.put({"type": "risk_alert", "msg": f"High fraud risk detected! Reason: {fraud_result['reason'] if fraud_result else 'N/A'}", "id": str(uuid.uuid4())})
                print("[AGENT][Fraud][Output]", result)
                out_q.put(("fraud", result))
                return
            except Exception as e:
                print(f"[Fraud Agent] Error: {e}")
                time.sleep(1)
        if monitoring_in_q:
            monitoring_in_q.put({"type": "escalation", "msg": "Fraud failed after retries!", "id": str(uuid.uuid4())})
        out_q.put(("fraud_error", "Fraud failed after retries"))

    def mlops_agent(in_q, out_q, fail_rate=0.1):
        retries = 2
        data = in_q.get()
        print("[AGENT][MLOps][Input]", data)
        explain_requests = []
        if hasattr(mlops_agent, "explain_in_q"):
            while not mlops_agent.explain_in_q.empty():
                msg = mlops_agent.explain_in_q.get()
                if isinstance(msg, dict) and msg.get("type") == "explain_request":
                    explain_requests.append(msg)
        for attempt in range(retries):
            try:
                print(f"[MLOps Agent] Serving and monitoring ML models... (attempt {attempt+1})")
                if random.random() < fail_rate:
                    raise Exception("Random MLOps failure!")
                fastapi = FastAPIServingAdapter()
                torch = TorchServeAdapter()
                tf = TensorFlowServingAdapter()
                kube = KubeflowAdapter()
                shap = SHAPAdapter()
                arize = ArizeAdapter()
                whylogs = WhylogsAdapter()
                monte = MonteCarloAdapter()
                gexp = GreatExpectationsAdapter()
                result = {
                    "fastapi": fastapi.validate(fastapi.transform(fastapi.fetch())),
                    "torch": torch.validate(torch.transform(torch.fetch())),
                    "tf": tf.validate(tf.transform(tf.fetch())),
                    "kubeflow": kube.validate(kube.transform(kube.fetch())),
                    "shap": shap.validate(shap.transform(shap.fetch())),
                    "arize": arize.validate(arize.transform(arize.fetch())),
                    "whylogs": whylogs.validate(whylogs.transform(whylogs.fetch())),
                    "monte": monte.validate(monte.transform(monte.fetch())),
                    "gexp": gexp.validate(gexp.transform(gexp.fetch())),
                }
                for req in explain_requests:
                    print(f"[MLOps Agent] Responding to explain request from {req.get('from')}: {req.get('msg')}")
                print("[AGENT][MLOps][Output]", result)
                out_q.put(("mlops", result))
                return
            except Exception as e:
                print(f"[MLOps Agent] Error: {e}")
                time.sleep(1)
        out_q.put(("mlops_error", "MLOps failed after retries"))

    def monitoring_agent(in_q, out_q, fail_rate=0.1):
        retries = 2
        stop_event = getattr(monitoring_agent, "stop_event", None)
        processed_ids = set()
        data = None  # Monitoring agent does not use input data in the same way
        print("[AGENT][Monitoring][Input]", data)
        for attempt in range(retries):
            try:
                print(f"[Monitoring Agent] Observing system and alerting... (attempt {attempt+1})")
                while True:
                    try:
                        msg = in_q.get(timeout=0.5)
                        if isinstance(msg, dict) and "type" in msg and msg.get("id") not in processed_ids:
                            processed_ids.add(msg.get("id"))
                            if msg["type"] == "risk_alert":
                                print(f"[Monitoring Agent] Received risk alert: {msg['msg']}")
                            elif msg["type"] == "audit_log":
                                print(f"[Monitoring Agent] Audit log: {msg['msg']}")
                            elif msg["type"] == "escalation":
                                print(f"[Monitoring Agent] Escalation: {msg['msg']}")
                    except queue.Empty:
                        if stop_event and stop_event.is_set():
                            break
                        continue
                if random.random() < fail_rate:
                    raise Exception("Random Monitoring failure!")
                dashboard = CentralizedObservabilityDashboardAdapter()
                pagerduty = PagerDutyAdapter()
                audit = AuditLogAdapter()
                kafka = KafkaAdapter()
                result = {
                    "dashboard": dashboard.validate(dashboard.transform(dashboard.fetch())),
                    "pagerduty": pagerduty.validate(pagerduty.transform(pagerduty.fetch())),
                    "audit": audit.validate(audit.transform(audit.fetch())),
                    "kafka": kafka.validate(kafka.transform(kafka.fetch())),
                }
                print("[AGENT][Monitoring][Output]", result)
                out_q.put(("monitoring", result))
                return
            except Exception as e:
                print(f"[Monitoring Agent] Error: {e}")
                time.sleep(1)
        out_q.put(("monitoring_error", "Monitoring failed after retries"))
    # Queues for message passing
    etl_q = queue.Queue()
    compliance_q = queue.Queue()
    fraud_q = queue.Queue()
    mlops_q = queue.Queue()
    monitoring_q = queue.Queue()
    access_q = queue.Queue()
    reporting_q = queue.Queue()

    # Real-time monitoring: use a stop event
    monitoring_stop_event = threading.Event()
    setattr(monitoring_agent, "stop_event", monitoring_stop_event)

    # Agent-to-agent request: compliance can ask MLOps for explanation
    mlops_explain_in_q = queue.Queue()
    setattr(mlops_agent, "explain_in_q", mlops_explain_in_q)
    setattr(compliance_agent, "mlops_in_q", mlops_explain_in_q)

    # Start monitoring agent in real time (with timeout and logging)
    monitoring_in = queue.Queue()
    monitoring_thread = threading.Thread(target=monitoring_agent, args=(monitoring_in, monitoring_q, monitoring_fail))
    agent_logger.log('monitoring', 'start', 'Monitoring agent started')
    monitoring_thread.start()

    # Start ETL agent (single thread, with timeout and logging)
    etl_thread = threading.Thread(target=etl_agent, args=(etl_q, etl_fail))
    agent_logger.log('etl', 'start', 'ETL agent started')
    etl_thread.start()
    etl_thread.join(agent_timeout)
    if etl_thread.is_alive():
        agent_logger.log('etl', 'timeout', f'ETL agent timed out after {agent_timeout}s')
        monitoring_stop_event.set()
        monitoring_thread.join()
        return
    etl_type, etl_data = etl_q.get()
    agent_logger.log('etl', 'end', 'ETL agent finished')
    if etl_type.endswith("error"):
        agent_logger.log('etl', 'error', f'ETL Agent Error: {etl_data}')
        print(f"ETL Agent Error: {etl_data}")
        monitoring_stop_event.set()
        monitoring_thread.join()
        return

    # Advanced: compliance can send alerts/info to fraud, audit_log/escalation to monitoring
    compliance_in = queue.Queue(); compliance_in.put(etl_data)
    fraud_in = queue.Queue(); fraud_in.put(etl_data)
    mlops_in = queue.Queue(); mlops_in.put(etl_data)
    access_in = queue.Queue(); access_in.put(etl_data)
    reporting_in = queue.Queue(); reporting_in.put(etl_data)
    # Pass fraud_in and monitoring_in to compliance_agent, monitoring_in to fraud_agent
    agent_threads = {}
    agent_defs = {
        'compliance': (compliance_agent, (compliance_in, compliance_q, fraud_in, monitoring_in, compliance_fail)),
        'fraud': (fraud_agent, (fraud_in, fraud_q, monitoring_in, fraud_fail)),
        'mlops': (mlops_agent, (mlops_in, mlops_q, mlops_fail)),
        'access': (access_security_agent, (access_in, access_q, access_fail)),
        'reporting': (reporting_case_agent, (reporting_in, reporting_q, reporting_fail)),
    }
    # Start all agent threads with logging
    for name, (func, args) in agent_defs.items():
        agent_logger.log(name, 'start', f'{name.capitalize()} agent started')
        t = threading.Thread(target=func, args=args)
        agent_threads[name] = t
        t.start()
    # Wait for all to finish with timeout
    for name, t in agent_threads.items():
        t.join(agent_timeout)
        if t.is_alive():
            agent_logger.log(name, 'timeout', f'{name.capitalize()} agent timed out after {agent_timeout}s')
    # Collect results
    compliance_type, compliance_results = compliance_q.get()
    fraud_type, fraud_results = fraud_q.get()
    mlops_type, mlops_results = mlops_q.get()
    access_type, access_results = access_q.get()
    reporting_type, reporting_results = reporting_q.get()
    # Error handling and logging
    if compliance_type.endswith("error"):
        agent_logger.log('compliance', 'error', f'Compliance Agent Error: {compliance_results}')
        print(f"Compliance Agent Error: {compliance_results}")
    else:
        agent_logger.log('compliance', 'end', 'Compliance agent finished')
    if fraud_type.endswith("error"):
        agent_logger.log('fraud', 'error', f'Fraud Agent Error: {fraud_results}')
        print(f"Fraud Agent Error: {fraud_results}")
    else:
        agent_logger.log('fraud', 'end', 'Fraud agent finished')
    if mlops_type.endswith("error"):
        agent_logger.log('mlops', 'error', f'MLOps Agent Error: {mlops_results}')
        print(f"MLOps Agent Error: {mlops_results}")
    else:
        agent_logger.log('mlops', 'end', 'MLOps agent finished')
    if access_type.endswith("error"):
        agent_logger.log('access', 'error', f'Access/Security Agent Error: {access_results}')
        print(f"Access/Security Agent Error: {access_results}")
    else:
        agent_logger.log('access', 'end', 'Access/Security agent finished')
    if reporting_type.endswith("error"):
        agent_logger.log('reporting', 'error', f'Reporting/Case Agent Error: {reporting_results}')
        print(f"Reporting/Case Agent Error: {reporting_results}")
    else:
        agent_logger.log('reporting', 'end', 'Reporting/Case agent finished')

    # After all agents finish, stop monitoring
    monitoring_stop_event.set()
    monitoring_thread.join(agent_timeout)
    if monitoring_thread.is_alive():
        agent_logger.log('monitoring', 'timeout', f'Monitoring agent timed out after {agent_timeout}s')
        print("Monitoring agent timed out.")
        monitoring_results = None
    else:
        monitoring_type, monitoring_results = monitoring_q.get()
        if monitoring_type.endswith("error"):
            agent_logger.log('monitoring', 'error', f'Monitoring Agent Error: {monitoring_results}')
            print(f"Monitoring Agent Error: {monitoring_results}")
        else:
            agent_logger.log('monitoring', 'end', 'Monitoring agent finished')

    print("\n[Supervisor Agent] Aggregating results...")
    print("ETL:", etl_data)
    print("Compliance:", compliance_results)
    print("Fraud:", fraud_results)
    print("MLOps:", mlops_results)
    print("Monitoring:", monitoring_results)
    print("Access/Security:", access_results)
    print("Reporting/Case Management:", reporting_results)
    print("\n[Supervisor Agent] Multi-agent simulation with real-time monitoring, more message types, and agent-to-agent requests complete.")
    # Print logs and metrics summary
    print("\n--- Agent Logs ---")
    logs = agent_logger.get_logs()
    for log in logs:
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(log['timestamp']))} [{log['agent']}][{log['msg_type']}] {log['message']}")
    print("\n--- Agent Metrics ---")
    for agent, metrics in agent_logger.get_metrics().items():
        print(f"{agent}:")
        for metric, value, ts in metrics:
            print(f"  {metric}: {value} at {time.strftime('%H:%M:%S', time.localtime(ts))}")
    # Generate sequence diagrams
    generate_sequence_diagram(logs)
    generate_mermaid_sequence(logs)

if __name__ == "__main__":
    # Example: customize failure rates here
    supervisor_agent(
        etl_fail=0.25,  # 25% ETL failure rate
        compliance_fail=0.2,  # 20% Compliance failure rate
        fraud_fail=0.18,  # 18% Fraud failure rate
        mlops_fail=0.12,  # 12% MLOps failure rate
        monitoring_fail=0.15,  # 15% Monitoring failure rate
        access_fail=0.1,  # 10% Access/Security failure rate
        reporting_fail=0.13  # 13% Reporting/Case failure rate
    )
