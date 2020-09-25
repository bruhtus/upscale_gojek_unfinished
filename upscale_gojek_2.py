from fire import Fire
from tqdm import tqdm

def main(file_input, file_output):
    input_array = []

    f = open(file_input, 'r')
    numbers = f.readlines()

    for number in tqdm(numbers):
        input_array.append(int(number))

    t = input_array[0]
    a = 1
    b = 2
    k = 3

    #print(f'there is {t} case')

    for i in tqdm(range(len(input_array))):
        input_a = input_array[a]
        input_b = input_array[b]
        input_k = input_array[k]
        
        divisable(file_output, i, input_a, input_b, input_k)

        if a <= (len(input_array)-6) and b <= (len(input_array)-5) and k <= (len(input_array)-4):
            a += 3
            b += 3
            k += 3
        else:
            #print(f'finished all {t} case')
            break

def divisable(output_file, t, a, b, k):
    x = 0 # the number that divisable by k, between a and b
    f_output = open(output_file, 'a+')

    #f_output.write(f'a = {a}, b = {b}, k = {k}\r\n')

    if a >= 1 and b < 10000:
        if a <= b:
            while a <= b:
                if k >= 1 and k < 10000:
                    if a % k == 0:
                        x += 1
                        a +=1
                    else:
                        a +=1
                else:
                    print('out of constraints')
                    break

            f_output.write(f'Case {t+1}: {x}\r\n')

        else:
            print('out of constraints')

    else:
        print('out of constraints')


if __name__ == '__main__':
    Fire(main)
