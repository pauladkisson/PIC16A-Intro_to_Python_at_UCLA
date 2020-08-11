#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27, 2020

@author: Paul Adkisson
"""


class StructuredDict:
    def __init__(self, d):
        self.__check(d)
        self.__d = d

    def __str__(self):
        return str(self.__d)

    def __repr__(self):
        return repr(self.__d)

    def __len__(self):
        return len(self.__d)

    def __contains__(self, item):
        return (item in self.__d)

    def __iter__(self):
        for key in self.__d:
            yield key

    def __getitem__(self, key):
        return self.__d[key]

    def __delitem__(self, key):
        raise DeleteError

    def __setitem__(self, key, value):
        if type(value) == self.__class__.key_to_type[key]:
            self.__d[key] = value
        else:
            raise UpdateValueError(key, value, self.__class__.key_to_type)
    
    def __check(self, d):
        input_keys = set(d.keys())
        true_keys = set(self.__class__.key_to_type.keys())
        missing_keys = true_keys - input_keys
        extra_keys = input_keys - true_keys
        type_error_keys = set()
        for key in true_keys:
            if key in input_keys:
                if type(d[key]) != self.__class__.key_to_type[key]:
                    type_error_keys.add(key)
                    
        if not(type_error_keys == set() and input_keys == true_keys):
            raise InitializationError(d, self.__class__.key_to_type, missing_keys, extra_keys, type_error_keys)


    

class StructuredDictError(Exception):
    pass

class DeleteError(StructuredDictError):
    
    def __str__(self):
        return "You cannot delete from a StructuredDict"

class UpdateValueError(StructuredDictError):
    def __init__(self, key, value, key_to_type):
        self.key = key
        self.value = value
        self.key_to_type = key_to_type
    
    def __str__(self):
        return "The type of %s is %s, but the value corresponding to the key %s should have type %s" % (self.value,
                type(self.value), repr(self.key), self.key_to_type[self.key])

class InitializationError(StructuredDictError):
    def __init__(self, d, key_to_type, mis, add, typ):
        self.d = d
        self.key_to_type = key_to_type
        self.missing_keys = mis
        self.extra_keys = add
        self.type_error_keys = typ
    
    def __str__(self):
        error_message = ""
        if self.missing_keys != set():
            missing_keys_msg = "the following keys are missing from d: {"
            idx = 0
            for key in self.missing_keys:
                idx += 1
                missing_keys_msg += repr(key)
                if idx != len(self.missing_keys):
                    missing_keys_msg += ", "
                else:
                    missing_keys_msg += "};"
            error_message += missing_keys_msg + "\n"
            
        if self.extra_keys != set():
            extra_keys_msg = "the following keys were supplied in error: {"
            idx = 0
            for key in self.extra_keys:
                idx += 1
                extra_keys_msg += repr(key)
                if idx != len(self.extra_keys):
                    extra_keys_msg += ", "
                else:
                    extra_keys_msg += "};"
            error_message += extra_keys_msg + "\n"
        
        if self.type_error_keys != set():
            for key in self.type_error_keys:
                error_message += "the type of d[%s] is %s, but it should be %s;" % (repr(key), type(self.d[key]), self.key_to_type[key])
                error_message += "\n"
        return error_message
        


class Rectangle(StructuredDict):
    key_to_type = {'len1': float, 'len2': float}

    def __init__(self, len1, len2):
        d = {'len1' : len1, 'len2' : len2}
        super().__init__(d)

    def area(self):
        return self['len1'] * self['len2']


class Student(StructuredDict):
    key_to_type = {'first name': str, 'last name': str, 'GPA': float}

    def __init__(self, first, last, gpa):
        d = {'first name': first, 'last name': last, 'GPA': gpa}
        super().__init__(d)

    def __str__(self):
        name = 'Name: ' + self['first name'] + ' ' + self['last name'] + ', '
        gpa = 'GPA: ' + str(self['GPA'])

        return name + gpa


'''
if __name__ == '__main__':
    r = Rectangle(2.0, 4.0)
    print('area =', r.area())

    def f1():
        r = Rectangle(2.0, 4.0)
        del r['len1']

    def f2():
        r = Rectangle(2.0, 4.0)
        r['len1'] = 2

    def f3():
        r = Rectangle(2, '4')
        return r

    def f4():
        class C(StructuredDict):
            key_to_type = {0:int, 1:int, 2:int, 3:float, 4:str}

        c = C({2:2, 3:3, 4:4, 5:5, 6:6})
        return c

    L = [f1, f2, f3, f4]

    for f in L:
        try:
            print('')
            f()
        except DeleteError as e:
            print('DeleteError:', e)
        except UpdateValueError as e:
            print('UpdateValueError:', e)
        except InitializationError as e:
            print('InitializationError:', e)


'''
# MY OUTPUT
# area = 8.0

# DeleteError: You cannot delete from a StructuredDict

# UpdateValueError: The type of 2 is <class 'int'>, but the value corresponding to the key 'len1' should have type <class 'float'>

# InitializationError: the type of d['len1'] is <class 'int'>, but it should be <class 'float'>;
# the type of d['len2'] is <class 'str'>, but it should be <class 'float'>;

# InitializationError: the following keys are missing from d: {0, 1};
# the following keys were supplied in error: {5, 6};
# the type of d[3] is <class 'int'>, but it should be <class 'float'>;
# the type of d[4] is <class 'int'>, but it should be <class 'str'>;