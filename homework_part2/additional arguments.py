def function_name([positional_args(ex.: a),
                    [positional_args_with_default(b = 10),
                    [*pos_args_name(*args),
                    [keyword_only_ards(c = 10, d),
                    [**kw_args_name(**kwargs)]]]]])

def printab(a, b = 10, *args, c = 10, d, **kwargs):
    print(a, b, c, d)
printab(15, d = 15)

