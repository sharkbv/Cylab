import cylab.core.config as config_mod


def test_load_config_defaults_when_missing(tmp_path, monkeypatch):
    fake_file = tmp_path / "config.toml"
    monkeypatch.setattr(config_mod, "CONFIG_FILE", fake_file)

    result = config_mod.load_config()

    assert result["log_level"] == "INFO"
    assert result["default_profile"] == "default"


def test_save_then_load_config(tmp_path, monkeypatch):
    fake_dir = tmp_path / "cylab_config"
    fake_file = fake_dir / "config.toml"
    monkeypatch.setattr(config_mod, "CONFIG_DIR", fake_dir)
    monkeypatch.setattr(config_mod, "CONFIG_FILE", fake_file)

    config_mod.save_config({"log_level": "DEBUG", "default_profile": "test"})
    result = config_mod.load_config()

    assert result["log_level"] == "DEBUG"
    assert result["default_profile"] == "test"
