import sys
import subprocess


# 필요 패키지 설치 -> 설치 불필요 시 주석 처리
def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])


for pk in ['numpy==1.19.3']:
    install(pk)
