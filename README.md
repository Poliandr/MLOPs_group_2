# MLOPs_group_2

[link to the dataset on Kaggle](https://www.kaggle.com/datasets/poojakeer/e-commerce-dataset)

[link to the directory on Google Drive for dvc](https://drive.google.com/drive/folders/18aBRTpFRJMBK-ngecXdbx91aPD2f0Emg?usp=sharing), for dvc remote repository take only ID_FOLDER=18aBRTpFRJMBK-ngecXdbx91aPD2f0Emg

to run docker:
sh '''
docker run -d --rm --name jen -v jenkins:/var/jenkins_home/data -p 80:8080 -p 88:8888 -p 50000:50000 jenkins:v1
'''