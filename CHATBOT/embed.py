# -*- coding: utf-8 -*-
"""embed.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17wweXoLilhZa3wfHhXj2K_06dSNtV8CJ
"""

import pandas as pd
import pickle
import torch
from sentence_transformers import SentenceTransformer

def embed_data(csv_path='scraped_output/scraped_data_iitk.csv', pickle_path='embedded_data.pkl'):
    df = pd.read_csv(csv_path)
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(df['text'].tolist(), show_progress_bar=True)
    df['embedding'] = embeddings.tolist()
    with open(pickle_path, 'wb') as f:
        pickle.dump((df, embeddings), f)
    return df, torch.tensor(embeddings), model