import os

import os


needremove = []


def get_file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):  # 获取当前文件夹的信息
        # print(files)
        print(files)
        for file in files:
            # print(file)# 扫描所有文件
            if os.path.splitext(file)[1] == ".docx":  # 提取出所有后缀名为md的文件
                bbb = os.path.join(root, file)
                needremove.append(bbb)


def removeself(seltlist):
    for i in range(len(seltlist)):
        os.remove(seltlist[i])


if __name__ == "__main__":
    get_file_name(
        r"C:\Users\geniusShi\Nutstore\1\我的坚果云\A知识库HTML\技术\01.尚硅谷Vue2Vue3全家桶代码")  # 修改文件路径
    removeself(needremove)
