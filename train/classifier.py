from tensorflow.keras.models import load_model
import numpy as np

model = load_model('/home/luiz/Desktop/Aline/model.h1')

labels = open('/home/luiz/Desktop/Aline/labels.txt','r',encoding='utf-8').read().split('\n')

labels2idx  = {}
idx2label = {}

for k,label in enumerate(labels):
    labels2idx[label] = k
    idx2label[k] = label

# classificar texto em uma entidade
def classify(text) :

    x = np.zeros((1,21,256),dtype ='float32')

    for k,ch in enumerate(bytes(text.encode('utf-8'))):
        x[0,k,int(ch)] = 1.0

    out = model.predict(x)
    idx = out.argmax()
    return idx2label[idx]
