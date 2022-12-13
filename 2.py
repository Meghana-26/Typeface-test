# We can add any number of phonetics into testcase 
testcase = """
          Murthy Moorthi Moorthy Murthi
          
          Meghana Megna Meghna

          Sathwik Sathvik Satwik Satvik

          Yaswanth Yaswant Yashwant Yashwanth
          
          Six Mix Fix

          Stay Sway 

    """
# Read input from the user in the form of string
name = input()
word = name

for item in testcase.split("\n"):
  if word in item :  
    # if the search word is present in the present line or list it will return entire list
    print(item.strip())