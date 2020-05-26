# <div align=center> Under Guidence of </div>
# <div align=center> ░v░i░m░a░l░ ░d░a░g░a░</div><br/><br/>
### Now a quick review about project :<br/>
This is a project which would automate everything after developer commits code in GIT<br/>
Prerequities: **GIT , Docker, ngrok and Jenkins** should be pre installed on the top of Base system RHEL8<br/><br/>
**To deploy the project**
- Create a file named "Dockerfile" and copy paste from Dockerfile then save.
- Run the command same as `docker build -t mlops:latest .`
- In GIT bash go to Your `project_folder/.git/hooks//`
- Create post-commit file and copy paste data from `post-commit`
- Now in jenkins create job1 and write `cp -v -r -f * /myweb` in Execute shell.<br/>
  set triggers for SCM pooling and save
- Create job2 and copy paste the code <br/><br/>
`if sudo python3 /myenv/checking.py == CNN model<br/>
then
if sudo docker ps -a | grep testing
then
sudo docker rm -f testing
sudo docker run -v /myweb:/MLops --name testing mlops:latest
else
echo "Image not present"
fi
fi`
   set triggers to build after job1
- Create job3 and copy paste the code <br/><br/>
  `sudo python3 /myenv/mail.py`
   set triggers to builtd after job2
4) Open browser and type http://<IP of BaseOS>:1991 and copy paste the jenkins password from the above launched container and setup the environment.
5) In github set up hooks.
6) In GIT bash go to Your project_folder/.git/hooks/
7) create post-commit file and copy paste data from post-commit.
8) a. Copy paste code of job1
   b. Set trigger to **GitHub hook trigger for GITScm polling and build to production system**
   c. Save
9) a. Copy paste code of job2
   b. Set trigger to **Build after job1 **
   c. Save
10) a. Copy paste code of job3
   b. Set trigger to **Build after job2 **
   c. Save
11) a. Copy paste code of job4
   b. Set trigger to **Build after job3 **
   c. Save
12) Setup job5 as pipeline for all 4 jobs using Build pipeline as a monitoring system.

13) Refer ss for further clarifications

Step 1 and 2 are used for creating jenkins-centos image.
Step 3 and 4 are used to setup the Environment to launch jenkins.




I would like to Thank Mr. Vimal Daga sir for this Intresting task.
