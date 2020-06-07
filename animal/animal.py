import yaml
import os


class Animal():

    def __init__(self, name: str, color: str, age: int, gender: str):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def run(self):
        print(f"{self.name}会跑")

    def shout(self):
        print(f"{self.name}会叫")

    def hunt_mouse(self):
        print(f"{self.name}正在抓老鼠")


class Cat(Animal):

    def __init__(self, name, color, age, gender, hair="短毛"):
        self.hair = hair
        super(Cat, self).__init__(name, color, age, gender)

    def shout(self):
        print(f"{self.name}会喵喵叫")


class Dog(Animal):

    def __init__(self, name, color, age, gender, hair="长毛"):
        self.hair = hair
        Animal.__init__(self, name, color, age, gender)

    def shout(self):
        print(f"{self.name}会汪汪叫")

    def look_home(self):
        print(f"{self.name}会看家")


if __name__ == '__main__':
    yml_file_path = os.path.join(os.getcwd(), "animal.yml")
    with open(str(yml_file_path), "r", encoding="UTF-8")  as f:
        content = yaml.safe_load(f.read())

    cat_miaomiao = Cat(**content["cat"])
    # print(cat_miaomiao.name,cat_miaomiao.age,cat_miaomiao.hair,cat_miaomiao.color,cat_miaomiao.gender)
    dog_wangcai = Dog(**content["dog"])
    cat_miaomiao.hunt_mouse()
    print(f"猫的姓名：{cat_miaomiao.name}，颜色：{cat_miaomiao.color}，年龄：{cat_miaomiao.age}岁，性别：{cat_miaomiao.gender}，毛发：{cat_miaomiao.hair}，抓到了老鼠")
    dog_wangcai.look_home()
    print(f"狗的姓名：{dog_wangcai.name}，颜色：{dog_wangcai.color}，年龄：{dog_wangcai.age}岁，性别：{dog_wangcai.gender}，毛发：{dog_wangcai.hair}")