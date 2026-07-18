from cylab.core.doctor_checks import run_checks


def test_run_checks_returns_five_checks():
    checks = run_checks()
    assert len(checks) == 5


def test_each_check_has_required_keys():
    checks = run_checks()
    for c in checks:
        assert "name" in c
        assert "passed" in c
        assert "hint" in c
        assert isinstance(c["passed"], bool)


def test_python_check_passes_on_current_interpreter():
    checks = run_checks()
    python_check = checks[0]
    assert python_check["passed"] is True
