import datetime
import random

# yusuf_employer = ""
# total_number_of_applications = 0

# while (yusuf_employer == "") or (total_number_of_applications < 1000):
#     print("Searching for job on job boards")
#     number_of_applications_today = random.randint(1, 10)
#     print(f"Applied to {number_of_applications_today} jobs today")
#     total_number_of_applications += number_of_applications_today
#     print(
# f"""The total number of jobs you've applied to since 
# you started searching is now {total_number_of_applications}"""
# )
#     print()

#     if total_number_of_applications > 100:
#         print(
# f"""You have applied to {total_number_of_applications} in total
# It is safe to say you have gotten a job now. 
# I would stop applying for jobs on your behalf now. Goodbye!"""
#         )
#         break
    # print("no_employer_yet")



lady_weight = 100
deadline = datetime.date(2025, 8, 11)
gym_days = 0
todays_date = datetime.datetime.now().date()

while lady_weight > 50:
    gym_days += 1
    print(f"Day {gym_days} of going to the gym.")   # go to the gym

    weight_lost_today = random.randint(1, 3)        # lose some kg per gym visit
    print(f"Welldone! You lost {weight_lost_today}kg today.")

    lady_weight -= weight_lost_today
    print(f"Your current weight is now {lady_weight}kg")

    todays_date = todays_date + datetime.timedelta(1)
    print(f"Today's date is now {todays_date}")

    if deadline == todays_date and lady_weight > 50:
        print(f"Sorry, you didn't meet the deadline for your weight goal.")
        break
