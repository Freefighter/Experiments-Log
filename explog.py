import sys
import os
import datetime
import pickle

# 避免在代码中 hardcode 参数信息，所有参数写在单独的一块；
# 每次实验运行保存至少如下信息：log信息（如运行时间、Loss结果等），
#   以及该次实验的configuration，主文件名称路径，
# 给每次实验取一个独特的id （时间+文件名）， 所有实验结果保存在该id的目录下。
# 提前准备好要保存的数据于save变量中

def retrieve_name_ex(var):
    frame = sys._getframe(2)    
    while(frame):        
        for item in frame.f_locals.items():            
            if (var is item[1]):
                return item[0]
        frame = frame.f_back    
    return "" 
    
def outputVar(var):    
    print("{} = {}".format(retrieve_name_ex(var),var))

    
def generateLog(config, result, save=None):
    # config 包括实验用的超参数 + 选用的模型名称，
    # result 包括loss结果 + runtime
    # save 包括需要存储的，更细一点的数据结果，比如每一轮的loss
    if not os.path.exists("log"):
        os.makedirs("log")
    
    filename = "{}_{}".format(
        os.path.split(__file__)[-1], str(datetime.datetime.now())
        ).replace(' ', '_'
        ).replace(':', '.')
        
    with open(os.path.join("log", filename + ".txt"), "w") as output:
        output.write("Configuration:\n")
        for var in config:
            output.write("{} = {}\n".format(retrieve_name_ex(var),var))
        
        output.write("\n\n")
        output.write("Experiments Result:\n")
        for var in result:
            output.write("{} = {}\n".format(retrieve_name_ex(var),var))
            
        output.write("\n\n")
        output.write("Saved Data:\n")
        for var in save:
            output.write("{}\n".format(retrieve_name_ex(var)))
        
    # print(filename)
    if not save is None:
        with open(os.path.join("log", filename + ".data"), "wb") as f: 
            pickle.dump(save, f)
        
    
    
    
if __name__ == "__main__":
    a = 10
    outputVar(a)
    
    print(__file__)
