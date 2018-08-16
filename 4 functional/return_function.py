def test(*args):
    return sum(args)
print(test(1,2,3,4,5))

def lazy_calc_sum(*args):
    def calc_sum():
        return sum(args)
    return calc_sum
s1=lazy_calc_sum(1,2,3,4,5)
s2=lazy_calc_sum(1,2,3,4,5)
print(s1, s1())
print(s2, s2())