#Python_program_to_interchange_first_and_last_elements_in_a_list
def swap(list):
    a=list[0],list[-1]=list[-1],list[0]
    
    return list 
    
# main code or driver code
list = [10,20,30,40,50]
print("before changing first and last element :",list)
print("After changing first and last element :",swap(list))