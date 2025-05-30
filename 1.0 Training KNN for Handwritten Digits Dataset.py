from sklearn.datasets import load_digits
#load_digits is the function used to load the digits dataset from sklearn module
dataset=load_digits()




data=dataset.data
target=dataset.target
images=dataset.images


import cv2

ret,data=cv2.threshold(data,7,15,cv2.THRESH_BINARY)
ret,images=cv2.threshold(images,7,15,cv2.THRESH_BINARY)


from sklearn.model_selection import train_test_split

train_data,test_data,train_target,test_target=train_test_split(data,target,test_size=0.1)

from sklearn.neighbors import KNeighborsClassifier

model=KNeighborsClassifier()
model.fit(train_data,train_target)


predicted_target=model.predict(test_data)

from sklearn.metrics import accuracy_score

acc=accuracy_score(test_target,predicted_target)

print('accuracy:',acc)


import joblib

joblib.dump(model,'KNN-Handwritten-Written-Digits.sav')


# In[ ]:




