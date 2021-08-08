import requests

class YaUploader:

    def __init__(self, token: str):
        self.token = token
        headers = {
            'accept': 'application/json',
            'authorization': f'OAuth {token}'
        }
        API_BASE_URL = 'https://cloud-api.yandex.net:443'
        self.r = requests.get(API_BASE_URL + "/v1/disk/resources/upload", params={'path': 'rabbit/' + path_to_file},
                              headers=headers)

    def upload(self, file_path: str):
        self.r = requests.put(upload_url, files={'file': open(path_to_file, "rb")})
        return print(f'Файл {path_to_file} успешно загружен')



if __name__ == '__main__':
    path_to_file = "rabbit.jpg"
    token =
    uploader = YaUploader(token)
    upload_url = uploader.r.json()["href"]
    result = uploader.upload(path_to_file)
