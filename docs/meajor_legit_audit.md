# MeAJOR Legitimate Email Audit

## Release inspection

- Official release: `meajor_cleaned_preprocessed.csv`
- Zenodo record: https://zenodo.org/records/18471483
- Published schema fields inspected: sender metadata, subject, body, language, source, label, and extracted email features.
- Label definition: `0 = benign`, `1 = phishing`.
- Release size stated by the dataset card: 108,685 samples.
- License: CC BY 4.0.
- Anonymization: entity removal tokens such as `[NAME]`, `[ORGANIZATION]`, `[EMAIL_ADDRESS]`, `[URL]`, and `[FINANCIAL_INFO]`.

## Extraction counts

- Total source labels: {'0.0': 60650, '1.0': 48034, '': 1}
- Source language values: {'en': 82175, 'unk': 1, 'ja': 602, 'en;en': 21250, 'zh': 315, 'fr': 303, 'es': 332, 'pl': 114, 'ru': 827, 'de': 383, 'zh;zh': 26, 'sl': 70, 'fa': 48, 'eo': 20, 'fi': 60, 'cy': 12, 'cs': 38, 'ca': 9, 'ru;ru': 26, 'ur': 10, 'it': 50, 'hu': 17, 'ar': 38, 'da': 17, 'az': 6, 'af': 9, 'es;es': 22, 'uk': 91, 'ceb': 7, 'nl': 57, 'eu': 10, 'en;zh': 37, 'bn': 3, 'br': 1, 'sco': 1, 'th': 22, 'en;ja': 47, 'ug': 1, 'zh;en': 12, 'id': 11, 'sw': 3, 'de;de': 77, 'pt': 85, 'sv': 18, 'sd': 1, 'wa': 2, 'zh;ja': 8, 'tl': 1, 'ja;en': 4, 'ml': 4, 'lv': 8, 'es;en': 11, 'en;be': 1, 'pl;pl': 7, 'fr;en': 12, 'tr': 14, 'ms;en': 2, 'sr': 13, 'hr': 14, 'lt': 7, 'it;en': 7, 'en;en;en': 218, 'gl': 2, 'vi': 2, 'no': 8, 'sk': 5, 'et': 18, 'war': 2, 'en;sr': 1, 'en;nl': 3, 'tl;hr': 1, 'de;en': 101, 'en;de': 31, 'am;en': 1, 'en;fr': 32, 'en;it': 5, 'en;pl': 4, 'id;en': 2, 'en;es': 50, 'it;de': 1, 'eo;en': 3, 'pt;it': 1, 'en;jbo': 1, 'zh;ru': 30, 'et;en': 2, 'cy;de': 1, 'en;ro': 1, 'ms;it': 1, 'es;sv': 1, 'fr;fr': 13, 'bs': 1, 'as': 1, 'en;en;en;en': 42, 'en;en;en;en;en': 13, 'ko': 6, 'hsb': 1, 'pt;pt': 58, 'en;en;en;en;en;en;en;en;en': 10, 'en;en;en;en;en;en': 24, 'pt;en': 2, 'it;es': 1, 'sl;fr': 1, 'pl;en': 2, 'ceb;es': 1, 'en;tl': 1, 'la;en': 2, 'ia;ca': 1, 'en;sh': 1, 'en;fi': 7, 'en;eo': 2, 'uz': 4, 'nn': 1, 'ro;de': 1, 'kn': 4, 'he': 4, 'el;el': 5, 'kw': 2, 'en;en;en;en;en;en;en': 11, 'en;en;en;en;en;en;en;en;en;en': 2, 'en;en;en;en;en;en;en;en': 8, 'ga': 1, 'en;en;en;en;en;en;fr;en;ja;en': 1, 'en;en;en;en;en;pt;en;en': 1, 'ro': 9, 'mn': 1, 'fr;en;en': 1, 'en;en;en;en;nl;en;en;en;en;en;en': 1, 'en;pt': 6, 'en;tr': 2, 'en;sv': 1, 'tl;en': 1, 'hu;sh': 1, 'nl;en': 2, 'no;es': 1, 'de;es': 1, 'es;it': 1, 'en;lt': 3, 'no;de': 1, 'io;en': 1, 'en;en;ja;en;en': 1, 'en;en;en;en;en;sr;en': 1, 'en;en;en;en;sr;en': 1, 'th;th': 1, 'sh': 4, 'jbo': 2, 'en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;cs;en;en': 1, 'fy': 1, 'en;en;en;en;en;en;en;en;en;en;en;en': 2, 'en;en;en;en;es;en': 1, 'uk;uk': 2, 'en;en;en;en;de;en;en;en;en': 1, 'en;en;en;en;en;en;en;en;en;fr;en;en': 1, 'en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en': 1, 'es;de': 1, 'tr;en': 284, 'da;fr': 1, 'hi': 4, 'ms': 4, 'en;en;en;en;ja;en': 1, 'sv;en;en': 1, 'ja;ja': 14, 'so': 1, 'lb': 1, 'en;ru': 29, 'sq': 1, 'gd': 1, 'en;fy': 1, 'en;br': 1, 'en;hu': 1, 'uk;en': 1, 'en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en': 1, 'als': 1, 'azb': 1, 'mg': 1, 'en;th': 4, 'km': 1, 'la;la': 2, 'zh;de': 2, 'it;it': 22, 'en;en;en;en;en;en;en;de;en;en;en;en;en;en;en;en;en;en': 1, 'ru;th': 1, 'en;en;en;en;en;en;en;en;en;en;en;en;en;en': 1, 'lo': 1, 'en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;en;pt;en;en;en;en': 1, '': 1, 'en;he': 4, 'uk;ru': 17, 'sr;en': 2, 'it;he': 1, 'fr;ru': 1, 'it;pt': 1, 'it;ru': 1, 'ilo': 1, 'ru;en': 2, 'sv;sv': 2, 'ro;ro': 8, 'sh;sh': 1, 'tr;bg': 1, 'hr;hr': 1, 'ceb;ceb': 1, 'tr;tr': 1, 'el': 1, 'ar;ar': 1, 'nn;en': 1, 'sl;sl': 1, 'pa': 1, 'ur;fi': 1, 'ca;en': 2, 'nl;nl': 1, 'cs;az': 1, 'en;en;sr': 1, 'fi;fi': 3, 'jbo;hu': 1, 'es;en;en': 1, 'sv;en': 8, 'oc': 1, 'ko;ko': 1, 'en;en;de': 2, 'en;de;en': 3, 'zh;es': 1, 'is': 2, 'no;no': 1, 'kk': 1, 'jv': 1, 'la': 1, 'mk': 1, 'eu;en': 1, 'sl;en': 1, 'ar;en': 1, 'da;en': 1, 'vi;en': 1, 'en;es;es;nl': 1, 'pl;en;en': 1, 'eu;de': 1, 'te;en': 1, 'en;lv': 1, 'sw;en': 1, 'de;en;en': 1, 'fi;sl': 1, 'de;fi': 1, 'kw;de': 1, 'wuu;wuu': 1, 'sv;nl': 1, 'lt;zh': 1}
- Benign records inspected: **0**
- English/unspecified usable candidates: **58621**
- Empty benign records excluded: **0**
- Malformed benign records excluded: **0**
- Internal exact duplicates removed: **2539**
- Exact duplicates against existing `real_fin_legit.csv`: **0**
- Candidate records written: **53543**
- Candidate financial_legitimate: **17179**
- Candidate general_legitimate: **36364**
- Ambiguous records held out for review: **0**

## Email length distribution for candidate records

### Words

{'count': 53543, 'min': 1, 'max': 968, 'mean': 172.67, 'median': 127, 'p90': 384, 'p95': 498}

### Characters

{'count': 53543, 'min': 4, 'max': 31136, 'mean': 1160.84, 'median': 837, 'p90': 2613, 'p95': 3406}

## Source composition

- `MeAJOR (trec5)`: 25714
- `MeAJOR (trec6)`: 10383
- `MeAJOR (trec7)`: 17446

## Duplicate comparison

- Exact duplicate candidate texts after filtering: 0.
- Candidate-to-existing exact duplicates removed: **0**.
- Candidate-to-existing near-duplicate matches at approximately 98% similarity: **0**.
- Near-duplicate candidates were retained unless exact duplicates; no source text was silently rewritten.

## Suitability decision

The candidate passes as a longer legitimate-email control corpus because the official release defines benign labels, preserves subject/body fields, documents its public-source composition, anonymizes entities, and provides a CC BY 4.0 license. It is not a pure financial dataset: ordinary business and personal/workplace email is categorized as `general_legitimate`, while financial/account-related wording is categorized as `financial_legitimate`.

## Limitations and review items

1. Benign means non-phishing under MeAJOR's annotation, not authenticated sender identity.
2. Source composition includes Enron and other legacy public corpora; some messages are business emails rather than consumer bank notifications.
3. Email bodies can contain extracted URLs and anonymization tokens; original text was preserved as requested.
4. The financial/general classification is rule-based and should be manually sampled.
5. The merged file is a new expanded corpus; the original `real_fin_legit.csv` remains unchanged.
