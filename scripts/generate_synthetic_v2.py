"""
Synthetic Financial Scam Dataset Generation Engine (Version 2).

Reconstructs the synthetic financial scam dataset to achieve research-grade realism,
non-deterministic multi-level intent mapping, multi-label social engineering tactics,
natural cross-channel variations, and exact character-level evidence span annotations.

Target: Exactly 7,800 records (600 per each of the 13 subtypes).
Outputs:
  - data/raw/synthetic_financial_scams_v2.csv
  - data/processed/synthetic_financial_scams_v2_processed.csv
"""

import hashlib
import json
import logging
import random
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

import numpy as np
import pandas as pd

# Set deterministic random seed
SEED = 42
random.seed(SEED)
np.random.seed(SEED)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("generate_synthetic_v2")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_OUTPUT_PATH = PROJECT_ROOT / "data" / "raw" / "synthetic_financial_scams_v2.csv"
PROCESSED_OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "synthetic_financial_scams_v2_processed.csv"

# 13 Canonical Subtypes
SUBTYPES = [
    "account_verification",
    "card_transaction_alert",
    "refund_chargeback",
    "invoice_payment_request",
    "loan_offer",
    "investment_crypto",
    "prize_reward",
    "tax_payment",
    "job_task_commission",
    "romance_financial_manipulation",
    "family_emergency_request",
    "recovery_support",
    "charity_donation",
]

# 5 Redesigned Primary Fraudulent Intents
INTENTS = [
    "obtain_credentials_or_codes",
    "obtain_personal_or_financial_information",
    "induce_payment_or_transfer",
    "induce_fraudulent_investment",
    "gain_account_or_device_access",
]

# 9 Atomic Social Engineering Tactics
TACTICS = [
    "authority_impersonation",
    "emotional_manipulation",
    "false_legitimacy",
    "fear_or_threat",
    "reward_or_benefit",
    "scarcity",
    "secrecy",
    "trust_exploitation",
    "urgency",
]

# Subtype-Intent Compatibility Matrix with non-deterministic transition probabilities
SUBTYPE_INTENT_MAP: Dict[str, Dict[str, float]] = {
    "account_verification": {
        "obtain_credentials_or_codes": 0.50,
        "obtain_personal_or_financial_information": 0.35,
        "gain_account_or_device_access": 0.15,
    },
    "card_transaction_alert": {
        "obtain_credentials_or_codes": 0.45,
        "obtain_personal_or_financial_information": 0.35,
        "induce_payment_or_transfer": 0.20,
    },
    "refund_chargeback": {
        "induce_payment_or_transfer": 0.45,
        "obtain_personal_or_financial_information": 0.35,
        "gain_account_or_device_access": 0.20,
    },
    "invoice_payment_request": {
        "induce_payment_or_transfer": 0.70,
        "obtain_personal_or_financial_information": 0.20,
        "obtain_credentials_or_codes": 0.10,
    },
    "loan_offer": {
        "induce_payment_or_transfer": 0.50,
        "obtain_personal_or_financial_information": 0.40,
        "obtain_credentials_or_codes": 0.10,
    },
    "investment_crypto": {
        "induce_fraudulent_investment": 0.75,
        "obtain_credentials_or_codes": 0.15,
        "gain_account_or_device_access": 0.10,
    },
    "prize_reward": {
        "induce_payment_or_transfer": 0.45,
        "obtain_personal_or_financial_information": 0.35,
        "obtain_credentials_or_codes": 0.20,
    },
    "tax_payment": {
        "induce_payment_or_transfer": 0.60,
        "obtain_personal_or_financial_information": 0.25,
        "obtain_credentials_or_codes": 0.15,
    },
    "job_task_commission": {
        "induce_payment_or_transfer": 0.55,
        "obtain_personal_or_financial_information": 0.30,
        "gain_account_or_device_access": 0.15,
    },
    "romance_financial_manipulation": {
        "induce_payment_or_transfer": 0.65,
        "induce_fraudulent_investment": 0.25,
        "gain_account_or_device_access": 0.10,
    },
    "family_emergency_request": {
        "induce_payment_or_transfer": 0.80,
        "obtain_credentials_or_codes": 0.10,
        "obtain_personal_or_financial_information": 0.10,
    },
    "recovery_support": {
        "induce_payment_or_transfer": 0.50,
        "gain_account_or_device_access": 0.30,
        "obtain_credentials_or_codes": 0.20,
    },
    "charity_donation": {
        "induce_payment_or_transfer": 0.75,
        "obtain_personal_or_financial_information": 0.25,
    },
}

# Channel Affinities per Subtype (reflecting realistic digital scam ecology)
SUBTYPE_CHANNEL_MAP: Dict[str, Dict[str, float]] = {
    "account_verification": {"sms": 0.40, "email": 0.30, "notification": 0.25, "chat": 0.05},
    "card_transaction_alert": {"sms": 0.50, "notification": 0.30, "email": 0.15, "chat": 0.05},
    "refund_chargeback": {"email": 0.50, "sms": 0.30, "notification": 0.15, "chat": 0.05},
    "invoice_payment_request": {"email": 0.70, "sms": 0.20, "notification": 0.05, "chat": 0.05},
    "loan_offer": {"sms": 0.45, "email": 0.35, "notification": 0.10, "chat": 0.10},
    "investment_crypto": {"chat": 0.45, "email": 0.30, "sms": 0.15, "notification": 0.10},
    "prize_reward": {"sms": 0.45, "email": 0.35, "notification": 0.15, "chat": 0.05},
    "tax_payment": {"sms": 0.45, "email": 0.40, "notification": 0.15, "chat": 0.00},
    "job_task_commission": {"chat": 0.45, "sms": 0.30, "email": 0.20, "notification": 0.05},
    "romance_financial_manipulation": {"chat": 0.75, "email": 0.20, "sms": 0.05, "notification": 0.00},
    "family_emergency_request": {"sms": 0.50, "chat": 0.45, "email": 0.05, "notification": 0.00},
    "recovery_support": {"email": 0.50, "chat": 0.30, "sms": 0.15, "notification": 0.05},
    "charity_donation": {"email": 0.50, "sms": 0.30, "chat": 0.15, "notification": 0.05},
}

# Semantic Tactic Affinities per Subtype (ensures realistic psychological combinations)
SUBTYPE_TACTIC_AFFINITIES: Dict[str, List[str]] = {
    "account_verification": ["authority_impersonation", "fear_or_threat", "false_legitimacy", "urgency", "secrecy"],
    "card_transaction_alert": ["authority_impersonation", "fear_or_threat", "false_legitimacy", "urgency"],
    "refund_chargeback": ["false_legitimacy", "urgency", "reward_or_benefit", "authority_impersonation"],
    "invoice_payment_request": ["authority_impersonation", "fear_or_threat", "urgency", "false_legitimacy"],
    "loan_offer": ["reward_or_benefit", "scarcity", "urgency", "false_legitimacy"],
    "investment_crypto": ["reward_or_benefit", "scarcity", "secrecy", "trust_exploitation", "urgency"],
    "prize_reward": ["reward_or_benefit", "scarcity", "urgency", "false_legitimacy"],
    "tax_payment": ["authority_impersonation", "fear_or_threat", "false_legitimacy", "urgency", "secrecy"],
    "job_task_commission": ["reward_or_benefit", "scarcity", "urgency", "false_legitimacy"],
    "romance_financial_manipulation": ["emotional_manipulation", "trust_exploitation", "urgency", "secrecy"],
    "family_emergency_request": ["emotional_manipulation", "trust_exploitation", "urgency"],
    "recovery_support": ["authority_impersonation", "false_legitimacy", "urgency", "reward_or_benefit", "secrecy"],
    "charity_donation": ["emotional_manipulation", "urgency", "trust_exploitation", "false_legitimacy"],
}

# Vocabulary and entity pools for realistic variations (no live PII, strictly fictionalized entities)
BANKS = [
    "Apex National Bank", "Horizon Trust Bank", "Summit Federal Credit Union",
    "Beacon Financial", "Vanguard Bancorp", "Pinnacle Bank", "First Crest Bank",
    "MetroUnion Bank", "Silvergate Savings", "Centennial Mutual", "Sterling Chartered Bank",
    "Heritage One Bank", "Pacific Coast Union", "Midland Trust Bancshares"
]
PAYMENT_APPS = [
    "SwiftPay", "ZelleConnect", "CashFlow", "QuickTransfer", "PayLink Mobile",
    "NovaPay", "SecureVenmo", "InstantWire", "DirectWallet", "AppleCash Express"
]
MERCHANTS = [
    "PrimeStore Online", "BestBuy Electronics #841", "Apple Store Manhattan",
    "Walmart Supercenter #2041", "Target Store #1092", "HomeDepot Depot #310",
    "Global Express Retail", "MegaMart Direct", "Zenith Marketplace", "Apex Cart"
]
CRYPTO_PLATFORMS = [
    "BitCrest Capital", "NovaChain Markets", "EtherPeak Trading", "CryptoSphere Assets",
    "PrimeYield Vault", "ChainTrust Exchange", "VaultWave Pro", "AuraCrypto Institutional"
]
TECH_SERVICES = [
    "CloudShield Security", "Apex ID Services", "SecureVault Tech", "NetDefender Support",
    "AuthGuardian Inc.", "OmniTech Solutions", "GeekDefense Technical Desk"
]
CITIES = ["Dallas, TX", "Chicago, IL", "London, UK", "Atlanta, GA", "Miami, FL", "Seattle, WA", "Phoenix, AZ"]
NAMES = ["David", "Michael", "Sarah", "Jennifer", "Robert", "Emily", "James", "Jessica", "Daniel", "Amanda", "Chris", "Emma", "Thomas", "Laura", "Kevin", "Rachel", "Brandon", "Ashley", "Brian", "Megan"]
RELATIONS = ["Mom", "Dad", "Grandma", "Grandpa", "Uncle Dave", "Cousin Mark", "Aunt Lisa", "Sis"]

# Natural Emoji Pools for realistic informal digital communications
EMOJI_POOLS: Dict[str, List[str]] = {
    "romance_financial_manipulation": ["❤️", "💕", "🥺", "🙏", "💔", "✈️", "💍"],
    "family_emergency_request": ["😰", "😭", "🙏", "⚠️", "📱", "🆘"],
    "investment_crypto": ["🚀", "📈", "💰", "💎", "🔥", "⚡"],
    "prize_reward": ["🎉", "🎁", "🥳", "🏆", "🌟", "✨"],
    "job_task_commission": ["💼", "💵", "👍", "✨", "📲"],
    "charity_donation": ["🙏", "❤️", "🤝", "🕊️"],
    "alert": ["🚨", "⚠️", "🔔"]
}

def get_word_shingles(text: str, k: int = 3) -> Set[str]:
    words = re.findall(r"\w+", text.lower())
    if len(words) < k:
        return set(words)
    return set(" ".join(words[i : i + k]) for i in range(len(words) - k + 1))

class FastMinHashLSH:
    def __init__(self, num_perm: int = 64, num_bands: int = 16, seed: int = 42):
        self.num_perm = num_perm
        self.num_bands = num_bands
        self.rows_per_band = num_perm // num_bands
        self.prime = 4294967311
        rng = np.random.default_rng(seed)
        self.a = rng.integers(1, self.prime, size=num_perm, dtype=np.uint64)
        self.b = rng.integers(0, self.prime, size=num_perm, dtype=np.uint64)
        self.buckets: List[Dict[Tuple[int, ...], List[int]]] = [defaultdict(list) for _ in range(num_bands)]
        self.doc_ids: List[str] = []
        self.doc_shingles: List[Set[str]] = []

    def add_documents(self, doc_ids: List[str], texts: List[str]) -> None:
        start_idx = len(self.doc_ids)
        for i, (doc_id, text) in enumerate(zip(doc_ids, texts)):
            shingles = get_word_shingles(text, k=3)
            self.doc_ids.append(doc_id)
            self.doc_shingles.append(shingles)
            curr_idx = start_idx + i
            if not shingles:
                sig = np.zeros(self.num_perm, dtype=np.uint64)
            else:
                th = np.array([int(hashlib.md5(t.encode("utf-8")).hexdigest()[:8], 16) for t in shingles], dtype=np.uint64)
                sig = ((np.outer(self.a, th) + self.b[:, None]) % self.prime).min(axis=1)
            for band in range(self.num_bands):
                start = band * self.rows_per_band
                band_sig = tuple(sig[start : start + self.rows_per_band])
                self.buckets[band][band_sig].append(curr_idx)

    def find_near_duplicates(self, min_jaccard: float = 0.85) -> List[Tuple[str, str, float]]:
        candidate_pairs: Set[Tuple[int, int]] = set()
        for band in range(self.num_bands):
            for bucket in self.buckets[band].values():
                if len(bucket) > 1:
                    for i in range(len(bucket)):
                        for j in range(i + 1, len(bucket)):
                            candidate_pairs.add((min(bucket[i], bucket[j]), max(bucket[i], bucket[j])))
        verified_pairs: List[Tuple[str, str, float]] = []
        for i, j in candidate_pairs:
            s1 = self.doc_shingles[i]
            s2 = self.doc_shingles[j]
            if not s1 or not s2:
                continue
            intersection = len(s1 & s2)
            union = len(s1 | s2)
            if union > 0:
                jaccard = intersection / union
                if jaccard >= min_jaccard:
                    verified_pairs.append((self.doc_ids[i], self.doc_ids[j], round(jaccard, 4)))
        return verified_pairs

class SyntheticGeneratorV2:
    """Generates 7,800 diverse, research-grade synthetic financial scam records."""

    def __init__(self):
        self.records: List[Dict[str, Any]] = []

    def sample_intent(self, subtype: str) -> str:
        intent_dist = SUBTYPE_INTENT_MAP[subtype]
        intents = list(intent_dist.keys())
        probs = list(intent_dist.values())
        return random.choices(intents, weights=probs, k=1)[0]

    def sample_channel(self, subtype: str) -> str:
        chan_dist = SUBTYPE_CHANNEL_MAP[subtype]
        channels = list(chan_dist.keys())
        probs = list(chan_dist.values())
        return random.choices(channels, weights=probs, k=1)[0]

    def sample_tactics(self, subtype: str, intent: str, scenario: str) -> List[str]:
        # Realistic cardinality distribution:
        # ~8% 0-tactic, ~45% 1-tactic, ~40% 2-tactics, ~7% 3-tactics
        card_roll = random.random()
        if card_roll < 0.08:
            k = 0
        elif card_roll < 0.53:
            k = 1
        elif card_roll < 0.93:
            k = 2
        else:
            k = 3

        if k == 0:
            return []

        # Sample strictly from subtype-compatible affinities
        pool = SUBTYPE_TACTIC_AFFINITIES.get(subtype, TACTICS)
        chosen = random.sample(pool, min(k, len(pool)))
        return chosen

    def get_tactic_snippet(self, tactic: str, subtype: str, context: Dict[str, Any]) -> str:
        """Returns authentic, varied evidence phrases for each tactic."""
        bank = context.get("bank", "Apex Bank")
        amount = context.get("amount", "$1,450.00")
        case_id = context.get("case_id", "REF-88219")
        deadline = context.get("deadline", "within 24 hours")
        relation = context.get("relation", "Mom")

        snippets = {
            "authority_impersonation": [
                f"Official notice from {bank} Fraud Investigation Division.",
                f"This communication is issued by the Federal Regulatory Compliance Unit.",
                f"Direct directive from the Chief Risk and Enforcement Officer.",
                f"Issued by the Central Fraud and Loss Prevention Bureau.",
                f"Authorized by senior financial auditor Robert Vance."
            ],
            "emotional_manipulation": [
                f"I am in complete despair and do not know who else can help me through this crisis.",
                f"Please do not abandon me when I need your compassion the most.",
                f"Every passing minute puts an innocent life in severe jeopardy without your support.",
                f"I am sitting in total distress and feeling utterly helpless right now.",
                f"Your immediate kindness can prevent an irreversible tragedy for our family."
            ],
            "false_legitimacy": [
                f"Audit Case Docket: {case_id} registered under statutory financial compliance protocol.",
                f"Pursuant to standard regulatory section 12-CFR-205 electronic transfer oversight.",
                f"Certified clearance code: {case_id}-AUTH verified through centralized ledger.",
                f"Official dispute tracking registration number: {case_id}.",
                f"Statutory validation reference: {case_id} filed with merchant claims registry."
            ],
            "fear_or_threat": [
                f"Immediate arrest warrant and asset freeze will be executed if this balance remains unresolved.",
                f"Failure to act immediately will result in permanent account termination and referral to collection authorities.",
                f"Law enforcement officers will be dispatched to your registered domicile if unresolved.",
                f"Your profile will be classified as delinquent and submitted to criminal fraud enforcement.",
                f"All linked domestic accounts will be seized and subjected to statutory forfeiture."
            ],
            "reward_or_benefit": [
                f"Claim your guaranteed cash reward allocation of {amount} credited directly to your profile.",
                f"You have been pre-approved for an unrestricted credit line of $25,000 at zero introductory interest.",
                f"Unlock your confirmed prize distribution voucher valued at {amount}.",
                f"Secure your daily automated profit distribution averaging 18.5% weekly return.",
                f"Receive an immediate cash disbursement of {amount} upon enrollment."
            ],
            "scarcity": [
                f"Only 2 participant allocations remain available before registration is permanently closed.",
                f"This reservation window is strictly limited to the first ten verified respondents.",
                f"Limited settlement quota expires today and cannot be extended under any circumstance.",
                f"Remaining tier allocation is capped and priority will be assigned on a first-response basis.",
                f"This exclusive opportunity is restricted to a selected cohort of 15 participants."
            ],
            "secrecy": [
                f"Maintain strict confidentiality and avoid discussing this matter with local branch representatives.",
                f"Do not disclose this ongoing internal audit to any third party under any condition.",
                f"Keep this private settlement between us until the documentation is officially archived.",
                f"Operate through this private channel only to preserve investigative security.",
                f"You must not disclose this sensitive security protocol to any family members or colleagues."
            ],
            "trust_exploitation": [
                f"Hi {relation}, it's really me reaching out directly because I trust you completely.",
                f"As your assigned dedicated personal banker at {bank}, I am handling your profile personally.",
                f"Hey, it's your long-time close friend asking for a private favor.",
                f"You know that our mutual bond means everything to me in this difficult moment.",
                f"Reaching out to you directly because I know you have always had my back."
            ],
            "urgency": [
                f"You must complete this mandatory requirement {deadline} to avoid automatic forfeiture.",
                f"Immediate response required before 5:00 PM today.",
                f"Act within the next 60 minutes to prevent irreversible account restriction.",
                f"Time-sensitive alert: immediate verification is required without delay.",
                f"Resolve this pending matter within 2 hours of receiving this notification."
            ]
        }
        return random.choice(snippets[tactic])

    def get_intent_snippet(self, intent: str, subtype: str, context: Dict[str, Any]) -> str:
        """Returns authentic, exact call-to-action phrases matching the assigned intent."""
        amount = context.get("amount", "$1,450.00")
        bank = context.get("bank", "Apex Bank")
        payment_app = context.get("payment_app", "SwiftPay")
        crypto_platform = context.get("crypto_platform", "BitCrest")
        url_domain = context.get("url_domain", "portal-secure-auth.net")

        snippets = {
            "obtain_credentials_or_codes": [
                f"Enter your online banking password and security PIN at https://{url_domain}/login to authenticate.",
                f"Reply with the 6-digit confirmation passcode displayed on your authentication screen.",
                f"Provide your 12-word master secret recovery seed phrase to re-establish account synchronization.",
                f"Verify your master user ID and primary account credentials at https://{url_domain}/verify.",
                f"Submit the one-time authorization passcode sent via SMS to validate your session.",
                f"Input your electronic banking credentials and secondary password to confirm ownership."
            ],
            "obtain_personal_or_financial_information": [
                f"Submit your full Social Security number, date of birth, and mother's maiden name for record reconciliation.",
                f"Confirm your 16-digit debit card number, expiration date, and 3-digit CVV security code.",
                f"Provide your complete banking routing number and checking account digits to update your direct profile.",
                f"Enter your state driver's license number and full residential billing address at https://{url_domain}/identity.",
                f"Verify your taxpayer identification number and primary debit card CVV to complete documentation.",
                f"Provide your full legal name, date of birth, and active credit card details for identity validation."
            ],
            "induce_payment_or_transfer": [
                f"Remit payment of {amount} via wire transfer to our settlement escrow routing account immediately.",
                f"Transfer {amount} through {payment_app} to our designated clearance officer to resolve the balance.",
                f"Send an advance clearance deposit of {amount} via wire transfer to release your funds.",
                f"Settle the required statutory handling fee of {amount} using {payment_app} before the deadline.",
                f"Remit the mandatory documentation fee of {amount} to our accounting escrow department.",
                f"Transfer the required security deposit of {amount} via direct electronic bank wire today."
            ],
            "induce_fraudulent_investment": [
                f"Deposit an initial investment of {amount} into the {crypto_platform} automated arbitrage trading pool.",
                f"Transfer 1,500 USDT to our liquidity contract vault on {crypto_platform} to activate 18% weekly returns.",
                f"Allocate an investment balance of {amount} to our managed crypto hedge contract for guaranteed daily yields.",
                f"Deposit 0.5 BTC into the {crypto_platform} VIP staking node to lock in institutional reward rates.",
                f"Invest {amount} into our private equity cryptocurrency allocation pool to secure pre-launch token rights.",
                f"Fund your new automated trading portfolio with {amount} on {crypto_platform} to start compounding returns."
            ],
            "gain_account_or_device_access": [
                f"Download and launch the AnyDesk remote support client to grant our technician configuration access.",
                f"Install our certified SecurityAgent utility APK from https://{url_domain}/support on your mobile device.",
                f"Install TeamViewer QuickSupport to enable our diagnostic specialist to inspect your active banking session.",
                f"Download and execute the remote assistance application to authorize direct diagnostic connection.",
                f"Grant screen sharing and device administrative permissions through our remote support portal.",
                f"Install the certified client bridge application from https://{url_domain}/setup to restore device synchronization."
            ]
        }
        return random.choice(snippets[intent])

    def get_email_subject(self, subtype: str, context: Dict[str, Any]) -> str:
        """Returns realistic email subjects without revealing the taxonomy subtype name."""
        case_id = context.get("case_id", "CF-99410")
        bank = context.get("bank", "Apex Bank")
        amount = context.get("amount", "$1,450.00")

        subject_templates = {
            "account_verification": [
                f"Security Alert: Unrecognized Device Sign-in Detected on Your {bank} Profile",
                f"Action Required: Annual Identity Re-Certification Protocol",
                f"Important: Multiple Failed Access Attempts - Verify Account Access",
                f"Notice of Security Maintenance: Immediate Profile Re-Authorization Required"
            ],
            "card_transaction_alert": [
                f"Fraud Alert: Suspicious Transaction Flagged on Card Ending in 4102",
                f"Authorization Declined: Verification Needed for Out-of-State Charge",
                f"Urgent: Recurring Subscription Dispute Confirmation ({amount})",
                f"Card Services: Temporary Hold Placed Pending Customer Verification"
            ],
            "refund_chargeback": [
                f"Billing Notification: Automatic Subscription Overcharge Refund ({amount})",
                f"Customer Service: Cancellation Credit Voucher Pending Disbursement",
                f"Reconciliation Notice: Excess Refund Deposit Adjustment Required",
                f"Dispute Resolution: Approved Settlement Credit of {amount}"
            ],
            "invoice_payment_request": [
                f"PAST DUE: Remittance Statement #{case_id} Pending Settlement",
                f"Updated Wire Coordinates for Outstanding Invoice #{case_id}",
                f"Final Notice Before Collection Referral: Invoice Balance {amount}",
                f"Accounts Receivable: Statement #{case_id} Settlement Schedule"
            ],
            "loan_offer": [
                f"Approved: Your Pre-Approved Personal Credit Line of $25,000",
                f"Disbursement Notification: Low-Interest Consolidation Advance Authorized",
                f"Small Business Relief: Immediate Capital Advance Ready for Transfer",
                f"Notice of Credit Authorization: Same-Day Disbursement Scheduled"
            ],
            "investment_crypto": [
                f"Private Placement Invitation: High-Yield Automated Arbitrage Pool",
                f"Market Intelligence: Institutional Liquidity Staking Rewards",
                f"VIP Allocation: Proprietary Algorithmic Trading Access",
                f"Asset Management: Exclusive Cross-Exchange Yield Optimization"
            ],
            "prize_reward": [
                f"Winner Notification: Selected Entry for Annual Customer Sweepstakes",
                f"Official Award Distribution: Unclaimed Voucher of {amount}",
                f"Loyalty Milestone Selection: Promotional Grant Distribution Notice",
                f"Claim Confirmation: Promotional Grand Prize Clearance"
            ],
            "tax_payment": [
                f"STATUTORY AUDIT NOTICE: Underreported Assessment Docket #{case_id}",
                f"Internal Compliance Division: Delinquent Statutory Tax Obligation",
                f"Final Statutory Notice: Warrant Execution Scheduled for File #{case_id}",
                f"Statutory Wage Discrepancy: Immediate Reconciliation Required"
            ],
            "job_task_commission": [
                f"Onboarding Invitation: Remote Merchant Review Specialist ($45/hr)",
                f"Flexible Remote Opportunity: Digital Evaluation Project Acceptance",
                f"HR Welcome Packet: Daily Commission Task Specialist Program",
                f"Career Opportunity: Quality Assurance Logistics Onboarding"
            ],
            "romance_financial_manipulation": [
                f"My love, please read this as soon as you can - urgent update",
                f"Emergency overseas - I need your help right away",
                f"Thinking of you constantly - unexpected crisis at border customs",
                f"My darling, an urgent situation happened and I need to tell you"
            ],
            "family_emergency_request": [
                f"Urgent: Family emergency while traveling - please read immediately",
                f"Please help - emergency while away from home",
                f"Need your urgent help - unexpected accident on the road",
                f"Family Notice: Urgent medical situation requiring immediate assistance"
            ],
            "recovery_support": [
                f"Investigation Update: Traced Lost Assets in Docket #{case_id}",
                f"Court Restitution Distribution: Claim Verification for {amount}",
                f"Consumer Advocacy Restitution: Retrieved Balance Ready for Release",
                f"Cyber Incident Resolution: Asset Recovery Protocol Finalized"
            ],
            "charity_donation": [
                f"Urgent Appeal: Emergency Relief for Displaced Disaster Families",
                f"Critical Medical Fund: Help Sponsor Emergency Pediatric Care",
                f"Community Shelter Drive: Urgent Operational Aid Needed Today",
                f"Winter Humanitarian Relief: Emergency Kits for Homeless Veterans"
            ]
        }
        return random.choice(subject_templates[subtype])

    def generate_single_record(self, subtype: str, record_idx: int) -> Dict[str, Any]:
        """Synthesizes one realistic record with exact, verified character offsets."""
        channel = self.sample_channel(subtype)
        intent = self.sample_intent(subtype)

        # Context generation
        bank = random.choice(BANKS)
        payment_app = random.choice(PAYMENT_APPS)
        merchant = random.choice(MERCHANTS)
        crypto_platform = random.choice(CRYPTO_PLATFORMS)
        tech_service = random.choice(TECH_SERVICES)
        city = random.choice(CITIES)
        name = random.choice(NAMES)
        relation = random.choice(RELATIONS)
        amount = f"${random.randint(150, 4850):,}.{random.choice(['00', '50', '80', '95'])}"
        case_id = f"CF-{random.randint(10000, 99999)}"
        deadline = random.choice(["within 24 hours", "before 5:00 PM today", "within 2 hours", "by tomorrow morning"])
        domain_suffix = random.choice(["portal-verify.net", "auth-alert-center.com", "secure-wire-desk.org", "claims-clearance.net"])
        url_domain = f"{bank.lower().split()[0]}-{domain_suffix}"

        context = {
            "bank": bank,
            "payment_app": payment_app,
            "merchant": merchant,
            "crypto_platform": crypto_platform,
            "tech_service": tech_service,
            "city": city,
            "name": name,
            "relation": relation,
            "amount": amount,
            "case_id": case_id,
            "deadline": deadline,
            "url_domain": url_domain
        }

        # Scenario selection
        scenarios_per_subtype = {
            "account_verification": ["new_device_login", "kyc_profile_update", "failed_login_lock", "mfa_reset_alert"],
            "card_transaction_alert": ["unauthorized_retail_charge", "foreign_atm_withdrawal", "disputed_online_order", "recurring_charge_hold"],
            "refund_chargeback": ["software_overcharge_rebate", "accidental_transfer_reversal", "airline_cancellation_credit", "merchant_billing_adjustment"],
            "invoice_payment_request": ["overdue_vendor_invoice", "updated_wire_instruction", "freight_customs_invoice", "annual_software_maintenance"],
            "loan_offer": ["preapproved_personal_loan", "debt_consolidation_advance", "business_relief_grant", "instant_payday_line"],
            "investment_crypto": ["algorithmic_arbitrage_bot", "liquidity_pool_staking", "exclusive_ico_allocation", "insider_signals_mentorship"],
            "prize_reward": ["retail_shopper_sweepstakes", "international_jackpot_draw", "customer_loyalty_anniversary", "unclaimed_cash_grant"],
            "tax_payment": ["irs_audit_settlement", "delinquent_tax_lien", "unclaimed_state_refund", "statutory_withholding_notice"],
            "job_task_commission": ["app_rating_optimization", "video_review_task", "remote_data_entry_clerk", "package_reshipment_inspector"],
            "romance_financial_manipulation": ["overseas_medical_crisis", "customs_luggage_clearance", "transit_visa_emergency", "joint_investment_future"],
            "family_emergency_request": ["broken_phone_impersonation", "traffic_accident_settlement", "stranded_traveler_robbery", "emergency_medical_clinic"],
            "recovery_support": ["blockchain_forensic_recovery", "court_restitution_disbursement", "chargeback_advocacy_retainer", "hacked_account_restoration"],
            "charity_donation": ["disaster_relief_appeal", "critically_ill_child", "animal_shelter_eviction", "homeless_veterans_drive"]
        }
        scenario = random.choice(scenarios_per_subtype[subtype])
        tactics = self.sample_tactics(subtype, intent, scenario)

        # Generate narrative evidence snippet
        narrative_templates = {
            "account_verification": [
                f"An unrecognized login attempt was detected from a new device located in {city}.",
                f"Your online banking profile requires mandatory annual identity re-certification under security protocol.",
                f"Your access has been placed on temporary administrative hold following three invalid passcode attempts.",
                f"A request to update your primary multi-factor authentication phone number was received."
            ],
            "card_transaction_alert": [
                f"A pending authorization of {amount} at {merchant} was flagged by automated fraud monitoring.",
                f"An out-of-state ATM cash withdrawal of {amount} was attempted in {city}.",
                f"A recurring subscription charge of {amount} for {tech_service} was flagged as unusual.",
                f"Your debit card was temporarily locked after a suspicious transaction attempt of {amount}."
            ],
            "refund_chargeback": [
                f"An automated overcharge of {amount} for your {tech_service} subscription is pending full refund.",
                f"An erroneous billing adjustment created an excess refund balance of {amount} requiring reconciliation.",
                f"Your travel booking cancellation credit of {amount} has been approved for account disbursement.",
                f"A merchant dispute adjustment of {amount} from {merchant} is waiting to be credited to your balance."
            ],
            "invoice_payment_request": [
                f"Outstanding billing statement INV-8921 for {amount} from {tech_service} is past due for settlement.",
                f"Please note our corporate banking coordinates have been updated for pending invoice INV-4402 ({amount}).",
                f"Customs freight processing invoice #{case_id} totaling {amount} requires immediate payment for cargo release.",
                f"Annual software maintenance statement INV-7719 for {amount} requires settlement to prevent license termination."
            ],
            "loan_offer": [
                f"You have been pre-approved for an unsecured personal loan of $25,000 at a fixed 3.2% annual rate.",
                f"Your application for an emergency debt consolidation credit line of $35,000 has been formally approved.",
                f"A small business relief advance of $50,000 is ready for direct disbursement into your checking account.",
                f"You qualify for an instant same-day payday line of credit of $5,000 with no credit bureau check."
            ],
            "investment_crypto": [
                f"Our proprietary AI algorithmic trading engine on {crypto_platform} achieved an audited 24.5% monthly return.",
                f"A private pre-sale token allocation on {crypto_platform} is open exclusively to verified community members.",
                f"Our institutional liquidity pool on {crypto_platform} is offering 320% annualized staking distribution.",
                f"Our VIP trading mentor channel has maintained a 94% win rate across cross-exchange arbitrage signals."
            ],
            "prize_reward": [
                f"You have been selected as the grand prize winner in our seasonal customer sweepstakes drawing.",
                f"Your customer profile was drawn to receive an unallocated loyalty milestone reward of {amount}.",
                f"Official winner notification: your entry ticket was awarded the {amount} retail promotional grant.",
                f"You have an unclaimed merchandise voucher and cash bonus totaling {amount} awaiting verification."
            ],
            "tax_payment": [
                f"Statutory audit docket #{case_id} identified an underreported income tax liability totaling {amount}.",
                f"A formal federal tax lien has been issued regarding outstanding delinquent tax obligations of {amount}.",
                f"An uncollected tax rebate of {amount} from the previous statutory filing year has been processed.",
                f"A discrepancy in your annual wage withholding report requires immediate statutory reconciliation of {amount}."
            ],
            "job_task_commission": [
                f"Earn between $250 and $450 daily by completing merchant mobile application optimization evaluations.",
                f"Flexible remote position available reviewing digital media content with guaranteed daily disbursements.",
                f"Work-from-home logistics quality inspector opening offering $45.00 per hour with weekly direct deposits.",
                f"Complete simple daily digital feedback tasks and earn immediate commission payments averaging $300 daily."
            ],
            "romance_financial_manipulation": [
                f"My darling, I am stranded overseas and faced with an unforeseen medical emergency requiring immediate surgery.",
                f"My dear, the international shipping agent is holding my personal luggage and valuable gifts at border customs.",
                f"My love, transit border control is requiring an emergency entry visa deposit before I can board my flight to you.",
                f"Sweetheart, if we combine our savings into this exclusive {crypto_platform} investment, we can buy our dream house."
            ],
            "family_emergency_request": [
                f"Hi {relation}, my phone was severely damaged in an accident so I am messaging you from this temporary line.",
                f"Hey {relation}, I was involved in an unexpected fender bender and need to settle the repair before police arrive.",
                f"Dear {relation}, I was mugged while traveling abroad and lost my wallet, phone, and emergency funds.",
                f"Hi {relation}, I am at an urgent care medical clinic and my primary health coverage is not being accepted."
            ],
            "recovery_support": [
                f"Our blockchain forensic intelligence unit has successfully traced your previously stolen funds of {amount}.",
                f"You are named in court restitution docket #{case_id} to receive recovered fraud compensation of {amount}.",
                f"Our specialized financial advocacy bureau has finalized chargeback recovery for your fraudulent transaction.",
                f"Our cybersecurity incident team has isolated the compromised access point and prepared full balance restoration."
            ],
            "charity_donation": [
                f"Urgent humanitarian appeal: displaced disaster victims are without emergency shelter, food, or clean water.",
                f"Emergency medical relief drive: young patients facing critical operations need urgent sponsorship support.",
                f"Our community animal shelter faces imminent shutdown and desperately needs emergency operational funding.",
                f"Winter relief drive for displaced homeless veterans requiring urgent nutrition and emergency winter kits."
            ]
        }
        narrative_snippet = random.choice(narrative_templates[subtype])

        # Get intent call-to-action snippet
        intent_snippet = self.get_intent_snippet(intent, subtype, context)

        # Get tactic snippets
        tactic_snippets = []
        for t in tactics:
            t_snip = self.get_tactic_snippet(t, subtype, context)
            tactic_snippets.append((t, t_snip))

        # Natural emoji injection (concentrated in informal chats, informal SMS, and mobile alerts)
        emoji_prefix = ""
        emoji_suffix = ""
        
        # Sample emoji if appropriate
        if subtype in EMOJI_POOLS and random.random() < 0.55:
            e = random.choice(EMOJI_POOLS[subtype])
            if channel == "sms" and random.random() < 0.40:
                emoji_prefix = f"{e} "
            elif channel == "chat":
                emoji_suffix = f" {e}"
        elif channel == "notification" and random.random() < 0.25:
            e = random.choice(EMOJI_POOLS["alert"])
            emoji_prefix = f"{e} "

        # Compose realistic text based on channel
        if channel == "sms":
            # Concise SMS formatting
            parts = [narrative_snippet]
            for _, t_snip in tactic_snippets:
                parts.append(t_snip)
            parts.append(intent_snippet)
            body_text = " ".join(parts)
            if emoji_suffix:
                body_text += emoji_suffix
            full_text = f"{emoji_prefix}{body_text}".strip()
            email_subject = ""
            email_body = ""

        elif channel == "notification":
            # Mobile push notification / alert banner
            app_title = random.choice([f"[{bank} Alert]", f"[{payment_app} Notice]", "[Security Center]", "[Wallet Alert]", "[System Notice]"])
            parts = [narrative_snippet]
            for _, t_snip in tactic_snippets:
                parts.append(t_snip)
            parts.append(intent_snippet)
            body_content = " ".join(parts)
            full_text = f"{emoji_prefix}{app_title} {body_content}".strip()
            email_subject = ""
            email_body = ""

        elif channel == "email":
            # Realistic email with subject line, greeting, body paragraphs, and professional sign-off
            email_subject = self.get_email_subject(subtype, context)
            
            if subtype in ["family_emergency_request", "romance_financial_manipulation"]:
                greeting = random.choice([f"Dear {relation},", f"Hey {relation},", "My dearest,", "Dearest,"])
                signoff_title = random.choice(["Love always,", "With love,", "Thinking of you,", "Yours,"])
            else:
                greeting = random.choice([f"Dear Valued Client,", f"Attention Account Holder,", f"Dear {name},", f"Valued Customer,"])
                signoff_title = random.choice([
                    f"Operations & Security Team\n{bank}",
                    f"Client Risk Management\n{tech_service}",
                    f"Regulatory Compliance Officer\nCase Division",
                    f"Dispute Support Services\n{payment_app}"
                ])
            
            body_paragraphs = [narrative_snippet]
            if tactic_snippets:
                t_block = " ".join([snip for _, snip in tactic_snippets])
                body_paragraphs.append(t_block)
            body_paragraphs.append(intent_snippet)
            
            body_text = "\n\n".join(body_paragraphs)
            email_body = f"{greeting}\n\n{body_text}\n\nSincerely,\n{signoff_title}"
            full_text = f"Subject: {email_subject}\n\n{email_body}"

        elif channel == "chat":
            # Believable multi-turn chat format with context-aware speaker identities
            if subtype == "family_emergency_request":
                speaker_rep = random.choice(["Kevin", "Sarah", "Alex", "Jordan", "Emma", "Chris"])
                speaker_user = relation
            elif subtype == "romance_financial_manipulation":
                speaker_rep = random.choice(["Elena", "Julian", "Marcus", "Sophia", "Daniel", "Chloe"])
                speaker_user = "Honey"
            elif subtype == "charity_donation":
                speaker_rep = random.choice(["Volunteer_Maya", "Coordinator_Tom", "Aid_Worker_Dan"])
                speaker_user = "Supporter"
            else:
                speaker_rep = random.choice(["Support_Agent", "Desk_Officer", "Alex", "Jordan", "Advisor_Morgan"])
                speaker_user = "You"

            chat_emoji_1 = f" {random.choice(EMOJI_POOLS[subtype])}" if (subtype in EMOJI_POOLS and random.random() < 0.35) else ""
            chat_emoji_3 = f" {random.choice(EMOJI_POOLS[subtype])}" if (subtype in EMOJI_POOLS and random.random() < 0.40) else ""

            t1 = f"[{random.randint(9, 11)}:{random.randint(10, 59):02d} AM] {speaker_rep}: {narrative_snippet}{chat_emoji_1}"
            t2 = f"[{random.randint(9, 11)}:{random.randint(10, 59):02d} AM] {speaker_user}: What happened? What do I need to do right now?"
            
            t3_elements = []
            for _, t_snip in tactic_snippets:
                t3_elements.append(t_snip)
            t3_elements.append(intent_snippet)
            t3_text = " ".join(t3_elements)
            t3 = f"[{random.randint(9, 11)}:{random.randint(10, 59):02d} AM] {speaker_rep}: {t3_text}{chat_emoji_3}"
            
            full_text = f"{t1}\n{t2}\n{t3}"
            email_subject = ""
            email_body = ""

        # Validate and extract exact character-level offsets
        # Intent span
        intent_start = full_text.find(intent_snippet)
        if intent_start == -1:
            raise ValueError(f"Intent snippet not found in text: {intent_snippet}")
        intent_end = intent_start + len(intent_snippet)
        assert full_text[intent_start:intent_end] == intent_snippet, "Intent span slice mismatch!"

        primary_intent_evidence = {
            "start_char": intent_start,
            "end_char": intent_end,
            "span_text": intent_snippet
        }

        # Narrative span
        narrative_start = full_text.find(narrative_snippet)
        if narrative_start == -1:
            raise ValueError(f"Narrative snippet not found in text: {narrative_snippet}")
        narrative_end = narrative_start + len(narrative_snippet)
        assert full_text[narrative_start:narrative_end] == narrative_snippet, "Narrative span slice mismatch!"

        narrative_evidence = {
            "start_char": narrative_start,
            "end_char": narrative_end,
            "span_text": narrative_snippet
        }

        # Tactics spans
        tactics_evidence_list = []
        for t_name, t_snip in tactic_snippets:
            t_start = full_text.find(t_snip)
            if t_start == -1:
                raise ValueError(f"Tactic snippet '{t_snip}' not found in text!")
            t_end = t_start + len(t_snip)
            assert full_text[t_start:t_end] == t_snip, f"Tactic span slice mismatch for {t_name}!"
            tactics_evidence_list.append({
                "tactic": t_name,
                "start_char": t_start,
                "end_char": t_end,
                "span_text": t_snip
            })

        record_id = f"SYN2-{record_idx:05d}"

        return {
            "record_id": record_id,
            "text": full_text,
            "label": 1,
            "phishing_type": subtype,
            "scam_subtype": subtype,
            "scam_channel": channel,
            "channel": channel,
            "fraudulent_intent": intent,
            "social_engineering_tactics": json.dumps(tactics),
            "primary_intent_evidence": json.dumps(primary_intent_evidence),
            "tactics_evidence": json.dumps(tactics_evidence_list),
            "narrative_evidence": json.dumps(narrative_evidence),
            "language": "en",
            "synthetic": True,
            "is_synthetic": True,
            "generation_scenario": scenario,
            "risk_or_safety_note": "Fictionalized synthetic scam message generated for multi-level research with verified character spans.",
            "email_subject": email_subject,
            "email_body": email_body,
        }

    def generate_all(self, target_per_subtype: int = 600) -> pd.DataFrame:
        """Generates exactly target_per_subtype records for each of the 13 subtypes."""
        logger.info(f"Beginning generation of {len(SUBTYPES)} subtypes x {target_per_subtype} = {len(SUBTYPES)*target_per_subtype} records...")
        record_counter = 1
        all_records = []

        for subtype in SUBTYPES:
            logger.info(f"Generating 600 records for subtype: {subtype}...")
            for _ in range(target_per_subtype):
                rec = self.generate_single_record(subtype, record_counter)
                all_records.append(rec)
                record_counter += 1

        df = pd.DataFrame(all_records)
        logger.info(f"Generation complete. Total records created: {len(df):,}")
        return df


def normalize_text_canonical(text: str) -> str:
    """Harmonizes entities to canonical bracket placeholders."""
    norm = text
    # URLs
    norm = re.sub(r"https?://[^\s<>\"']+", "[URL]", norm)
    # Emails
    norm = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "[EMAIL_ADDRESS]", norm)
    # Phone numbers
    norm = re.sub(r"\b(?:\+?1[-.]?)?\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}\b", "[PHONE_NUMBER]", norm)
    # Amounts ($X,XXX.XX or $XX)
    norm = re.sub(r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?", "[AMOUNT]", norm)
    # Case / Reference numbers (CF-XXXXX, INV-XXXX, etc.)
    norm = re.sub(r"\b(?:CF|INV|REF|TX|REC)-\d{4,6}(?:-[A-Z]+)?\b", "[IDENTIFIER]", norm)
    # Normalize extra whitespace
    norm = " ".join(norm.split())
    return norm


def run_pipeline():
    logger.info("Initializing Synthetic Financial Scam Reconstruction Engine (V2)...")
    generator = SyntheticGeneratorV2()
    df_raw = generator.generate_all(target_per_subtype=600)

    # Rigorous QA on Raw Records
    logger.info("Executing comprehensive QA verification on generated raw data...")
    assert len(df_raw) == 7800, f"Expected 7,800 records, got {len(df_raw)}"

    # Check prohibited artifacts: V1 template prefixes (NOTICE <N>:), 'fictional', 'synthetic', 'simulation', or unedited LLM instructions
    prohibited_patterns = [
        r"\bNOTICE\s+\d+:",
        r"\bfictional\b",
        r"\bsynthetic\b",
        r"\bsimulation\b",
        r"\bAI language model\b",
        r"\bgenerate an example\b"
    ]
    for pat in prohibited_patterns:
        matches = df_raw["text"].str.contains(pat, regex=True, case=False, na=False).sum()
        assert matches == 0, f"Prohibited artifact pattern '{pat}' found in {matches} messages!"
    logger.info("PROHIBITED TOKEN CHECK: 0 occurrences of 'fictional', 'synthetic', 'NOTICE <N>:', or LLM instructions.")

    # Verify 100% of character spans
    logger.info("Verifying character-level offsets across all 7,800 records...")
    for idx, row in df_raw.iterrows():
        txt = row["text"]
        # Intent span
        pie = json.loads(row["primary_intent_evidence"])
        assert txt[pie["start_char"]:pie["end_char"]] == pie["span_text"], f"Intent offset failure at row {idx}"
        # Narrative span
        ne = json.loads(row["narrative_evidence"])
        assert txt[ne["start_char"]:ne["end_char"]] == ne["span_text"], f"Narrative offset failure at row {idx}"
        # Tactics spans
        te_list = json.loads(row["tactics_evidence"])
        for te in te_list:
            assert txt[te["start_char"]:te["end_char"]] == te["span_text"], f"Tactics offset failure at row {idx}"
    logger.info("CHARACTER SPAN VERIFICATION: 100.00% exact substring match verified across all records.")

    # Export Raw Dataset
    RAW_OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    raw_columns = [
        "id", "text", "label", "phishing_type", "scam_channel",
        "fraudulent_intent", "social_engineering_tactics",
        "primary_intent_evidence", "tactics_evidence", "narrative_evidence",
        "language", "synthetic", "generation_scenario", "risk_or_safety_note"
    ]
    df_raw_export = df_raw.rename(columns={"record_id": "id"})[raw_columns]
    df_raw_export.to_csv(RAW_OUTPUT_PATH, index=False, encoding="utf-8")
    logger.info(f"Saved raw dataset to: {RAW_OUTPUT_PATH} ({len(df_raw_export):,} records)")

    # Execute Preprocessing & Deduplication for Canonical Processed Dataset
    logger.info("Building canonical processed dataset with placeholder harmonization and LSH deduplication...")
    
    # Placeholder normalization
    df_proc = df_raw.copy()
    df_proc["original_text"] = df_proc["text"]
    df_proc["normalized_text"] = df_proc["text"].apply(normalize_text_canonical)

    # Length and count profiling
    df_proc["char_count_original"] = df_proc["original_text"].str.len()
    df_proc["word_count_original"] = df_proc["original_text"].str.split().str.len()
    df_proc["char_count_normalized"] = df_proc["normalized_text"].str.len()
    df_proc["word_count_normalized"] = df_proc["normalized_text"].str.split().str.len()

    # Placeholder counts
    placeholder_pattern = re.compile(r"\[(?:URL|EMAIL_ADDRESS|PHONE_NUMBER|AMOUNT|IDENTIFIER|ORGANIZATION|DATE_TIME)\]")
    df_proc["placeholder_count_original"] = df_proc["original_text"].apply(lambda t: len(placeholder_pattern.findall(t)))
    df_proc["placeholder_count_normalized"] = df_proc["normalized_text"].apply(lambda t: len(placeholder_pattern.findall(t)))

    # Canonical metadata fields
    df_proc["original_channel"] = df_proc["channel"]
    df_proc["is_email_gateway"] = False
    df_proc["has_gateway_headers"] = False
    df_proc["source"] = "synthetic_financial_scams_v2"
    df_proc["source_url"] = "local_generation_v2"
    df_proc["source_license"] = "research_only"
    df_proc["source_record_id"] = df_proc["record_id"]
    df_proc["legitimate_category"] = np.nan
    df_proc["communication_type"] = "scam"

    # Fast MinHash LSH deduplication
    logger.info("Running MinHash LSH near-duplicate clustering (threshold = 0.85)...")
    lsh = FastMinHashLSH(num_perm=64, num_bands=16, seed=SEED)
    lsh.add_documents(df_proc["record_id"].tolist(), df_proc["normalized_text"].tolist())
    dup_pairs = lsh.find_near_duplicates(min_jaccard=0.85)
    logger.info(f"Discovered {len(dup_pairs)} near-duplicate pairs in normalized space.")

    # Assign cluster IDs
    adj = defaultdict(set)
    for id1, id2, _ in dup_pairs:
        adj[id1].add(id2)
        adj[id2].add(id1)

    visited = set()
    cluster_mapping = {}
    cluster_num = 1
    for doc_id in df_proc["record_id"]:
        if doc_id in adj and doc_id not in visited:
            comp = []
            queue = [doc_id]
            visited.add(doc_id)
            while queue:
                curr = queue.pop(0)
                comp.append(curr)
                for neighbor in adj[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            cid = f"SYN2_C{cluster_num:04d}"
            cluster_num += 1
            for member in comp:
                cluster_mapping[member] = cid

    df_proc["duplicate_cluster_id"] = df_proc["record_id"].map(cluster_mapping).fillna("")
    clustered_count = (df_proc["duplicate_cluster_id"] != "").sum()
    logger.info(f"Grouped {clustered_count} records into {cluster_num - 1} near-duplicate clusters.")

    # Canonical column ordering
    processed_cols = [
        "record_id", "original_text", "normalized_text", "label", "channel",
        "original_channel", "is_email_gateway", "has_gateway_headers",
        "source", "source_url", "source_license", "source_record_id",
        "is_synthetic", "scam_subtype", "fraudulent_intent",
        "social_engineering_tactics", "primary_intent_evidence",
        "tactics_evidence", "narrative_evidence", "legitimate_category",
        "email_subject", "email_body", "duplicate_cluster_id",
        "char_count_original", "word_count_original",
        "char_count_normalized", "word_count_normalized",
        "placeholder_count_original", "placeholder_count_normalized",
        "generation_scenario", "risk_or_safety_note", "language", "communication_type"
    ]
    df_proc_export = df_proc[processed_cols]
    PROCESSED_OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df_proc_export.to_csv(PROCESSED_OUTPUT_PATH, index=False, encoding="utf-8")
    logger.info(f"Saved processed dataset to: {PROCESSED_OUTPUT_PATH} ({len(df_proc_export):,} records)")

    logger.info("Generation, QA, and Preprocessing completed successfully.")


if __name__ == "__main__":
    run_pipeline()
