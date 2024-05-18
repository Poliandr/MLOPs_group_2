# MLOPs_group_2

Repository of team №2 as final project for MLops.

---------------------

  [link to the dataset on Kaggle](https://www.kaggle.com/datasets/poojakeer/e-commerce-dataset)

[link to the directory on Google Drive for dvc](https://drive.google.com/drive/folders/18aBRTpFRJMBK-ngecXdbx91aPD2f0Emg?usp=sharing), for dvc remote repository take only ID_FOLDER=18aBRTpFRJMBK-ngecXdbx91aPD2f0Emg

to run docker:
sh '''
docker run -d --rm --name jen -v jenkins:/var/jenkins_home/data -p 80:8080 -p 88:8888 -p 50000:50000 jenkins:v1
'''


# MLOPs_group_2.

Repository of team №2 as final project for MLops.


---------------------

    [link to the dataset on Kaggle](https://www.kaggle.com/datasets/poojakeer/e-commerce-dataset)

3. Запускаем контейнер.
----------------

    docker run --name container_name -p 8000:8000 image_name

4. Получаем ссылку в терминале.
----------------------

    Uvicorn running on http://0.0.0.0:8000
