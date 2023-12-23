import pprint
gen = [3,10] # generator = [x,y]
modulo = 23
a_coeff = 1


def point_addition(p_1,p_2):
    lambda_coff = 0
    x_3 = 0
    y_3 = 0

    if isinstance(p_1,str):
        return p_2

    if(p_1==p_2):
        lambda_coff = ((3*pow(p_1[0],2)+a_coeff)%modulo)*(pow(2*p_1[1],-1,modulo))
        lambda_coff =  lambda_coff % modulo

    else:
        delta_x = (p_2[0] - p_1[0]) % modulo 
        delta_y = (p_2[1] - p_1[1]) % modulo
        if 0==delta_x:
            return "inf"
        lambda_coff = (delta_y)*(pow(delta_x,-1,modulo))
        lambda_coff =  lambda_coff % modulo

    x_3 = pow(lambda_coff,2) - p_1[0] - p_2[0]
    x_3 = x_3 % modulo 
    y_3 = (p_1[0] - x_3)*lambda_coff - p_1[1]
    y_3 = y_3 % modulo
    return ([x_3,y_3])


def main():
    point = point_addition(gen,gen) 
    index = 1
    group = {}
    group[f"{index}p"]=gen
    while index != 33:
        index = index + 1
        group[f"{index}p"]=point
        point = point_addition(point,gen) 
        point_prev =group[f"{index}p"]
        print(f"p{index}:{point}={point_prev}+{gen}[x,y]")
    print(f"group: {group}")


main()
