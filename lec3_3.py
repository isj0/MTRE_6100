class Base():

    # Class Constrcutor
    def __init__(self):     # self is similar to this keyword in c++
        print( 'Class Constructor' )
        # self allow defining object to use within the class
        self.place_hodler = None
        # without self, the object only exists as local object
        second_item = None


    # Class Destrcutor
    def __del__(self):
        print( 'Class Destructor' )

    def __add__(self, RHS):
        #check the type of the RHS & provide solutions for any type
        #type(RHS) == type(int())
        #type(RHS) == type(self)
        print('Add was called')
        print(f'Our RHS is: {RHS}')
        print(f'The type is: {type(RHS)}')

        if type( RHS ) == type( int() ):
            print('We can do something with the integer')
            self.place_holder = 7

    def cal_avg(items = None):
        if items in None:
            return
        
    def print_info():
        print('This is the base Class')


def main():
    base_object = Base()
    base_object2 = Base()
    base_object + base_object2

if __name__ == '__main__':
    main()

