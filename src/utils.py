import kagglehub
import shutil
import os

download_path = kagglehub.dataset_download("tmdb/tmdb-movie-metadata")

target_folder = '../data/raw'

os.makedirs(target_folder, exist_ok=True)

for filename in os.listdir(download_path):
    source_file = os.path.join(download_path, filename)
    target_file = os.path.join(target_folder, filename)
    
    if os.path.isfile(source_file):
        shutil.copy(source_file, target_file)
        print(f"Copiado: {filename} -> {target_folder}")

print("\nDataset listo en data/raw!")