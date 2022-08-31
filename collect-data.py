from multiprocessing.pool import Pool
import requests
import json
import os


base_url = 'http://api.guildwars2.com'
api_v2_url = '{}/v2'.format(base_url)
num_of_processes = 32

def main():
    resources = [
        'traits',
    ]

    for resource in resources:
        save_resource_from_api(resource)

def save_resource_from_api(resource):
    resource_url = '{}/{}'.format(api_v2_url, resource)
    resource_response = requests.get(resource_url)
    item_ids = resource_response.json()

    params = list(zip([resource] * len(item_ids), item_ids))

    p = Pool(num_of_processes)
    p.map(save_item_from_api, params)

def save_item_from_api(param):
    resource = param[0]
    item_id = param[1]
    item_url = '{}/{}/{}'.format(api_v2_url, resource, item_id)
    item_response = requests.get(item_url)
    item_json = item_response.json()
    save_item_with_id_by_resource(resource, item_json, item_id)

def create_dir(dir_name):
    try:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
    except OSError:
        print('[Error] Create directory : {}'.format(dir_name))

def save_json(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)

def save_item_with_id_by_resource(resource, item, id):
    dir_name = './data/{}'.format(resource)
    file_name = '{}/{}.json'.format(dir_name, id)
    create_dir(dir_name)
    save_json(file_name, item)
    print('[Info] Saved : {}'.format(file_name))


if __name__ == '__main__':
    main()
