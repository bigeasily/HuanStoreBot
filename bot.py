# bot.py
import cv2
import numpy as np
import time
import mss
from screeninfo import get_monitors
import pydirectinput
from food_maker import FoodMaker

pydirectinput.FAILSAFE = False


class StoreManagerBot:
    def __init__(self, confidence=0.48):
        self.confidence = confidence
        self.sct = mss.mss()
        self.food_maker = FoodMaker()

        monitors = get_monitors()
        self.target_monitor = monitors[0]

        self.mss_monitor = {
            'left': self.target_monitor.x,
            'top': self.target_monitor.y,
            'width': self.target_monitor.width,
            'height': self.target_monitor.height
        }

        # 上半屏搜索区域
        self.upper_half = (0, 80, self.target_monitor.width, 550)

        self.coords = {
            'level_1_1': (176, 392),
            'start': (1684, 994),
            'exit': (22, 23),
            'lingqu':(1154,818)
        }

        self.food_templates = {
            'food_a': 'templates/food_a.png',
            'food_b': 'templates/food_b.png',
            'food_c': 'templates/food_c.png',
        }

    def capture_screen(self, region=None):
        """截取屏幕"""
        if region:
            adjusted = {
                'left': self.target_monitor.x + region[0],
                'top': self.target_monitor.y + region[1],
                'width': region[2],
                'height': region[3]
            }
            screenshot = self.sct.grab(adjusted)
        else:
            screenshot = self.sct.grab(self.mss_monitor)

        img = np.array(screenshot)
        return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    def find_new_food(self):
        """多尺度搜索食物"""
        screenshot = self.capture_screen(self.upper_half)
        found = []

        for food_name, template_path in self.food_templates.items():
            template = cv2.imread(template_path)
            if template is None:
                continue

            best_val = 0
            best_loc = None
            best_scale = 1.0

            for scale in [0.7, 0.85, 1.0, 1.15, 1.3]:
                scaled_template = cv2.resize(template, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
                if scaled_template.shape[0] > screenshot.shape[0] or scaled_template.shape[1] > screenshot.shape[1]:
                    continue

                result = cv2.matchTemplate(screenshot, scaled_template, cv2.TM_CCOEFF_NORMED)
                _, max_val, _, max_loc = cv2.minMaxLoc(result)

                if max_val > best_val:
                    best_val = max_val
                    best_loc = max_loc
                    best_scale = scale

            if best_val >= self.confidence:
                h, w = template.shape[:2]
                scaled_h = int(h * best_scale)
                scaled_w = int(w * best_scale)

                center_x = self.upper_half[0] + best_loc[0] + scaled_w // 2
                center_y = self.upper_half[1] + best_loc[1] + scaled_h // 2

                found.append((food_name, center_x, center_y, best_val, best_scale))

        found.sort(key=lambda x: x[1])
        return found

    def run_detection_and_making(self, max_time=50):
        """边识别边制作"""
        print(f"\n🔄 开始边识别边制作（最多 {max_time} 秒）...")
        start_time = time.time()
        made_count = 0

        while time.time() - start_time < max_time and made_count < 3:
            foods = self.find_new_food()

            for food_name, _, _, conf, scale in foods:
                if made_count >= 3:
                    break

                print(f"🎯 检测到 {food_name.upper()} (缩放 {scale:.2f}x, 置信度 {conf:.4f}) → 开始制作")

                self.food_maker.make_food(food_name)

                made_count += 1
                time.sleep(1.2)
                break

            time.sleep(0.5)

        print(f"✅ 本轮制作完成，共制作 {made_count} 个食物")

    def press_f(self):
        # if 'exit' in self.coords:
        #     ex = self.coords['exit']
        #     pydirectinput.click(ex[0] + 60, ex[1] + 60)
        #     time.sleep(0.3)
        pydirectinput.press('f')
        print("✅ 按下 F 键进入")

    def click(self, x, y):
        pydirectinput.click(x, y)
        print(f"✅ 点击: ({x}, {y})")
        time.sleep(0.2)

    def enter_level(self):
        print("\n--- 进入关卡 ---")
        self.press_f()
        time.sleep(1.3)
        self.click(*self.coords['level_1_1'])
        time.sleep(1)
        self.click(*self.coords['start'])
        print("等待关卡加载...")
        time.sleep(3)

    def exit_level(self):
        print("\n--- 退出关卡 ---")
        self.click(*self.coords['exit'])
        time.sleep(1.5)

    def run_one_cycle(self):
        self.enter_level()
        self.run_detection_and_making(max_time=50)
        self.exit_level()
        self.click(*self.coords['lingqu'])
        print("✅ 一轮完成\n")

    def run_loop(self, cycles=10):
        print(f"开始运行 {cycles} 轮...\n")
        time.sleep(2)
        for i in range(cycles):
            print(f"========== 第 {i + 1} 轮 ==========")
            self.run_one_cycle()
            time.sleep(2)