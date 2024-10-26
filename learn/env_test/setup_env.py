import subprocess
import sys

# 需要安装的库列表
required_packages = ['opencv-python', 'supervision', 'ultralytics']

# 检查库是否已安装
def check_packages():
    installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'list']).decode('utf-8')
    return [pkg for pkg in required_packages if pkg not in installed_packages]

# 创建新环境
def create_new_environment(env_name):
    subprocess.call(f'conda create --name {env_name} python=3.10 -y', shell=True)
    subprocess.call(f'conda activate {env_name} && pip install ' + ' '.join(required_packages), shell=True)

# 在当前环境中安装库
def install_in_current_environment():
    subprocess.call(f'pip install ' + ' '.join(required_packages), shell=True)

def main():
    while True:
        missing_packages = check_packages()
        
        if not missing_packages:
            print("所有库都已安装。")
            break

        print("缺少以下库：")
        for pkg in missing_packages:
            print(pkg)
        
        user_choice = input("选择操作：\n1. 创建一个新Conda环境\n2. 在当前Conda环境中安装库\n3. 退出\n请输入数字：")

        if user_choice == '1':
            env_name = input("请输入新的Conda环境名称：")
            create_new_environment(env_name)
        elif user_choice == '2':
            install_in_current_environment()
        elif user_choice == '3':
            print("退出脚本。")
            break
        else:
            print("无效选择，请重新输入。")

        # 询问用户是否继续
        continue_choice = input("是否继续检查库安装情况？(y/n): ")
        if continue_choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()