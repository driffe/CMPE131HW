import time

def calculate_time(function):
        '''
        Wrap the function that calculate the time for the function

        Parameter
        ---------
        function:
                function for getting value of the runtime
        return
        ------
        inner fucntion
                Calls the actual function(wrapper)
        '''
        def wrapper():
                '''
                Calculate the time for the function

                '''
                start = time.time()
                function()
                end = time.time()
                print(f"Total time {end - start}")
        return wrapper
def counting():
        '''
        the value to calculate the runtime
        '''
        time.sleep(2)
        for i in range(10):
                print(i)

result = calculate_time(counting)
result()