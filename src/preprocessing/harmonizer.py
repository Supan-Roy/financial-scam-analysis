"""
Harmonization and Normalization Module for Financial Scam Preprocessing.

This module provides deterministic, idempotent placeholder harmonization,
collapsing malformed/nested bracket artifacts and standardizing anonymized
entities across disparate research corpora into a canonical ontology.
"""

import re
import logging
from typing import Dict, List, Tuple, Set, Optional, Any

logger = logging.getLogger(__name__)

# Canonical ontology mapping dictionary
# Maps raw angle/square bracket placeholders to canonical tokens.
CANONICAL_PLACEHOLDER_MAPPINGS: Dict[str, str] = {
    # 1. URL & Links
    "<URL>": "[URL]",
    "[URL]": "[URL]",
    "<url>": "[URL]",
    "[url]": "[URL]",
    "[LINK REDACTED]": "[URL]",

    # 2. Phone Numbers & Telephony
    "<PHONE>": "[PHONE_NUMBER]",
    "<PHONE_NUMBER>": "[PHONE_NUMBER]",
    "[PHONE_NUMBER]": "[PHONE_NUMBER]",
    "[PHONE]": "[PHONE_NUMBER]",
    "[FAX_NUMBER]": "[PHONE_NUMBER]",

    # 3. Email Addresses
    "<EMAIL>": "[EMAIL_ADDRESS]",
    "<EMAIL_ADDRESS>": "[EMAIL_ADDRESS]",
    "[EMAIL_ADDRESS]": "[EMAIL_ADDRESS]",
    "[EMAIL]": "[EMAIL_ADDRESS]",

    # 4. Person Names & Identities
    "<NAMED_ENTITY>": "[PERSON_NAME]",
    "[NAME]": "[PERSON_NAME]",
    "[Name]": "[PERSON_NAME]",
    "<name>": "[PERSON_NAME]",
    "[USERNAME]": "[PERSON_NAME]",
    "[INITIALS]": "[PERSON_NAME]",
    "[Fictional Contact]": "[PERSON_NAME]",
    "[You]": "[PERSON_NAME]",

    # 5. Organizations & Services
    "<NRP>": "[ORGANIZATION]",
    "[ORGANIZATION]": "[ORGANIZATION]",
    "[FICTIONAL ORGANIZATION]": "[ORGANIZATION]",
    "[FICTITIOUS SERVICE DESK]": "[ORGANIZATION]",
    "[FICTIONAL SERVICE]": "[ORGANIZATION]",

    # 6. Financial Information & Data
    "<US_BANK_NUMBER>": "[FINANCIAL_DATA]",
    "[FINANCIAL_INFO]": "[FINANCIAL_DATA]",
    "[AMOUNT REDACTED]": "[FINANCIAL_DATA]",
    "[ACCOUNT_NUMBER]": "[FINANCIAL_DATA]",
    "<CREDIT_CARD>": "[FINANCIAL_DATA]",

    # 7. Identifiers (Case Numbers, Government IDs, Licenses)
    "<US_DRIVER_LICENSE>": "[IDENTIFIER]",
    "<US_SSN>": "[IDENTIFIER]",
    "<US_PASSPORT>": "[IDENTIFIER]",
    "<UK_NHS>": "[IDENTIFIER]",
    "<MEDICAL_LICENSE>": "[IDENTIFIER]",
    "[REFERENCE_NUMBER]": "[IDENTIFIER]",
    "[CASE REDACTED]": "[IDENTIFIER]",

    # 8. Date & Time
    "<DATE_TIME>": "[DATE_TIME]",
    "[DATE]": "[DATE_TIME]",
    "[date]": "[DATE_TIME]",
    "[TIME]": "[DATE_TIME]",

    # 9. Physical Locations & Addresses
    "<LOCATION>": "[LOCATION]",
    "[ADDRESS]": "[LOCATION]",

    # 10. System & Markup Artifacts
    "<IP_ADDRESS>": "[SYSTEM_ARTIFACT]",
    "[IP_ADDRESS]": "[SYSTEM_ARTIFACT]",
    "[FILE_NAME]": "[SYSTEM_ARTIFACT]",
    "[FILE_PATH]": "[SYSTEM_ARTIFACT]",
    "[PASSWORD]": "[SYSTEM_ARTIFACT]",
    "[SYMBOL]": "[SYSTEM_ARTIFACT]",
    "[VERSION]": "[SYSTEM_ARTIFACT]",
    "[alternative HTML version deleted]": "[SYSTEM_ARTIFACT]",

    # Preserved Domain Entities (MeAJOR product entity retained to preserve domain distinction)
    "[PRODUCT]": "[PRODUCT]",
}

# 10 Standard Canonical Tokens + Preserved Domain Entity
CANONICAL_TOKENS: Set[str] = {
    "[URL]",
    "[PHONE_NUMBER]",
    "[EMAIL_ADDRESS]",
    "[PERSON_NAME]",
    "[ORGANIZATION]",
    "[FINANCIAL_DATA]",
    "[IDENTIFIER]",
    "[DATE_TIME]",
    "[LOCATION]",
    "[SYSTEM_ARTIFACT]",
    "[PRODUCT]",
}


class PlaceholderHarmonizer:
    """
    Deterministic, idempotent placeholder normalization engine.
    """

    def __init__(self, mapping: Optional[Dict[str, str]] = None):
        self.mapping = mapping if mapping is not None else CANONICAL_PLACEHOLDER_MAPPINGS
        # Sort keys by length descending to prevent shorter prefix substrings matching first
        self._sorted_keys = sorted(self.mapping.keys(), key=len, reverse=True)

        # Precompiled regexes for bracket cleanup
        self._re_mixed_brackets = re.compile(
            r"<{2,}\s*(?:File:\s*)?\[([A-Za-z0-9_ -]+?)\]\s*>{2,}"
        )
        self._re_multi_square_open = re.compile(r"\[{2,}([A-Za-z0-9_ -]+?)\]+")
        self._re_multi_square_close = re.compile(r"\[+([A-Za-z0-9_ -]+?)\]{2,}")
        self._re_multi_angle_open = re.compile(r"<{2,}([A-Za-z0-9_ -]+?)>+")
        self._re_multi_angle_close = re.compile(r"<+([A-Za-z0-9_ -]+?)>{2,}")

        # General placeholder matcher
        self._re_placeholder = re.compile(r"<[A-Za-z0-9_ -]+>|\[[A-Za-z0-9_ -]+\]")

    def clean_nested_brackets(self, text: str) -> str:
        """
        Safely collapses redundant nested and malformed bracket artifacts without
        affecting natural text or performing arbitrary regex replacements.
        """
        if not isinstance(text, str) or not text:
            return "" if text is None else str(text)

        # 1. Peel mixed outer angle brackets enclosing square brackets, e.g. <<[FILE_NAME]>>
        text = self._re_mixed_brackets.sub(r"[\1]", text)

        # 2. Collapse repeated square brackets around tokens, e.g. [[[[[PRODUCT]]]]] -> [PRODUCT]
        text = self._re_multi_square_open.sub(r"[\1]", text)
        text = self._re_multi_square_close.sub(r"[\1]", text)

        # 3. Collapse repeated angle brackets around tokens, e.g. <<<URL>>> -> <URL>
        text = self._re_multi_angle_open.sub(r"<\1>", text)
        text = self._re_multi_angle_close.sub(r"<\1>", text)

        return text

    def normalize_text(self, text: str) -> str:
        """
        Deterministically normalizes placeholders in text to canonical tokens.
        Preserves unmapped/unknown bracketed tokens without arbitrary categorization.
        Is strictly idempotent: normalize_text(normalize_text(t)) == normalize_text(t).
        """
        if not isinstance(text, str) or not text:
            return "" if text is None else str(text)

        # First clean nested/malformed brackets
        text = self.clean_nested_brackets(text)

        # Replace known placeholders with canonical tokens
        for token in self._sorted_keys:
            target = self.mapping[token]
            if token in text:
                text = text.replace(token, target)

        return text

    def count_placeholders(self, text: str) -> int:
        """Counts occurrences of angle or square bracket tokens."""
        if not isinstance(text, str) or not text:
            return 0
        return len(self._re_placeholder.findall(text))

    def find_unresolved_placeholders(self, text: str) -> List[str]:
        """
        Returns list of bracketed tokens present in text that are not part of the
        canonical token ontology.
        """
        if not isinstance(text, str) or not text:
            return []
        matches = self._re_placeholder.findall(text)
        return [m for m in matches if m not in CANONICAL_TOKENS]

    @staticmethod
    def profile_text(text: str) -> Tuple[int, int]:
        """
        Returns (character_count, word_count).
        Word count is computed via whitespace tokenization.
        """
        if not isinstance(text, str) or not text:
            return 0, 0
        char_count = len(text)
        word_count = len(text.split())
        return char_count, word_count

