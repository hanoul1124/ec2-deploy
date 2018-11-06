# 이미지 빌드 (ec2-deploy폴더에서 실행)
# docker build -t ec2-deploy -f Dockerfile .
FROM        python:3.6.7-slim
MAINTAINER  hanoul1124@gmail.com

ENV         LANG                    C.UTF-8

# 패키지 업그레이드, Python3 설치
RUN         apt -y update
RUN         apt -y dist-upgrade
RUN         apt -y install gcc nginx supervior
RUN         pip3 install uwsgi

# requirements.txt 파일만 복사 후 패키지 설치
# requirements.txt 파일의 내용이 바뀌지 않으면 pip3 install ...
# 부분이 재실행되지 않는다.(빌드마다 계속 재설치하는 것을 피하기 위함)
COPY        requirements.txt /tmp/
RUN         pip3 install -r /tmp/requirements.txt

# docker build할 때의 PATH
#(현재 설정은 . (빌드한 현 위치=ec2-deploy폴더))에
# 해당하는 폴더의 전체 내용을
# Image의 /srv/project/폴더 내부에 복사

COPY        ./  /srv/project
WORKDIR     /srv/project

# 프로세스를 실행할 명령
# RUN은 이미지를 만드는 데에 사용됨
# CMD는 딱 한 번만 사용 가능함.
# CMD는 실제 실행하는 데 사용되며,
# docker run --rm -it -~~.... ec2-deploy(지금 이 이미지 이름)
# 위 명령어에서 이미지 이름 뒤에 아무것도, 붙이지 않으면 알아서 CMD를 실행한다.
WORKDIR     /srv/project/app
RUN         python3 manage.py collectstatic --noinput
#CMD         python3 manage.py runserver 0:8000


# Nginx
# 기존에 존재하던 Nginx설정파일들 삭제
RUN         rm -rf /etc/nginx/sites-available/*
RUN         rm -rf /etc/nginx/sites-enabled/*

# 프로젝트 Nginx설정파일 복사 및 enabled로 링크 설정
RUN         cp -f /srv/project/.config/app.nginx \
            /etc/nginx/sites-available/

RUN         ln -sf /etc/nginx/sites-available/app.nginx \
            /etc/nginx/sites-enabled/app.nginx

# Supervior설정파일 복사
RUN         cp -f /srv/project/.config/supervisord.conf \
            /etc/supervisor/conf.d/

# Command로 supervisor실행
CMD        supervisord -n

# uWSGI
#CMD         uwsgi --http :8000 --chdir /srv/project/app --wsgi config.wsgi
