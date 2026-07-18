import cylab.core.reports as reports_mod


def test_build_report_counts_passed():
    checks = [
        {"name": "a", "passed": True, "hint": ""},
        {"name": "b", "passed": False, "hint": "fix b"},
    ]
    report = reports_mod.build_report(checks)
    assert report["passed"] == 1
    assert report["total"] == 2


def test_save_and_list_report(tmp_path, monkeypatch):
    fake_dir = tmp_path / "reports"
    monkeypatch.setattr(reports_mod, "REPORTS_DIR", fake_dir)
    checks = [{"name": "a", "passed": True, "hint": ""}]
    report = reports_mod.build_report(checks)
    path = reports_mod.save_report(report)
    assert path.exists()
    assert path in reports_mod.list_reports()
