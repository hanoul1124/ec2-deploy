# 이미지 빌드 (ec2-deploy폴더에서 실행)
# docker build -t ec2-deploy -f Dockerfile .
FROM        ubuntu:18.04
MAINTAINER  hanoul1124@gmail.com

# 패키지 업그레이드, Python3 설치
RUN         apt -y update
RUN         apt -y dist-upgrade
RUN         apt -y install python3-pip

# Nginx , uWSGI 설치
RUN apt -y install Nginx
RUN pip3 install uwsgi

# docker build할 때의 PATH
#(현재 설정은 . (빌드한 현 위치=ec2-deploy폴더))에
# 해당하는 폴더의 전체 내용을
# Image의 /srv/project/폴더 내부에 복사
COPY        ./  /srv/project
WORKDIR     /srv/project
RUN         pip3 install -r requirements.txt

# 프로세스를 실행할 명령
# RUN은 이미지를 만드는 데에 사용됨
# CMD는 딱 한 번만 사용 가능함.
# CMD는 실제 실행하는 데 사용되며,
# docker run --rm -it -~~.... ec2-deploy(지금 이 이미지 이름)
# 위 명령어에서 이미지 이름 뒤에 아무것도, 붙이지 않으면 알아서 CMD를 실행한다.
WORKDIR     /srv/project/app
CMD         python3 manage.py runserver 0:8000