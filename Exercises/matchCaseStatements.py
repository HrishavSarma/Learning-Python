# Match-case Statements(switch) -> An alternative to using many 'elif' statements
#                                  Execute some code if value matches a 'case'
#                                  Benefits : Cleaner and syntax more readable

# def day_of_week(day):
#     match day:
#         case 1:
#             return "Monday"
#         case 2:
#             return "Tuesday"
#         case 3:
#             return "Wednesday"
#         case 4:
#             return "Thursday"
#         case 5:
#             return "Friday"
#         case 6:
#             return "Saturday"
#         case 7:
#             return "Sunday"
#         case _:                         #"_" -> is a wild card
#             return "Not a valid day"
        
# print(day_of_week(7))

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:                         #"_" -> is a wild card
            return "Not a valid day"
        
print(is_weekend("Pizza"))