resources=["coal", "iron", "gold", "coal", "timber", "coal"]
user_input=input()
if user_input in resources:
    user_input_count=resources.count(user_input)
    resourse_index=resources.index(user_input)
    print(f" Number of coal wagons: {user_input_count}")
    print(f"First coal wagon is at index: {resourse_index}")
else:
    print("Resource not in the list")