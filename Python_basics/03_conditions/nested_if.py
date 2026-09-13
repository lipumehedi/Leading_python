# ==========================================
# Python Control Flow
# Nested If Statement
# ==========================================

"""
Nested if means an if statement inside another if statement.

Candidate Selection Process:

1. CGPA > 3.5
       ↓
2. First Interview Score > 80
       ↓
3. Second Interview Score > 90
       ↓
4. Non-Smoker
       ↓
5. Offer Letter
"""


# Get candidate information

cgpa = float(input("Enter candidate CGPA: "))


# First condition: CGPA

if cgpa > 3.5:
    print("You are selected for the first interview.")

    score = int(input("Enter candidate's first interview score: "))


    # Second condition: First Interview

    if score > 80:
        print("You are selected for the second interview.")

        second_score = int(
            input("Enter candidate's second interview score: ")
        )


        # Third condition: Second Interview

        if second_score > 90:
            print("You are selected for the final test.")

            is_smoker = input(
                "Enter candidate status (smoker/non smoker): "
            ).strip().lower()


            # Fourth condition: Non-Smoker

            if is_smoker == "non smoker":
                print("Congratulations! You are hired.")
            else:
                print("Sorry, only non-smokers are eligible.")

        else:
            print("You are not selected for the final test.")

    else:
        print("You are not selected for the second interview.")

else:
    print("Sorry, your CGPA is not adequate enough.")
    
    

'''

#এখানে decision tree হচ্ছে:
CGPA > 3.5?
│
├── No → ❌ Rejected
│
└── Yes
     │
     └── First Interview > 80?
          │
          ├── No → ❌ Rejected
          │
          └── Yes
               │
               └── Second Interview > 90?
                    │
                    ├── No → ❌ Rejected
                    │
                    └── Yes
                         │
                         └── Non-Smoker?
                              │
                              ├── No → ❌ Rejected
                              │
                              └── Yes → ✅ Hired 
                              '''

'''
এখানে সবচেয়ে গুরুত্বপূর্ণ concept

এই অংশটা:

if cgpa > 3.5:

    if score > 80:

        if second_score > 90:

            if is_smoker == "non smoker":
                print("Congratulations! You are hired.")

এটাই Nested If।
অর্থাৎ: প্রথম condition True হলে → দ্বিতীয় condition check করবে → সেটাও True হলে → তৃতীয় condition check করবে → তারপর চতুর্থ condition।
'''