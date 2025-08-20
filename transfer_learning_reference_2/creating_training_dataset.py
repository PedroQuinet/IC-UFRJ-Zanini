# Para usar a função keras.utils.image_dataset_from_directory temos que ter uma pasta com as imagens em subpastas e cada subpasta com o nome da label

import pandas as pd
import os
import shutil

# Botar o path correto do arquivo CSV
df = pd.read_csv(r'C:\Users\pedro.quinet\Desktop\IC-UFRJ-Zanini\transfer_learning_reference_2\Training_set.csv')

os.makedirs(os.path.join(r'C:\Users\pedro.quinet\Desktop\IC-UFRJ-Zanini\transfer_learning_reference_2', 'treino'), exist_ok=True)

for idx, row in df.iterrows():
    label = str(row['label'])
    img_path = os.path.join(r"C:\Users\pedro.quinet\Desktop\IC-UFRJ-Zanini\transfer_learning_reference_2\train", row['filename'])
    label_folder = os.path.join('treino', label)
    os.makedirs(label_folder, exist_ok=True)
    # Copia a imagem para a pasta da label
    if os.path.isfile(img_path):
        shutil.copy(img_path, label_folder)
    