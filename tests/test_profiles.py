import cylab.core.profiles as profiles_mod


def _patch_dirs(tmp_path, monkeypatch):
    fake_dir = tmp_path / "profiles"
    fake_active = tmp_path / "active_profile"
    monkeypatch.setattr(profiles_mod, "PROFILES_DIR", fake_dir)
    monkeypatch.setattr(profiles_mod, "ACTIVE_PROFILE_FILE", fake_active)


def test_list_profiles_empty(tmp_path, monkeypatch):
    _patch_dirs(tmp_path, monkeypatch)
    assert profiles_mod.list_profiles() == []


def test_create_and_list_profile(tmp_path, monkeypatch):
    _patch_dirs(tmp_path, monkeypatch)
    created = profiles_mod.create_profile("ctf", "CTF profile")
    assert created is True
    assert "ctf" in profiles_mod.list_profiles()


def test_create_duplicate_profile_fails(tmp_path, monkeypatch):
    _patch_dirs(tmp_path, monkeypatch)
    profiles_mod.create_profile("ctf")
    second = profiles_mod.create_profile("ctf")
    assert second is False


def test_set_and_get_active_profile(tmp_path, monkeypatch):
    _patch_dirs(tmp_path, monkeypatch)
    profiles_mod.create_profile("red-team")
    ok = profiles_mod.set_active_profile("red-team")
    assert ok is True
    assert profiles_mod.get_active_profile() == "red-team"


def test_use_nonexistent_profile_fails(tmp_path, monkeypatch):
    _patch_dirs(tmp_path, monkeypatch)
    ok = profiles_mod.set_active_profile("does-not-exist")
    assert ok is False
