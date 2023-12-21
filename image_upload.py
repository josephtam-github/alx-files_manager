import base64
import requests
import sys

def encode_file_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def post_image_to_server(file_path, token, parent_id):
    file_name = file_path.split('/')[-1]
    file_encoded = encode_file_to_base64(file_path)

    r_json = {
        'name': file_name,
        'type': 'image',
        'isPublic': True,
        'data': file_encoded,
        'parentId': parent_id
    }

    r_headers = {'X-Token': token}

    r = requests.post("http://0.0.0.0:5000/files", json=r_json, headers=r_headers)
    print(r.json())

if __name__ == "__main__":
    file_path = sys.argv[1]
    token = sys.argv[2]
    parent_id = sys.argv[3]

    post_image_to_server(file_path, token, parent_id)
