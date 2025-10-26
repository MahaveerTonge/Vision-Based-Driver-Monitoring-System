Dataset Details: 
print("train data class name",data_train['ClassName'].value_counts()) 
print(data_train.describe()) 
labels_id = {label_name:id for id,label_name in enumerate(labels_list)} 
print("labels_id",labels_id) 

Preprocessing: 
def path_to_tensor(img_path): 
img = image.load_img(img_path, target_size=(224, 224)) 
x = image.img_to_array(img) 
return np.expand_dims(x, axis=0) 
def paths_to_tensor(img_paths): 
list_of_tensors = [path_to_tensor(img_path) for img_path in tqdm(img_paths)] 
return np.vstack(list_of_tensors) 
train_generator = train_datagen.flow_from_directory(train_data_dir,batch_size=32,shuffle=True,target_size=(224, 224)) 
train_tensors = paths_to_tensor(xtrain).astype('float32')/255 - 0.5 
valid_tensors = paths_to_tensor(xtest).astype('float32')/255 - 0.5
xtrain,xtest,ytrain,ytest = train_test_split(data_train.iloc[:,0],labels,test_size = 0.2,random_state=42) 
