from torch.utils.data import DataLoader, Dataset
import librosa
import numpy as np
import torch
import torch.nn as nn  # 신경망들이 포함됨

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu') #GPU 할당

"""

0   [원천]1.강제추행(성범죄)_1
1   [원천]2.강도범죄_1
2   [원천]3.절도범죄_1
3   [원천]4.폭력범죄_1
4   [원천]14.도움요청_1

"""

def predict_wav(file_name):
    checkpoint = torch.load('best_model_20000.pth')
    model = CNNclassification().to(device)
    model.load_state_dict(checkpoint)

    print("상황 추론")
    audio, sample_rate = librosa.load(file_name, sr=16000)
    data = set_len(audio)
    data = np.array(data)

    mfcc = preprocess_data(data)

    test_mfccs = mfcc.reshape(-1, mfcc.shape[1], mfcc.shape[2], 1)

    dataset = CustomDataset(X=test_mfccs, y=None, train_mode=False)
    test_loader = DataLoader(dataset, batch_size=10, shuffle=False)

    pred = predict(model, test_loader, device)
    #print(type(pred))

    if pred[0] == 0:
        print("강제추행(성범죄)")
    elif pred[0] == 1:
        print("강도범죄")
    elif pred[0] == 2:
        print("절도범죄")
    elif pred[0] == 3:
        print("폭력범죄")
    elif pred[0] == 4:
        print("도움요청")


def set_len(data):
    max = 20000
    result = []
    if len(data) < max:
        data = np.pad(data, (0, max - len(data)), 'constant', constant_values=0)
    elif len(data) > max:
        data = data[:max]

    result.append(data)

    return result

def preprocess_data(data):

    extracted_features = librosa.feature.mfcc(y=data, sr=16000, n_mfcc=40)
    mfccs = extracted_features

    return mfccs

def predict(model, test_loader, device):

    with torch.no_grad():
        for wav in iter(test_loader):
            wav = wav.to(device)
            pred_logit = model(wav)
            pred_logit = pred_logit.argmax(dim=1, keepdim=True).squeeze(1)
            model_pred = pred_logit.tolist()

    return model_pred


class CustomDataset(Dataset):
    def __init__(self, X, y, train_mode=True, transforms=None):  # 필요한 변수들을 선언
        self.X = X
        self.y = y
        self.train_mode = train_mode
        self.transforms = transforms

    def __getitem__(self, index):  # index번째 data를 return
        X = self.X[index]

        if self.transforms is not None:
            X = self.transforms(X)

        if self.train_mode:
            y = self.y[index]
            return X, y
        else:
            return X

    def __len__(self):  # 길이 return
        return len(self.X)



class CNNclassification(torch.nn.Module):
    def __init__(self):
        super(CNNclassification, self).__init__()
        self.layer1 = torch.nn.Sequential(
            nn.Conv2d(40, 10, kernel_size=2, stride=1, padding=1),  # cnn layer
            nn.ReLU(),  # activation function
            nn.MaxPool2d(kernel_size=2, stride=2))  # pooling layer

        self.layer2 = torch.nn.Sequential(
            nn.Conv2d(10, 100, kernel_size=2, stride=1, padding=1),  # cnn layer
            nn.ReLU(),  # activation function
            nn.MaxPool2d(kernel_size=2, stride=2))  # pooling layer

        self.layer3 = torch.nn.Sequential(
            nn.Conv2d(100, 200, kernel_size=2, stride=1, padding=1),  # cnn layer
            nn.ReLU(),  # activation function
            nn.MaxPool2d(kernel_size=2, stride=2))  # pooling layer

        self.layer4 = torch.nn.Sequential(
            nn.Conv2d(200, 300, kernel_size=2, stride=1, padding=1),  # cnn layer
            nn.ReLU(),  # activation function
            nn.MaxPool2d(kernel_size=2, stride=2))  # pooling layer

        self.fc_layer = nn.Sequential(
            nn.Linear(900, 10)  # fully connected layer(ouput layer)
        )

    def forward(self, x):
        x = self.layer1(x)  # 1층

        x = self.layer2(x)  # 2층

        x = self.layer3(x)  # 3층

        x = self.layer4(x)  # 4층

        x = torch.flatten(x, start_dim=1)  # N차원 배열 -> 1차원 배열

        out = self.fc_layer(x)
        return out
