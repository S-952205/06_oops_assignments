# humnay eik logger class banani hai jo message print kray object create (constructor) krtay waqt or 
# message print kray jb object destroyed (destructor) hojai 

class Logger:

    # Constructor
    def __init__(self):
        print('Logger object created.....')

    # Destructor
    def __del__(self):
        print('Logger object destroyed.....')


# object created 
obj = Logger()

# we can manually destroy the objects 
# del obj
