# food_maker.py
import time
import pydirectinput

pydirectinput.FAILSAFE = False


class FoodMaker:
    def __init__(self):
        # 各种食材/按钮坐标（请根据你的游戏实际坐标修改）
        self.ingredients = {
            # food_a 示例：面包 + 鸡蛋
            'food_a': [
                ('bread', (520, 620)),   # 点击面包（预制）
                ('egg', (680, 620)),     # 点击鸡蛋
            ],
            # food_b 示例：请替换成实际坐标和步骤
            'food_b': [
                ('dough', (520, 620)),
                ('meat', (820, 620)),
                ('vegetable', (980, 620)),
            ],
            # food_c 示例：请替换成实际坐标和步骤
            'food_c': [
                ('rice', (520, 620)),
                ('fish', (720, 620)),
                ('seaweed', (880, 620)),
            ],
        }

    def make_food(self, food_name: str):
        """制作指定食物"""
        if food_name not in self.ingredients:
            print(f"⚠️ 未知食物类型: {food_name}")
            return False

        steps = self.ingredients[food_name]
        print(f"🍳 开始制作 {food_name.upper()}...")

        for item_name, (x, y) in steps:
            print(f"   → 点击 {item_name} ({x}, {y})")
            pydirectinput.click(x, y)
            time.sleep(0.8)   # 每次点击后间隔

        print(f"✅ {food_name.upper()} 制作完成！")
        time.sleep(1.2)   # 制作完成后额外等待
        return True


# 测试用（可选）
if __name__ == "__main__":
    maker = FoodMaker()
    maker.make_food('food_a')