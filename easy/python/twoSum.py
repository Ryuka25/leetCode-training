#!/usr/bin/env python

print('''
/**************/
/* twoSum.py */
/**************/
''')

def twoSum(nums, target):
    nums = list(nums)
    target = int(target)

    print(f"[*] Nums list is {nums} and the Target is {target}")
    answers = []

    try:
        for i in range(0,len(nums)-1): # last number is already checked with the z iteration
            print(f"[*] Cheking for value matching with nums[{i}] = {nums[i]}")
            for z in range(i+1,len(nums)): # test the matching with all the 
                print(f"[*] ... Testing with nums[{z}] = {nums[z]}")
                if (nums[i]+nums[z] == target):
                    answers.append(i)
                    answers.append(z)
                    print("[!] Match found !")
                    break

            if (len(answers) > 0):
                break
            else:
                pass

        
        print(f"[!] The answers is {answers}\n[!] {nums[answers[0]]} + {nums[answers[1]]} = {target}")

    except:
        print("[!] Excepted error happen !")

def main():
    print("This programmes return the index of the two numbers in the nums's list where sum == target")
    print("e.g:twoSum([1,2,4], 3) will return the list [0,1]\ncause (nums[0] + nums[1]) == 3\n")
    
    print('[?] Choose on the the sample to test:')
    print('\t1 - nums = [4,5,3,2], target = 8')
    print('\t2 - nums = [2,4,6,7,1], target = 7')
    print('\t3 - nums = [1,2,3], target = 3')
    
    choosing = True
    while choosing:
        sample = input('[menu] > ')
        if (sample == '1'):
            twoSum(nums = [4,5,3,2], target = 8)
            break
        elif (sample == '2'):
            twoSum(nums = [2,4,6,7,1], target = 7)
            break
        elif (sample == '3'):
            twoSum(nums = [1,2,3], target = 3)
            break
        else:
            print('[!] Please choose a correct number of sample (123)')
            pass

if (__name__ == '__main__'):
    main()