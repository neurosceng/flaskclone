import subprocess

# コマンド関数 
#cmd = "ls -l"
cmd = "python3 detect.py --source photo/ --conf 0.5 --weights yolov5s.pt"

# 実行
subprocess.run(cmd.split())