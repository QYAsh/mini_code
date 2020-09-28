word_list = [[],[],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],
    ["p","q","r","s"],["t","u","v"],["w","x","y","z"]]

def combine(a, b):
    r_list = []

    if len(a) == 0 and len(b) > 0:
        r_list = b
    elif len(a) > 0 and len(b) == 0:
        r_list = a
    else :
        for i in a:
            for j in b:
                r_list.append(i+j)
    return r_list

def solve(input_num_list):
    con_list = [] #字母二维列表
    r_list=[] #输出列表

    for i in input_num_list:
        try:
            con_list.append(word_list[int(i)])
        except IndexError:
            print("Invalid input ! List items must between 0 to 9")
            raise

    iter_input_list = iter(con_list)
    r_list = next(iter_input_list)
    while(True):
        try:
            n_list = next(iter_input_list)
            r_list = combine(r_list, n_list)
        except StopIteration:
            break
    return r_list

if __name__ == "__main__":
    # 接受控制台输入 start
    # user_input = input("input like [2,3]: ")

    # pattern = re.compile(r'\d+')
    # input_num_list = pattern.findall(user_input)
    # 接受控制台输入 end

    #输入列表
    input_num_list = [2,3] 
    print("input: ", end="")
    print(input_num_list)
    
    r_list = solve(input_num_list)

    print("Output:", end=" ")
    for i in r_list:
        print(i, end=" ")
