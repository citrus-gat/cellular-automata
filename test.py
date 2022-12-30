import onedca

# Testing for onedca
def test_d2b():
    # Testing digits_to_bin 
    counter = 0
    for d3 in [0,1]:
        for d2 in [0,1]:
            for d1 in [0,1]:
                assert onedca.digits_to_bin(d3, d2, d1) == counter, \
                print('digits_to_bin(',d3,d2,d1,') =', onedca.digits_to_bin(d3, d2, d1), '\t expected:', counter)
                counter += 1


def test_n_dig():
    num = 0b0111_1010
    num = 0b1000_0101
    # Get a 8-bit binary string from num
    num_str = (bin(num)[2:]).rjust(8,'0')
    for n in range(8):
        assert onedca.n_digit_of_bin(num, n) == int(num_str[7-n]),\
            print('n_digit_of_bin({0}, {1}) = {2}\t expected: {3}'.format(num, n, onedca.n_digit_of_bin(num, n), num_str[7-n]))

def test():
    test_d2b()
    test_n_dig()

if __name__ == '__main__':
    test()