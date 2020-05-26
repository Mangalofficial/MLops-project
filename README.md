# <div align=center> Under Guidence of </div>
# <div align=center> ░v░i░m░a░l░ ░d░a░g░a░</div><br/><br/>
### Now a quick review about project :<br/>
This is a project which would automate everything after developer commits code in GIT<br/>
Prerequities: **GIT , Docker and Jenkins** should be pre-installed on the top of Base system RHEL8<br/><br/>
**To deploy the project**
- Create a file named "Dockerfile" and copy paste from Dockerfile then save.
- Run the command same as `docker build -t mlops:latest .`
- In GIT bash go to Your `project_folder/.git/hooks//`
- Create post-commit file and copy paste data from `post-commit`
- Now in jenkins create job1 and write `cp -v -r -f * /myweb` in Execute shell.<br/>
  set triggers for SCM pooling and save
- Create job2 and copy paste the code <br/><br/>
`if sudo python3 /myenv/checking.py == CNN model`<br/>
`then`<br/>
`if sudo docker ps -a | grep testing`<br/>
`then`<br/>
`sudo docker rm -f testing`<br/>
`sudo docker run -v /myweb:/MLops --name testing mlops:latest`<br/>
`else`<br/>
`echo "Image not present"`<br/>
`fi`<br/>
`fi`<br/>
   set triggers to build after job1
- Create job3 and copy paste the code <br/><br/>
  `sudo python3 /myenv/mail.py`<br/>
   set triggers to builtd after job2
- Setup job4  as pipeline for all 3 jobs using Build pipeline as a monitoring system.

### Refer ss for further clarifications

- Job1 : Download the code and store it in `/myenv` folder.<br/>
- Job2 : Check the code and accordingly launch the container for model training. Also it check the accuracy of the model and if `acc < 0.95` it retrains the model after changing the architecture of the model. After the training the model it stores the accuracy of the model to `/MLops/accuracy.txt` file.<br/>
- Job3 : After getting best accuracy it notify to the developer for accuracy via E-mail.<br/>
- Job4 : Monitoring system for all 3 jobs using Build pipeline.<br/>



## I would like to Thank Mr. Vimal Daga sir for this Intresting task.
