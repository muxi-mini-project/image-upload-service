# image-upload-service
存放上传图片API
#功能
上传本地的一个图片到服务器的磁盘，并返回图片存放在磁盘中的URL地址。<br>
大家可以去 [http://120.77.80.219:5000](http://120.77.80.219:5000) 上看下效果。<br>
#部署过程
1，在阿里云上购买服务器。选择的1G1核的配置，操作系统选择的``Ubuntu16.04 64位``<br>
（一开始想用Docker，但是怎么都搞不明白Docker该怎么用......问了朱学长之后改为直接在服务器上部署。）<br>
2，安装nginx ``sudo apt-get install nginx``<br>
启动nginx ``sudo /etc/init.d/nginx start``<br>
安装uwsgi和其组件 `` sudo apt-get install build-essential python-dev    sudo pip install uwsgi``<br>
3，用git命令将上传到github的``image-upload-service``克隆到本地：<br>
  `` git clone https://github.com/muxi-mini-project/image-upload-service.git ``<br>
  这里注意在app.run 中的参数 ``app.run(debug=True,host='0.0.0.0', port=5001)`` host 和 port <br>
4, 用Nginx处理Web服务<br>
/etc/nginx/sites-enabled/defualt 文件
```
server{
        listen 80;
        server_name upload.muxixyz.com;
        access_log /home/imageuploadservice/docs/access.log;
        error_log /home/imageuploadservice/docs/error.log;
        location /{
                        include uwsgi_params;
                        uwsgi_pass 127.0.0.1:8001 ;
                        uwsgi_param UWSGI_CHDIR /home/imageuploadservice ;
                        uwsgi_param UWSGI_SCRIPT imageuploadservice.py ;
        }
}
```
5, 启动配置uWSGI<br>
uwsgi.ini文档
```
[uwsgi]
socket = 127.0.0.1:8001
chdir = /home/imageuploadservice/
wsgi-file =imageuploadservice.py
mudule = wsgi
callable = app
processes = 4
threads = 2

```


（4，5两步的细节以及一些关于nginx和uwsgi的介绍可以看 [Flask+uWSGI+Nginx+Ubuntu部署教程](http://www.linuxidc.com/Linux/2016-06/132690.htm))<br>
6,此时就可以用 python XXX.py 的命令来运行了。但是，我们想让它即使在我们关闭命令行之后还是在运行，这时我们就需要 ``nohup``命令了。<br>
  通过<br>``nohup uwsgi uwsgi.ini & `` <br>
  命令，我们就能让这个文件即使在我们退出了服务器的命令行之后仍然可以正常运行。
  
