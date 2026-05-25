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
                ('1',(732,992)),  #制作面报
                ('bread', (605, 780)),   # 点击面包（预制）
                ('egg', (384, 631)),     # 点击鸡蛋
            ],
            # food_b 示例：请替换成实际坐标和步骤
            'food_b': [
                ('1', (990, 987)),
                ('meat', (1254, 1010)),
                ('vegetable', (1024, 626)),
            ],
            # food_c 示例：请替换成实际坐标和步骤
            'food_c': [
                ('1', (136, 937)),
                ('fish', (116, 786)),
                ('seaweed', (220, 626)),
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
            if item_name == '1':
                time.sleep(1.7)   # 每次点击后间隔
            else:
                time.sleep(1)

        print(f"✅ {food_name.upper()} 制作完成！")
        time.sleep(0)   # 制作完成后额外等待
        return True


# 测试用（可选）
if __name__ == "__main__":
    maker = FoodMaker()
    maker.make_food('food_a')