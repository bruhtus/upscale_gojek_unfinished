from fire import Fire
import readline

def main(test_cases):
    if test_cases >= 1 and test_cases <= 100:
        for test in range(test_cases):
            a, b, k = [int(x) for x in input('enter a, b, k: ').split()]
            divisable(test, a, b, k)
    else:
        print('out of constraints')

def divisable(t, a, b, k):
    x = 0 #the number that divisable by k, between a and b

    if a >= 1 and b < 10000:
        if a <= b:
            while a <= b:
                if k >= 1 and k < 10000:
                    if a % k == 0:
                        x += 1
                        a += 1
                    else:
                        a += 1
                else:
                    print('out of constraints')
                    break

            print(f'case {t+1}: {x}')

        else:
            print('out of constraints')

    else:
        print('out of constraints')

if __name__ == '__main__':
    Fire(main)
