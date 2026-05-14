# Q19. Simulate the UPSC selection process with the following steps:

age = int(input("Enter your age : "))
Graduate = input("Are you Graduate? (yes/no) : ").lower()
Nationality = input("Enter your Nationality : ").lower()

if 21 <= age <=32:
    if Graduate.lower() == "yes":
        if Nationality.lower() == "indian":
            print("Eligible : Process to Prelims")

            #Prelims Exam
            prelims_marks = int(input("Enter prelims marks"))
            prelims_cutoff = 100

            if prelims_marks >= prelims_cutoff:
                print("Passed Prelims : Proceed to Mains")

                # Mains Exam
                mains_score = int(input("Enter Mains Marks : "))
                mains_cutoff = 200
                if mains_score >= mains_cutoff:
                    print("Passed Mains : Proceed to Interview")

                    #interview 
                    interview_marks = int(input("Enter Interview Marks : "))
                    interview_cutoff =70
                    if interview_marks >= interview_cutoff:
                        print("Congratulation ! you have cleared the UPSC")
                    else:
                        print("You failed in Interview")
                else:
                    print("You failed in Mains")
            else:
                print("You Failed in Prelims")        
        else:
            print("Ineligible: Nationality must be Indian.")
    else:
        print("Ineligible: Candidate must be a graduate.")
else:
    print("Ineligible: Age must be between 21 and 32 years.")