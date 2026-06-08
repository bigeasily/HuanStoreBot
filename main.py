# main.py
from bot import StoreManagerBot
import pyautogui
import time


def get_coordinates():
    print("\n=== 坐标获取工具 ===")
    print("把鼠标移动到对应位置，按 Ctrl+C 停止查看当前坐标")
    try:
        while True:
            x, y = pyautogui.position()
            print(f"\r当前坐标: ({x:4d}, {y:4d})", end="")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n坐标获取结束")


def capture_templates():
    print("\n=== 模板截图提示 ===")
    print("1. 在游戏中显示顾客头顶食物")
    print("2. 创建 templates 文件夹")
    print("3. 分别截图保存为：food_a.png、food_b.png、food_c.png")


def main():
    print("=" * 60)
    print("异环 - 店长自动化脚本")
    print("=" * 60)

    print("\n1. 获取坐标")
    print("2. 模板截图提示")
    print("3. 运行自动化")

    choice = input("\n请选择 (1/2/3): ").strip()

    if choice == "1":
        get_coordinates()
    elif choice == "2":
        capture_templates()
    elif choice == "3":
        bot = StoreManagerBot(confidence=0.65)   # 可调置信度
        cycles = int(input("请输入循环次数 (默认10): ") or "10")
        bot.run_loop(cycles)
    else:
        print("输入错误")


if __name__ == "__main__":
    main()
