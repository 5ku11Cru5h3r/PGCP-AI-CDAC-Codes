vip_queue=["Guido", "Esha", "Rajan", "Kishori"]

while True:
    guest_name=input("Enter the guest name")
    if guest_name=="exit":
        break
    if guest_name in vip_queue:
        vip_queue.remove(guest_name)
        vip_queue[0]=guest_name
        print(f'{guest_name} moved to the front')
        print(f'Current vip queue: {vip_queue}')
        
    else:
        print("Access denied!not in the vip list")


