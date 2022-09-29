import yaml

data = yaml.safe_load(open('/home/luiz/Desktop/Aline/train/train.yml',
                       encoding='utf-8').read())

for command in data['commands']:
    print(command)