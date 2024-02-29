import random
import timeit
import tracemalloc
start = timeit.timeit()
for i in range(1,10):
    
    def measure_memory_usage(func):
        def wrapper(*args, **kwargs):
            tracemalloc.start()


            result = func(initial_value)

            snapshot = tracemalloc.take_snapshot()
            top_stats = snapshot.statistics("lineno")

            
            print(f"Memory usage of {func.__name__}:")
            for stat in top_stats[:5]:
                print(stat)

            return result

        return wrapper

    @measure_memory_usage




    def modify(initial_value):
   
            modified_value = initial_value + 10 
            doubled = modified_value * 2  
            squared = modified_value ** 2  
            halved = modified_value / 2  
    
            results = {
                "modified_value": modified_value,
                "doubled": doubled,
                "squared": squared,
                "halved": halved
            }
    
            return results
    end = timeit.timeit()
    initial_value = i
    result = modify(initial_value)
    print(f"Results: {result}")
    print(end - start)
    
