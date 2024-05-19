# MLOPs_group_2

<br />

Repository of team №2 as final project for MLOps.

<br />

## Members of team: 

Aleksei Izmalkin
<br />
Denis Melnikov
<br />
Danila Moiseev
<br />
Alexander Duplin
<br />
Ivan Kazarin
<br />
Semen Kaunov

<br />

**Logistic regression** is used in this model. 
The predicted parameter reflects information about whether the ordered goods will be delivered to the customer **on time or not**.

----------------

<br />

[Link to the dataset on Kaggle](https://www.kaggle.com/datasets/poojakeer/e-commerce-dataset)
The pipeline runs data validation tests in the dataframe for compliance with the requirements of the model (test_dataset.py).

----------------

<br />

 Datasets are versioned using dvc and synchronized with remote storage. In order to remote the repository you should use **ID_FOLDER**:
 
    18aBRTpFRJMBK-ngecXdbx91aPD2f0Emg
    
[Link to the directory on Google Drive for dvc](https://drive.google.com/drive/folders/18aBRTpFRJMBK-ngecXdbx91aPD2f0Emg?usp=sharing)

----------------

<br />

The project is a machine learning pipeline of a data product implemented as a docker image. To run the docker you need to use the **command below**:


    sh ''' docker run -d --rm --name jen -v jenkins:/var/jenkins_home/data -p 80:8080 -p 88:8888 -p 50000:50000 jenkins:v1 '''

----------------

