ResNet Model: 

ResNet50_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224,224,3), classes=10) 
resnet50_x = Flatten()(ResNet50_model.output) 
resnet50_x = Dense(256,activation='relu')(resnet50_x) 
resnet50_x = Dense(10,activation='softmax')(resnet50_x) 
resnet50_x_final_model.compile(loss = 'categorical_crossentropy', optimizer= SGD, metrics=['acc']) 


Plotting Confusion Matrix , Accuracy and Loss Graph: 


plt.xlabel('Predictions', fontsize=18) 
plt.ylabel('Actuals', fontsize=18) 
plt.title('Confusion Matrix', fontsize=18) 
plt.savefig("results/confusionmatrix1.png") 
plt.show() 
plt.plot(resnet50_history.history['loss'], color='b', label="Training loss") 
plt.plot(resnet50_history.history['val_loss'], color='r', label="validation loss") 
plt.title("Training and Validation Loss") 
plt.xlabel("Epoch #") 
plt.ylabel("Loss") 
plt.legend(loc="upper left") 
plt.savefig("results/resnet_loss1.png") 
plt.show() 
plt.plot(resnet50_history.history['acc'], color='b', label="Training accuracy") 
plt.plot(resnet50_history.history['val_acc'], color='r',label="Validation accuracy") 
plt.title("Training and Validation Accuracy") 
plt.xlabel("Epoch #") 
plt.ylabel("Accuracy") 
plt.legend(loc="lower left") 
plt.savefig("results/resnet_accuracy1.png") 
plt.show() 
