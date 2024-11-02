def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

inner_function() # имя функции не определяется в глобальном прстранстве
                # т.к. функция inner_function находится в локальном пространстве
                # функции test_function

