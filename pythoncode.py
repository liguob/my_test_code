class Person:

    def __init__(self,name,age):
        """

        :param name: 名字
        :param age: 年龄
        """
        self.name = name
        self.age = age

    def no_return(self):
        """

        :return: 是否成年人的True/False
        """
        if  self.age >= 18:
            self.is_adult = True
        else:
            self.is_adult = False

    def have_return(self,is_adult):
        """

        :param is_adult: 传入参数，是否成年人
        :return: 返回信息
        """
        if is_adult:
            return "成年人，生活不容易！"
        else:
            return "小孩子，你妈叫你回家吃饭了！"


#person_li = Person("Tom",18)
#person_li.no_return()
#print(person_li.have_return(person_li.is_adult))

