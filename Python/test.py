# Algorithm to find the single number in an array of pairs of numbers
def test(numbers):
	temp=0;
	for x in range(0,len(numbers)):
		temp=temp^numbers[x]
	
	return temp


nums=[1,1,2,2,3,5,5]

print test(nums)
