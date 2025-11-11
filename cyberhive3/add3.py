#!/usr/bin/env python3
import sys

def add_command(args):
    #print(args)
    #print(len(sys.argv))
    
    # if len(sys.argv) > 2:
    #      print("Result: ignoring second input")

    #      return

    try:
        # Try to convert the first parameter to an integer
        # if it fails it raises the exception
        int(args)
        n = int(args)
        # Check if the number is in valid range [0..150]
        if 0 <= n <= 150:
            result = n + 1
            print(f"Result: {result}")
            print(result)
            return result
        else: 
            print("Result: Invalid input")
            print("Number out of range")
            return 'Invalid Input'
    except ValueError:
        # Text parameters are unsupported
        print('Invalid Input, Text Characters not supported')      
        return 'Invalid Input Text Characters not supported'
    
    
def main():
        if len(sys.argv) < 2:
            print("Usage: python add3.py <number>") 
            sys.exit(1)
        
        add_command(sys.argv[1])
        

if __name__ == "__main__":
    
    main()
     
     
         
 
   
       
    
     