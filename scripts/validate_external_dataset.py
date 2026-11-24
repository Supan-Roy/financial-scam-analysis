import pandas as pd
from pathlib import Path

def validate():
    data_dir = Path('data/external_evaluation')
    audit_path = data_dir / 'external_scam_annotation_audit.csv'
    excl_path = data_dir / 'external_scam_exclusion_log.csv'
    curated_path = data_dir / 'external_fin_scam_curated.csv'
    expanded_path = data_dir / 'expanded_binary_external_test.csv'
    balanced_path = data_dir / 'balanced_binary_external_test.csv'
    test_path = Path('data/splits/test.csv')

    print("Running external evaluation dataset validation...")
    audit_df = pd.read_csv(audit_path)
    excl_df = pd.read_csv(excl_path)
    curated_df = pd.read_csv(curated_path)
    expanded_df = pd.read_csv(expanded_path)
    balanced_df = pd.read_csv(balanced_path)
    test_df = pd.read_csv(test_path)

    assert len(audit_df) == 12776
    assert (audit_df['inclusion_status'] == 'included').sum() == 792
    assert (audit_df['inclusion_status'] == 'excluded').sum() == 11984
    assert len(excl_df) == 11984
    assert len(curated_df) == 792
    assert len(expanded_df) == 7025
    assert len(balanced_df) == 1584

    assert curated_df['record_id'].nunique() == 792
    assert expanded_df['record_id'].nunique() == 7025
    assert balanced_df['record_id'].nunique() == 1584

    # Legitimate preservation
    test_legit = test_df[test_df['label'] == 0].reset_index(drop=True)
    exp_legit = expanded_df[expanded_df['label'] == 0].reset_index(drop=True)
    assert len(test_legit) == 6233
    assert (exp_legit['record_id'] == test_legit['record_id']).all()
    assert (exp_legit['original_text'] == test_legit['original_text']).all()
    assert (exp_legit['normalized_text'] == test_legit['normalized_text']).all()

    # Excluded records check
    excluded_ids = {'EXT-SCAM-00224', 'EXT-SCAM-00449', 'EXT-SCAM-00450', 'EXT-SCAM-00485', 'EXT-SCAM-00106'}
    for eid in excluded_ids:
        assert eid not in set(curated_df['record_id'])
        assert eid not in set(expanded_df['record_id'])
        assert eid not in set(balanced_df['record_id'])

    print("All validation assertions passed successfully!")

if __name__ == '__main__':
    validate()
