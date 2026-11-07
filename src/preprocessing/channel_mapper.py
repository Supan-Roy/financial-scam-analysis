"""
Channel Harmonization and Email Gateway Detection Module.

This module maps raw channel strings across heterogeneous sources to canonical
communication channels ('email', 'sms', 'chat', 'notification'), while identifying
email-to-SMS gateway delivery mechanisms and header markers based on empirical source evidence.
"""

import re
import logging
from typing import Tuple, Dict, Any, Optional

logger = logging.getLogger(__name__)

# Precompiled regex for email-to-SMS carrier gateway headers.
# Captures standard carrier gateway delivery headers:
# - Messages starting with FRM: (e.g. 'FRM:Chase Alert SUBJ:... MSG:...')
# - Messages with multi-field carrier headers (FRM/FROM followed by SUBJ/MSG/CONTENT)
RE_GATEWAY_HEADERS = re.compile(
    r"(?:^FRM:|(?:^|\n|\s)(?:FRM|FROM):\s*.*?\b(?:SUBJ|MSG|CONTENT):|\bFRM:\s*.*?\b(?:SUBJ:|MSG:))",
    re.IGNORECASE | re.DOTALL,
)


class ChannelHarmonizer:
    """
    Channel harmonization engine with gateway transmission profiling.
    """

    def __init__(self):
        # Canonical channel set
        self.canonical_channels = {"email", "sms", "chat", "notification"}

    @staticmethod
    def detect_gateway_headers(text: str) -> bool:
        """
        Determines whether message text contains explicit email-to-SMS carrier
        gateway transport headers (e.g. 'FRM:... SUBJ:... MSG:...').
        """
        if not isinstance(text, str) or not text:
            return False
        if text.startswith("FRM:"):
            return True
        return bool(RE_GATEWAY_HEADERS.search(text))

    def harmonize_channel(
        self,
        raw_channel: Optional[str],
        source: Optional[str],
        text: Optional[str],
    ) -> Tuple[str, bool, bool]:
        """
        Harmonizes raw channel label into canonical channel and evaluates gateway flags.

        Rules:
        - `channel`: Canonical communication medium ('sms', 'email', 'chat', 'notification').
        - `original_channel`: Preserved raw channel string from upstream source.
        - `has_gateway_headers`: True if text contains explicit carrier transport headers.
        - `is_email_gateway`: True ONLY when email-to-SMS gateway transport is supported
          by empirical source evidence (presence of carrier gateway headers/origin).
          Ordinary mobile SMS records (including the 9,576+ records in IMC25 without
          gateway evidence) receive is_email_gateway = False.

        Returns:
            Tuple of:
            - canonical_channel (str): 'email', 'sms', 'chat', 'notification', or raw if unmapped
            - is_email_gateway (bool): True if gateway transport is supported by source evidence
            - has_gateway_headers (bool): True if message contains explicit transport headers
        """
        raw_clean = str(raw_channel).strip().lower() if raw_channel is not None else "unknown"
        source_clean = str(source).strip() if source is not None else ""
        text_str = str(text) if text is not None else ""

        has_headers = self.detect_gateway_headers(text_str)

        # 1. IMC25 Compound Channel: sms/email
        # Provenance: IMC25 Smishing Dataset contains public user-reported mobile smishing
        # messages delivered to cellular handsets. The compound label 'sms/email' denoted
        # that mobile reports could have originated via SMS or carrier email-to-SMS gateways.
        # Only records with explicit gateway evidence receive is_email_gateway = True.
        # Ordinary mobile SMS messages must NOT be labelled as email gateways.
        if raw_clean == "sms/email":
            canonical_channel = "sms"
            is_gateway = has_headers  # True only if empirical gateway header evidence exists
            return canonical_channel, is_gateway, has_headers

        # 2. Standard SMS (UCI SMS, Mendeley, smishtank, synthetic)
        if raw_clean == "sms":
            canonical_channel = "sms"
            is_gateway = has_headers  # In smishtank, gateway headers also indicate gateway delivery
            return canonical_channel, is_gateway, has_headers

        # 3. Standard Email (MeAJOR, Nigerian_Fraud, Kaggle, synthetic)
        if raw_clean == "email":
            canonical_channel = "email"
            is_gateway = False
            return canonical_channel, is_gateway, False

        # 4. Instant Messaging / Chat (Synthetic generator)
        if raw_clean == "chat":
            canonical_channel = "chat"
            is_gateway = False
            return canonical_channel, is_gateway, False

        # 5. Mobile Push / System Notification (Synthetic generator)
        if raw_clean == "notification":
            canonical_channel = "notification"
            is_gateway = False
            return canonical_channel, is_gateway, False

        # 6. Fallback: If channel is already in canonical channels, retain
        if raw_clean in self.canonical_channels:
            return raw_clean, False, has_headers

        # 7. Unmapped / Ambiguous records: retain original without arbitrary guessing
        logger.warning(f"Unrecognized channel '{raw_channel}' from source '{source}'")
        return raw_clean, False, has_headers
