import yaml
from ordek.main import load_config

def test_load_config(tmpdir):
    # Create a sample config file
    sample_config = {
        'theme': 'default',
        'site_title': 'Test Blog',
        'author': 'Jane Doe'
    }
    config_file = tmpdir.join("config.yml")
    config_file.write(yaml.dump(sample_config))

    # Load the config
    config = load_config(str(config_file))

    # Assert the values are correct
    assert config['theme'] == 'default'
    assert config['site_title'] == 'Test Blog'
    assert config['author'] == 'Jane Doe'