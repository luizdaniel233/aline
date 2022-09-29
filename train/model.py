from pickle import TRUE
from pickletools import optimize
import yaml
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM,Dense,Embedding
from tensorflow.keras.utils import to_categorical


data = yaml.safe_load(open('/home/luiz/Desktop/Aline/train/train.yml',
                       encoding='utf-8').read())

inputs,outputs = [],[]


for command in data['commands']:
    inputs.append(command['input'].lower())
    outputs.append('{}\{}'.format(command['entity'],command['action']))

max_seq = max([len(bytes(x.encode('utf-8'))) for x in inputs])

#criar dataset (numero de exemplos)
# one hot encoding
input_data = np.zeros((len(inputs),max_seq,256),dtype='float32')

for i,inp in enumerate(inputs):
    for k,ch in enumerate(bytes(inp.encode('utf-8'))):
        input_data[i,k,int(ch)] = 1.0

# input data sparse
# input_data = np.zeros((len(inputs),max_seq),dtype='int32')

# for i,input in enumerate(inputs):
#     for k,ch in enumerate(input):
#         input_data[i,k] = ch2idx[ch]

# Criar labels para o classificador

labels = set(outputs)

fwrite = open('/home/luiz/Documents/aline/labels.txt','w',encoding='utf-8')

labels2idx  = {}
idx2label = {}

for k,label in enumerate(labels):
    labels2idx[label] = k
    idx2label[k] = label
    fwrite.write(label + '\n')

fwrite.close()

output_data = []

for output in outputs:
    output_data.append(labels2idx[output])

output_data = to_categorical(output_data,len(output_data))


model = Sequential()
model.add(LSTM(128))
model.add(Dense(len(output_data),activation='softmax'))
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['acc'])

model.fit(input_data,output_data,epochs=200)

model.save('model.h1')


# classificar texto em uma entidade
def classify(text) :
    x = np.zeros((1,max_seq,256),dtype ='float32')

    for k,ch in enumerate(bytes(text.encode('utf-8'))):
        x[0,k,int(ch)] = 1.0

    out = model.predict(x)
    idx = out.argmax()
    print(idx2label[idx])




