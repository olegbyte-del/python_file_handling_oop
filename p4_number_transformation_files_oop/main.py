# Main Program

import integer_processor as ip 

analysis = ip.NumberAnalysis()
read = ip.FileManager()

while True:
    try:
        print("="*50, "Number Analysis".center(50), "="*50, sep="\n")
        print("[1] File Manager", 
            "[2] Number Analysis",
            "[0] Exit", "="*50, sep="\n")
        
    except Exception as e:
        print(f"Error Occured! {e}")

