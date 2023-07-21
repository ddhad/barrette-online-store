import os
import googleapiclient.http
import io

from google.oauth2 import service_account
from googleapiclient.discovery import build


CREDENTIALS = 'creds.json'
FOLDER_ID = '1UqoOLVbQma7fAreyzZvbr_hSakFN5OMs'
TARGET_DIR = 'data'


def authenticate_drive():
    creds = service_account.Credentials.from_service_account_file(
        CREDENTIALS,
        scopes=['https://www.googleapis.com/auth/drive']
    )
    return build('drive', 'v3', credentials=creds)


def download_file(service, file_id, output_dir):
    file = service.files().get(fileId=file_id).execute()
    file_name = file['name']

    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(os.path.join(output_dir, file_name), 'wb')
    downloader = googleapiclient.http.MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f"Downloading {file_name}: {status.progress() * 100:.1f}%")


def download_folder_files(service, folder_id, output_dir):
    results = service.files().list(
        q=f"'{folder_id}' in parents and trashed=false",
        fields="files(id, name, mimeType)"
    ).execute()

    for item in results['files']:
        file_id = item['id']
        mime_type = item.get('mimeType', '')

        if mime_type == 'application/vnd.google-apps.folder':
            folder_name = item['name']
            new_output_dir = os.path.join(output_dir, folder_name)
            if not os.path.exists(new_output_dir):
                os.makedirs(new_output_dir)
            download_folder_files(service, file_id, new_output_dir)
        else:
            download_file(service, file_id, output_dir)


if __name__ == "__main__":
    if os.path.exists(TARGET_DIR):
        os.remove(TARGET_DIR)
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

    drive_service = authenticate_drive()
    download_folder_files(drive_service, FOLDER_ID, TARGET_DIR)
    print("Success")
