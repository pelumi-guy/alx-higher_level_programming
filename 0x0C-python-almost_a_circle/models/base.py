#!/usr/bin/python3
"""Base Class"""
import json
import csv
import os
import turtle



class Base:
    """base for this project. The goal of it is to
    manage id attribute in children classes and to avoid
    duplicating the same code (by extension, same bugs)"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes this base class
        Args:
            @id: id of object"""
        if id == None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Base class method that converts a dictionary
        to JSON string

        Args:
            list_dictionaries: dictionary to convert
        Return:
            JSON string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(i) == dict for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as cf:
            if list_objs is None:
                cf.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                cf.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Base class method that converts a json string
        to a python list

        Args:
            json_string: json string to convert
        Return:
            python list
        """
        if json_string is None or json_string == "":
            return []
        if (type(json_string) != str):
            raise TypeError("json_string must be a string")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns a constructed instance of class
        using dictionary attribues"""
        dummy = None
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Base class method that returns a
        list of class instances constructed from a
        json file"""

        filename = cls.__name__ + '.json'
        if os.path.exists(filename):
            with open(filename, 'r') as cf:
                inst_dict = Base.from_json_string(cf.read())

            inst_list = []
            for inst in inst_dict:
                inst_list.append(cls.create(**inst))
            return inst_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes a list of objects to csv
        and saves to a csv file

        Args:
            list_objs: list of objects to serialize
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as cf:
            if list_objs is None:
                cf.write("")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                # cf.write(Base.to_json_string(dict_list))
                data = []
                header = None
                if cls.__name__ == 'Rectangle':
                    header = ['id', 'width', 'height','x', 'y']
                elif cls.__name__ == 'Square':
                    header = ['id', 'size','x', 'y']
                for obj in dict_list:
                    row = []
                    row.append(obj['id'])
                    if cls.__name__ == 'Rectangle':
                        row.append(obj['width'])
                        row.append(obj['height'])
                    elif cls.__name__ == 'Square':
                        row.append(obj['size'])
                    row.append(obj['x'])
                    row.append(obj['y'])
                    data.append(row)

                csvwriter = csv.writer(cf)
                csvwriter.writerow(header)
                csvwriter.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a csv file and returns list
        of object contained there in"""
        filename = cls.__name__ + ".csv"
        data = []
        if os.path.exists(filename):
            with open(filename, 'r', newline='') as cf:
                csvreader = csv.reader(cf)
                header = next(csvreader)
                for row in csvreader:
                    data.append(row)

        obj_list = []
        obj_dict = {}
        for row in data:
            if cls.__name__ == 'Rectangle':
                attrs = ['id', 'width', 'height', 'x', 'y']
                for i in range(len(row)):
                    obj_dict[attrs[i]] = int(row[i])
            elif cls.__name__ == 'Square':
                attrs = ['id', 'size', 'x', 'y']
                for i in range(len(row)):
                    obj_dict[attrs[i]] = int(row[i])
            obj_list.append(cls.create(**obj_dict))

        return obj_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
