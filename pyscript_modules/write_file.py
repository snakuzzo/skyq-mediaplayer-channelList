import yaml

def write_yaml(filename, content):
    with open(filename, 'w') as file:
        yaml.dump(content, file, sort_keys=False)
