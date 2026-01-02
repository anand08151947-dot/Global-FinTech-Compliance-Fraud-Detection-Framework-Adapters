import random
import time

def mock_transaction_api():
    # Simulate a transaction API call
    time.sleep(random.uniform(0.05, 0.2))
    return {
        "transaction_id": f"txn_{random.randint(10000,99999)}",
        "amount": round(random.uniform(10, 10000), 2),
        "currency": random.choice(["USD", "EUR", "GBP", "INR"]),
        "country": random.choice(["US", "GB", "IN", "DE", "SG"]),
        "timestamp": time.time(),
        "user_id": f"user_{random.randint(1000,9999)}"
    }

def mock_user_profile_api(user_id=None):
    # Simulate a user profile API call
    time.sleep(random.uniform(0.05, 0.15))
    if not user_id:
        user_id = f"user_{random.randint(1000,9999)}"
    return {
        "user_id": user_id,
        "name": random.choice(["Alice", "Bob", "Charlie", "Diana", "Eve"]),
        "kyc_status": random.choice(["verified", "pending", "rejected"]),
        "risk_score": random.randint(1, 100),
        "country": random.choice(["US", "GB", "IN", "DE", "SG"]),
        "account_age_days": random.randint(1, 2000)
    }

def mock_fraud_check_api(transaction, user_profile):
    # Simulate a fraud check API call
    time.sleep(random.uniform(0.05, 0.2))
    # Simple mock logic
    risk = user_profile["risk_score"]
    amount = transaction["amount"]
    country = transaction["country"]
    kyc = user_profile["kyc_status"]
    flagged = (risk > 80 or amount > 9000 or kyc != "verified" or country not in ["US", "GB", "DE"])
    return {
        "transaction_id": transaction["transaction_id"],
        "flagged": flagged,
        "reason": (
            "High risk" if risk > 80 else
            "Large amount" if amount > 9000 else
            "KYC not verified" if kyc != "verified" else
            "Country not allowed" if country not in ["US", "GB", "DE"] else
            "OK"
        )
    }
