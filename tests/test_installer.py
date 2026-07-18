import cylab.core.installer as installer_mod


def test_is_installed_true_when_which_finds_it(monkeypatch):
    monkeypatch.setattr(
        installer_mod.shutil, "which", lambda name: "/usr/bin/docker"
    )
    assert installer_mod.is_installed("docker") is True


def test_is_installed_false_when_not_found(monkeypatch):
    monkeypatch.setattr(installer_mod.shutil, "which", lambda name: None)
    assert installer_mod.is_installed("docker") is False


def test_is_installed_unknown_package_returns_false():
    assert installer_mod.is_installed("not-a-real-tool") is False


def test_install_skips_if_already_installed(monkeypatch, capsys):
    monkeypatch.setattr(
        installer_mod, "is_installed", lambda name: True
    )
    result = installer_mod.install("docker")
    captured = capsys.readouterr()

    assert result is True
    assert "already installed" in captured.out


def test_install_cancelled_when_user_declines(monkeypatch):
    monkeypatch.setattr(installer_mod, "is_installed", lambda name: False)
    monkeypatch.setattr("builtins.input", lambda prompt: "n")

    result = installer_mod.install("docker")

    assert result is False


def test_install_unknown_package_returns_false(capsys):
    result = installer_mod.install("not-a-real-tool")
    captured = capsys.readouterr()

    assert result is False
    assert "Unknown package" in captured.out
