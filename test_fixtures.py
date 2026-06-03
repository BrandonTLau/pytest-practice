import pytest

@pytest.fixture
def bug_reports():
    return [
        {"id": 1, "title": "Login button not working", "severity": "high", "status": "open"},
        {"id": 2, "title": "Profile picture not loading", "severity": "low", "status": "closed"},
        {"id": 3, "title": "Checkout page crashes", "severity": "high", "status": "open"},
    ]

def test_bug_count(bug_reports):
    # assert there are 3 bug reports
    assert len(bug_reports) == 3

def test_first_bug_id(bug_reports):
    # assert first bug has id 1
    assert bug_reports[0]["id"] == 1

def test_high_severity_bugs(bug_reports):
    # assert correct count of high severity bugs
    count = 0
    for bug in bug_reports:
        if bug["severity"] == "high":
            count += 1
    assert count == 2