import streamlit as st
import numpy as np
import pandas as pd
import lightfm as lf
import nmslib
import pickle
import scipy.sparse as sparse


def nearest_books_nms(book_id, index, n=10):
    """Р¤СѓРЅРєС†РёСЏ РґР»СЏ РїРѕРёСЃРєР° Р±Р»РёР¶Р°Р№С€РёС… СЃРѕСЃРµРґРµР№, РІРѕР·РІСЂР°С‰Р°РµС‚ РїРѕСЃС‚СЂРѕРµРЅРЅС‹Р№ РёРЅРґРµРєСЃ"""
    nn = index.knnQuery(item_embeddings[book_id], k=n)
    return nn


def get_names(index):
    """
    input - idx of books
    Р¤СѓРЅРєС†РёСЏ РґР»СЏ РІРѕР·РІСЂР°С‰РµРЅРёСЏ РёРјРµРЅРё РєРЅРёРі
    return - list of names
    """
    names = []
    for idx in index:
        names.append('Book name:  {} '.format(
            name_mapper[idx]) + '  Book Author: {}'.format(author_mapper[idx]))
    return names

def read_files(folder_name='data'):
    """
    Р¤СѓРЅРєС†РёСЏ РґР»СЏ С‡С‚РµРЅРёСЏ С„Р°Р№Р»РѕРІ + РїСЂРµРѕР±СЂР°Р·РѕРІР°РЅРёРµ Рє  РЅРёР¶РЅРµРјСѓ СЂРµРіРёСЃС‚СЂСѓ
    """
    ratings = pd.read_csv(folder_name+'/ratings.csv')
    books = pd.read_csv(folder_name+'/books.csv')
    books['title'] = books.title.str.lower()
    return ratings, books 

def make_mappers():
    """
    Р¤СѓРЅРєС†РёСЏ РґР»СЏ СЃРѕР·РґР°РЅРёСЏ РѕС‚РѕР±СЂР°Р¶РµРЅРёСЏ id РІ title
    """
    name_mapper = dict(zip(books.id, books.title))
    author_mapper = dict(zip(books.id, books.authors))

    return name_mapper, author_mapper 

def load_embeddings():
    """
    Р¤СѓРЅРєС†РёСЏ РґР»СЏ Р·Р°РіСЂСѓР·РєРё РІРµРєС‚РѕСЂРЅС‹С… РїСЂРµРґСЃС‚Р°РІР»РµРЅРёР№
    """
    with open('item_embeddings.pickle', 'rb') as f:
        item_embeddings = pickle.load(f)

    # РўСѓС‚ РјС‹ РёСЃРїРѕР»СЊР·СѓРµРј nmslib, С‡С‚РѕР±С‹ СЃРѕР·РґР°С‚СЊ РЅР°С€ Р±С‹СЃС‚СЂС‹Р№ knn
    nms_idx = nmslib.init(method='hnsw', space='cosinesimil')
    nms_idx.addDataPointBatch(item_embeddings)
    nms_idx.createIndex(print_progress=True)
    return item_embeddings,nms_idx

#Р—Р°РіСЂСѓР¶Р°РµРј РґР°РЅРЅС‹Рµ
ratings, books  = read_files(folder_name='data') 
name_mapper, author_mapper = make_mappers()
item_embeddings,nms_idx = load_embeddings()

#Р¤РѕСЂРјР° РґР»СЏ РІРІРѕРґР° С‚РµРєСЃС‚Р°
title = st.text_input('Book Name', '')
title = title.lower()

#РќР°С€ РїРѕРёСЃРє РїРѕ РєРЅРёРіР°Рј
output = books[books.title.str.contains(title) > 0]

#Р’С‹Р±РѕСЂ РєРЅРёРіРё РёР· СЃРїРёСЃРєР°
option = st.selectbox('Which book?', output['title'].values)

#Р’С‹РІРѕРґРёРј РєРЅРёРіСѓ
'You selected: ', option

#РС‰РµРј СЂРµРєРѕРјРµРЅРґР°С†РёРё
val_index = output[output['title'].values == option].id
index = nearest_books_nms(val_index, nms_idx, 5)

#Р’С‹РІРѕРґРёРј СЂРµРєРѕРјРµРЅРґР°С†РёРё Рє РЅРµР№
'Most simmilar books are: '
st.write('', get_names(index[0])[1:])

# Пошаговая инструкция по работе с Heroku 
# Инструкция по созданию дашборда Streamlit + Heroku (англ.)
# https://devcenter.heroku.com/articles/getting-started-with-python#set-up
# https://towardsdatascience.com/quickly-build-and-deploy-an-application-with-streamlit-988ca08c7e83