'''
5. News Feed — Latest 3 Headlines

Problem Statement:
• Given a list of headlines stored oldest-first.
• Slice the last 3 headlines into a variable called recent.
• Print the total headline count and recent count.
• Print each recent headline numbered and in title case.
• If total headlines are fewer than 3, print 'Not enough news yet'.

Acceptance Criteria:
• Use a negative slice headlines[-3:] for recent.
• Use len() for both counts.
• Access each item by index and apply .title().
• Use if/else on len(headlines) for the guard check.

Expected Output:
Total headlines: 5 | Showing: 3
1. New Ai Law Passed
2. Budget Cuts Announced
3. School Reform Bill
'''

headlines = [
           "weather alert issued",
           "japan's auto industry plots new road map",
           "new ai law passed",
           "budget cuts announced",
           "school reform bill"]

recent = headlines[-3:]


if len(headlines) <=3:
     print("Not enough news yet.")

else:     
     print("Total headlines:", len(headlines), "|showing:", len(recent))
     print("1.", recent[0].title())   
     print("2.", recent[1].title())
     print("3.", recent[2].title())

   
     
