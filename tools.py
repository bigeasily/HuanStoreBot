"""
工具函数：获取坐标、截取模板图片
"""
import pyautogui
import time
import cv2
import numpy as np


def get_coordinates():
    """获取鼠标坐标"""
    print("\n鼠标坐标获取工具")
    print("把鼠标移到目标位置，按 Ctrl+C 退出")
    print("需要获取的坐标：")
    print("  - 1-1关卡按钮")
    print("  - 开始按钮")
    print("  - 退出按钮")
    print("  - 三个食物制作按钮（按顺序）")

    try:
        while True:
            x, y = pyautogui.position()
            print(f"\r当前坐标: ({x:4d}, {y:4d})", end="")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n\n坐标获取完成")
        print("请将坐标填入")


def capture_template(region, save_path):
    """
    截取指定区域并保存为模板图片
    region: (x, y, width, height)
    save_path: 保存路径
    """
    screenshot = pyautogui.screenshot(region=region)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    cv2.imwrite(save_path, screenshot)
    print(f"已保存: {save_path}")


def capture_templates_guide():
    """截取食物模板图片的引导"""
    print("\n模板图片截取工具")
    print("=" * 40)
    print("请在游戏中显示顾客头顶的食物图标")
    print("\n步骤：")
    print("1. 先运行 get_coordinates() 获取食物图标区域的坐标")
    print("2. 记录食物图标的左上角和右下角坐标")
    print("3. 用下面的代码截取：")
    print()
    print("   from tools import capture_template")
    print("   # 截取食物A")
    print("   capture_template((x1, y1, w, h), 'templates/food_a.png')")
    print()
    print("=" * 40)


def test_screenshot():
    """测试截图功能"""
    print("测试截图...")
    screenshot = pyautogui.screenshot()
    print(f"截图成功，大小: {screenshot.size}")

    # 保存测试截图
    screenshot.save("test_screenshot.png")
    print("已保存 test_screenshot.png")