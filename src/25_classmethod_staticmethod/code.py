class ClassTest:
    def instance_method(self):
        print(f"Class instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method.")

classTest = ClassTest()
classTest.instance_method()

ClassTest.instance_method(classTest)

ClassTest.class_method()

ClassTest.static_method()