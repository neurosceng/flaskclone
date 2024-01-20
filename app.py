from flask import Flask,render_template,request,url_for,current_app,redirect
import os
import base64
import subprocess
from werkzeug.utils import secure_filename
import glob

app = Flask(__name__)
#app.run(debug=True) # デバッグモードを有効にする

@app.route("/")
def index():
    return "Hello , Flaskbook"

@app.route("/hello",methods=["GET","POST"])
def hello():
    return "Hello , world"

@app.route("/name/<name>")
def show_name(name):
    #変数をテンプレートエンジンに渡す
    return render_template("index.html",name=name)

@app.route("/button")
def html():
    #変数をテンプレートエンジンに渡す
    return render_template("button.html")

@app.route('/image/<path>')
def show_image(path):
    # テンプレートをレンダリングして表示
    return render_template('show_image.html', data=path)


@app.route("/dir/<path>")
def dir(path):
    # ファイルの絶対パスを取得
    #directory_path = os.path.join(app.static_folder, "photo", path)

    # ディレクトリ内のファイルをリストアップ
    #files = os.listdir(directory_path)
    file = os.getcwd()
    folder = file+"/"+path
    files = os.listdir(folder)

    # ファイルのリストをHTMLで表示
    return render_template("dir.html", files=files)

def get_image_base64(image_path):
    #image_path = "minimalapp/photo/bus.jpg"
    image_path = "/Users/okmac/flask/flaskbook/apps/minimalapp/photo/" + image_path
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

def get_image(image_path):
    #image_path = "minimalapp/photo/bus.jpg"
    print(image_path)
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

@app.route("/photo/<path>")
def show_photo(path):
    #path="fish.jpg"
    image_base64 = get_image_base64(path)
    return render_template("photo.html", image_data=image_base64)

@app.route("/upload")
def upload():
    return render_template("upload.html")

# 絶対パスでアップロードされた画像を保存するディレクトリを指定
UPLOAD_FOLDER = os.path.abspath('/Users/okmac/flask/flaskbook/apps/minimalapp/upload/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 保存先のディレクトリが存在しない場合は作成する
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/catch', methods=['POST'])
def catch():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        # アップロードされたファイルを保存
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(file_path)

        #ここからyolo
        cmd = "python3 detect.py --source upload/{} --conf 0.5 --weights yolov5s.pt".format(file.filename)
        # 実行
        subprocess.run(cmd.split())

        folder_path = sorted(glob.glob("/Users/okmac/flask/flaskbook/apps/minimalapp/runs/detect/*"))[-1]
        file_path = glob.glob(folder_path+"/*")[-1]

        image_base64 = get_image(file_path)

        return render_template("photo_show.html", image_data=image_base64)
        #return 'File uploaded successfully: {}'.format(file.filename)


@app.route("/yolo/<path>")
def yolo(path):
    #path="fish.jpg"
    image_base64 = get_image_base64(path)
    #ここからyolo


    
    return render_template("photo.html", image_data=image_base64)

@app.route("/yolotest")
def yolotest():
    # コマンド関数 
    #cmd = "ls -l"
    cmd = "python3 detect.py --source photo/ --conf 0.5 --weights yolov5s.pt"

    # 実行
    subprocess.run(cmd.split())
    return "yolo finished"