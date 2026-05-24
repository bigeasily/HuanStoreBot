import pyautogui
import time
import os


def get_coordinates():
    """获取鼠标坐标工具"""
    print("\n鼠标坐标获取工具")
    print("请依次把鼠标移到以下位置，按 Ctrl+C 记录：")
    print("  1. 1-1关卡按钮")
    print("  2. 开始按钮")
    print("  3. 退出按钮")
    print("  4. 三个食物制作按钮")
    print("  5. 三个顾客头顶区域（左上角和右下角）")

    try:
        while True:
            x, y = pyautogui.position()
            print(f"\r当前坐标: ({x:4d}, {y:4d})", end="")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n\n坐标获取完成")
        print("请手动记录你看到的坐标值")


def capture_templates():
    """截取模板图片提示"""
    print("\n模板图片截取工具")
    print("请在游戏中显示顾客头顶的食物图标")
    print("按提示截取图片...")

    print("\n请手动操作：")
    print("1. 在项目目录下创建 templates 文件夹（若不存在）")
    print("2. 用截图工具截取顾客头顶的每个食物图标")
    print("3. 保存为 food_a.png, food_b.png, food_c.png")
    print("4. 放在 templates 文件夹中")

    # 确保 templates 文件夹存在
    os.makedirs('templates', exist_ok=True)
    print("\n已确保 templates/ 目录存在，请将模板图片放入其中。")