import os

from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

# from utils import auto_get_solc_version

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/'  # 配置上传文件目录


# 加载主界面
@app.route('/')
def login_page():
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    data = {
        'msg': "用户名或密码错误！",
        'success': False
    }
    if request.method == 'POST':
        if request.form.get('username') == "admin" \
                and request.form.get('password') == "admin":
            data['msg'] = '登录成功！'
            data['success'] = True

    return jsonify(data)


@app.route('/success-page')
def jump_to_index_page():
    return render_template('check.html')


@app.route('/upload_file_path', methods=['POST', 'GET'])
def upload_file():
    try:
        # 检查是否有文件被上传
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        file_content = file.read()
        file_path = os.getcwd() + "/upload/" + file.filename
        with open(file_path, 'wb') as uploaded_file:
            uploaded_file.write(file_content)
        response_data = {
            'fileContent': file_content.decode('utf-8'),
            'versionNumber': auto_get_solc_version(file_path)
        }

        return response_data

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
