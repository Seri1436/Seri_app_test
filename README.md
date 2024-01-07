# Testing Apps

소스코드 다운로드

    git clone https://github.com/Seri1436/test_apps.git

python 환경변수 및 가상환경 설정

    cd ./test_apps

    pyenv versions

    pyenv local 3.11.6

    pyenv versions

    echo '.env'  >> .gitignore
    echo '.venv' >> .gitignore

    ls -la

    python -m venv .venv

    source .venv/bin/activate

    python -V

프로젝트에 필요한 라이브러리 설치

    pip list

    pip install -r requirements.txt

    pip list | tee requirements.txt.detail

예제코드 테스트

    python main.py

python 가상환경 deactivate

    deactivate
