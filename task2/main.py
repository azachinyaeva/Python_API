import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        headers = {'Authorization': self.token}
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        files = {"file": open(file_path, "rb")}
        params = {"path": files}
        r = requests.get(url=url, headers=headers, params=params)
        href = r.json()["href"]
        res = requests.put(href, files=files)
        res.raise_for_status()
        if res.status_code == 201:
            print(f'Файл "{file_path}" загружен')


if __name__ == '__main__':
    path_to_file = 'test.txt'
    token = 'y0_AgAAAAAMVvprAADLWwAAAADnkJ5BRfbm6N80TiW6fP7mW4ofqweKWQI'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
