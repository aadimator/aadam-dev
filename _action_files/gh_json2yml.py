import sys
import json
import yaml

def convert_json_to_yaml(json_path, yaml_path):
    with open(json_path, 'r') as json_file:
        json_data = json.load(json_file)
    
    output_data = []

    for node in json_data['data']['user']['pinnedItems']['edges']:
        node['node']['stargazers'] = node['node']['stargazers']['totalCount']
        output_data.append(node['node'])

    with open(yaml_path, 'w') as yaml_file:
        yaml.safe_dump(output_data, yaml_file, default_flow_style=False)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python json_to_yaml.py <json_file_path>')
        sys.exit(1)
    
    json_file_path = sys.argv[1]
    yaml_file_path = json_file_path.replace('.json', '.yaml')
    
    convert_json_to_yaml(json_file_path, yaml_file_path)
    print(f'Successfully converted {json_file_path} to {yaml_file_path}.')
