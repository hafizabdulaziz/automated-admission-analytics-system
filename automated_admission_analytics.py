import os
from datetime import datetime
def save_to_file(data_string):
    with open("university_database.json","a") as file:
        file.write(data_string + "\n")
def view_all_records():
    if not os.path.exists("university_database.json"):
     print("\n[!] No Records Found.Database Is Empty.")
     return
    print("\n--- Current Database Records ---")
    with open("university_database.json","r") as file:
         for line in file:
            print(line.strip())
    print("-------------------------------")
def show_analytics():
    if not os.path.exists("university_database.json"):
        print("\n[!] No Data To Analyze.")
        return
    total = 0
    approved = 0 
    with open("university_database.json","r") as file:
            for line in file:
                total += 1
                if "approved" in line.lower():
                    approved += 1
    print(f"\n--- System Analytics ---")
    print(f"Total Applications: {total}")
    print(f"Total Approved: {approved}")
    print(f"Total Rejected: {total - approved}")
    if total > 0:
        (f"Success Rate: {(approved/total)*100:.2f}%")
def main():
    while True:
        print("\n===== UNIVERSITY ADMISSION SYSTEM =====")
        print("1. Add New Student")
        print("2. View all Records")
        print("3. View Analytics")
        print("4. Exit")
        choice = input("Select An Option(1-4): ")
        if choice == "1":
            name = input("Enter Your Name: ")
            if not name.strip():
                print("Name is Mandatory")
                continue
            dept = input("Enter Your Deparetment(Pre Medical/Pre Engineering/Computer Science): ").lower()
            try:
                marks = int(input("Enter Your Marks: "))
                age = int(input("Enter Your Age: "))
                status = ""
                reasons = []
                if "pre engineering" in dept or "computer science" in dept:
                    if marks >= 70 and age >= 18:
                       status = "Approved: You Are passed! Welcome To Our College"
                    else:
                        reasons = []
                        if marks < 70:
                           reasons.append(f"{70 - marks} marks short")
                        if age < 18:
                           reasons.append("Minimum Age Must Be 18")
                        status = f"Rejected: {', '.join(reasons)}"
                elif "pre medical" in dept:
                    if marks >= 80 and age >= 18:
                       status = "Approved: You Are Passed! Welcome To Our Collage"
                    else:
                        medical_reasons = []
                        if marks < 80:
                           medical_reasons.append(f"{80 - marks} marks short")
                        if age < 18:
                           medical_reasons.append("Minimum Age Must Be 18")
                        status =  f"Rejected: {', '.join(medical_reasons)}"
                else:
                    status = "Error: Department Not Recognized"
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                record = f"{now} | Name: {name} | Dept: {dept} | Status: {status}"
                save_to_file(record)
                print(f"\n[+] Record Saved For {name}!")
            except ValueError:
              print("[!] Error: Please Enter Numbers Only For Marks And Age!")
        elif choice == '2':
            view_all_records()
        elif choice == '3':
            show_analytics()
        elif choice == '4':
            print("CLOSING SYSTEM. GOODBYE!")
            break
        else:
            print("Invalid Choice!")
if __name__ == "__main__":
   main()
   













