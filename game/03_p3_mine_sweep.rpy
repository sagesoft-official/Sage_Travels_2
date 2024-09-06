label MineSweep:
    "扫雷开始"
    python:
        import os
        os.system(os.getcwd() + "桑尾草原/桑尾草原.exe")

    "... ..."

    python:
        if not os.path.exists("桑尾草原.txt"):
            MineSweep_status = False
        else:
            MineSweep_status = True
    if MineSweep_status:
        "扫雷成功"
    else:
        "扫雷失败"

    jump label_p3