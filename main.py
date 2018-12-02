import subprocess
import time
from tools.sendMessageToDD import sendMessage
def add():
    cmd = "git add ."
    process = subprocess.Popen(cmd, shell=True)
    process.wait()
    returnCode = process.returncode

    if returnCode != 0:
        print(" add returnCode", returnCode)
    else:
        commit()
commitMessage = ""
def commit():
    global commitMessage
    commitMessage = time.strftime("%Y/%m/%d %H:%M")
    cmd = "git commit -m  '{}'".format(commitMessage)

    # print("cmd = " + cmd)
    process = subprocess.Popen(cmd, shell=True)
    process.wait()
    push()
def push():
    cmd = "git push origin master"
    process = subprocess.Popen(cmd, shell=True)
    process.wait()
    returnCode = process.returncode
    if returnCode != 0:
        print("push returnCode", returnCode)
    else:
        sendMessage({
            "fileName": "api文档 : \n\n已更新，请注意查看！ \n" +"\n更新信息: {}".format(
                commitMessage),
            "text": time.strftime("%Y/%m/%d %H:%M"),
            "error": False
        })
add()
