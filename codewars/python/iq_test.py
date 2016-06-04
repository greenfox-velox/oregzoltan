def iq_test(numbers):
    #your code here
    odd = 0
    even = 0
    counter = 0
    num_list = numbers.split()
    for i in num_list:
        if int(i) % 2 == 0:
            even += 1
            if even == 1:
                even_index = counter
        else:
            odd += 1
            if odd == 1:
                odd_index = counter
        counter += 1
    if even == 1:
        return even_index+1
    else:
        return odd_index+1

print(iq_test("1 2 2"))
