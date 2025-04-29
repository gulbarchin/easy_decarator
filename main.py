#Написать класс который, имеет поле array и реализует инкапсуляцию по отношению
#array, так чтобы она не оставалась пустым и не присваивалась туда дублирующиеся значения


# Написать набор классов, которые реализуют методы:
# -get()-получает последний элемент из массива -array
# -update() -обновляет последний элемент из массива-array
# -pop()-удаляет последний элемент из массива -array

class WorkWithArray:
     def __init__(self, array):
         self._array = array

     @property
     def get_array(self):
         return self._array

     @get_array.setter
     def get_array(self, value):
      if not value:
          raise ValueError(" Значение array не должно быть пустым")
      if len(set(value)) != len(value):
          raise ValueError( "Массив не может содержать дублирующиеся значения ")
          self._array = value


class GetArray(WorkWithArray):
    def __init__(self, array):
        super().__init__(array)

    def get(self):
         return self._array[-1]

    def update(self, new_value):
        if new_value in self._array:
            raise ValueError("Такое значение уже есть в массиве")
        self._array[-1] = new_value

    def pop(self):
        return self._array.pop()


get_arr = GetArray([1,2,3])
result = get_arr.get()
print(result)

get_arr = GetArray([10,20,30])
print('Последний элемент:', get_arr.get())

get_arr.update(40)
print("После обновления:", get_arr.get_array)

get_arr.pop()
print("После применения pop()", get_arr.get_array)







