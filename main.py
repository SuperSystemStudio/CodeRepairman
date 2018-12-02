from flask import Flask, request
import json
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    path = 'workspace/www'  # 项目目录
    return _hooks(path, request.data)

def _hooks(path, data):
    post_data = json.loads(data)
    ref = post_data['ref']
    branch_name = ref.split('/')[-1]
    status = os.system("cd %s && git checkout %s && git pull --rebase" % (path, branch_name,))
    if status == 0:
        return 'success'
    else:
        return 'error'

if __name__ == '__main__':
    app.run(threaded=True, debug=True)