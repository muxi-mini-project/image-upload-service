#--coding:utf-8--
import os  
from flask import Flask, request 

app = Flask(__name__)

UPLOAD_FOLDER=r'/home/humbert/pictures' #文件要存在哪一个位置
ALLOWED_EXTENSIONS=set(['png','jpg','jpeg']) #可以选择的文件拓展名 
  
def allowed_file(filename):  
    return '.' in filename and filename.split('.',1)[1] in ALLOWED_EXTENSIONS #按 '.' 分割一次后的第二个字符，即文件拓展名
																			   
 
@app.route('/',methods = ['GET','POST'])  
def upload_picture():  
    if request.method == 'POST':  
        file = request.files['file']  #从request请求的files字典中，取出file对应的文件。
        if file and allowed_file(file.filename):  
		file.save(os.path.join(UPLOAD_FOLDER,file.filename)) #保存在某个路径
		url = os.path.join(UPLOAD_FOLDER,file.filename) 
        	return url

	else:
		return 'Wrong'  
    return ''' 
    <!DOCTYPE html> 
    <title>Upload Picture</title> 
    <h1>Upload </h1> 
    <form action = "" method = "post" enctype=multipart/form-data> 
        <br>
		<input type = "file" name = file> 
		<br>
        <input type = "submit" value = Upload> 
	</form> 
    '''  

if __name__ == '__main__':
	app.run(debug=True)

#主要学着 http://blog.csdn.net/bestallen/article/details/52888876 这篇博文做的
		
