## MlOps: Integration of ML and DevOps
*The model has been created with an ideology to achieve automation. Often, the machine learning model achieves better accuracy with lots of hyper-parameter tuning. But when it comes to the deep neural network, it is really a tedious task to achieve it.*

> - Problem statement
```
1. Create container image that’s has Python3 and Keras or numpy  installed  using dockerfile 
2. When we launch this image, it should automatically starts train the model in the container.
3. Create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins 
4. Job1 : Pull  the Github repo automatically when some developers push repo to Github.
5. Job2 : By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed    interpreter install image container to deploy code  and start training( eg. If code uses CNN, then Jenkins should start the container    that has already installed all the softwares required for the cnn processing).
6. Job3 : Train your model and predict accuracy or metrics.
7. Job4 : if metrics accuracy is less than 80%  , then tweak the machine learning model architecture.
8. Job5: Retrain the model or notify that the best model is being created
9. Create One extra job job6 for monitor : If container where app is running. fails due to any reason then this job should automatically start the container again from where the last trained model left
```
To keep this in mind, I have automated the ml code with the help of docker container and  Jenkins. A separate environment has been built in the docker container with pre-installed required libraries to run the code. First of all, Job of build pipeline will fetch the code from the Github repository. Then, Jenkins will filter the code type i.e. either it is a simple machine learning model or neural network model and as per requirement launch the container. If the model doesn't achieve accuracy up to the mark, a mail will be sent to the developer. And if model crashes, it will automatically trigger the job to build the model again.

Detail setup of the environment:

> - Create a Dockerfile to setup the container environment
![Image](https://github.com/Shivamshiv/MlOps_code_optimization/tree/master/Images/dockerfile.png)
