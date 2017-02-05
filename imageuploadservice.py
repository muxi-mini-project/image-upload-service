#--coding:utf-8--
import os
from flask import Flask, request, send_from_directory,render_template
import time
UPLOAD_FOLDER=r'/home/imageuploadservice/pictures/' #文件要存在哪一个位置
ALLOWED_EXTENSIONS=set(['png','jpg','jpeg']) #可以选择的文件拓展名 

app = Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  #文件大小限制16M

def allowed_file(filename):
    return '.' in filename and filename.split('.',1)[1] in ALLOWED_EXTENSIONS #按 '.' 分割一次后的第二个字符，即文件拓展名


@app.route('/',methods = ['GET','POST'])
def upload_picture():
    if request.method == 'POST':
        file = request.files['file']  #从request请求的files字典中，取出file对应的文件。
        li = [str(int(time.time())),file.filename.split('.',1)[1]] #以上传的秒数为文件名，原文件类型为文件后缀名
        uploadtime ='.'.join(li)   #用join连在一起. 因为如果文件没有后缀名浏览器不会直接显示而是会下载
        if file and allowed_file(file.filename):
                file.save(os.path.join(UPLOAD_FOLDER,uploadtime)) #保存在某个路径
                url = os.path.join(UPLOAD_FOLDER,uploadtime)
                return url

        else:
                return render_template('error415.html')


    return render_template('upload.html')

@app.route('/home/imageuploadservice/pictures/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0', port=5000)


#主要学着 http://blog.csdn.net/bestallen/article/details/52888876 这篇博文做的
###
