import explog
import time

a = 102
b = "666"
c = [1, 2, 3]
explog.outputVar(a)
explog.generateLog([a], [b], [c])


@explog.get_time_output
def test():
    time.sleep(2)  # 模拟运行2s

print( test() )