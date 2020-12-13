import os
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_: str):
        """Метод загруджает файл file_ на яндекс диск"""
        HEADERS = {"Authorization": f"OAuth {self.token}"}
        response = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload",
                                params={"path": f'/Education/netology/{file_}', "overwrite": "true"},
                                headers=HEADERS,
                                )
        requests.put(response.json()['href'], files={'file': open(file_, 'rb')})
        return f'Файл <{file_}> успешно загружен на Яндекс.Диск'


if __name__ == '__main__':
    # Input abs file path, like: C:\Temp\file_to_upload.jpg
    file_path = os.path.basename(input('Введите путь к файлу вместе с именем файла:\n'))
    # There is your Yandex.disk Token
    uploader = YaUploader("Yandex.disk Token")
    result = uploader.upload(file_path)
    print(result)
