
import timing

code = "[ x ** 2 for x in range(1_000) ]"

result = timing.time_it(code, 1000)
print(result)
