
def dynamic_Data_pipeline(dataset):
    parsed_data=list(map(
        lambda x:(
        x[0],
        float(x[1].split(":")[1]),
        float(x[2].split(":")[1])
        ),dataset
        ))
    filtered_data=list(filter(
        lambda x:x[1]<=1000.0 ,parsed_data
    ))
    mapped_data=list(map(
        lambda x:{
            "product":x[0],
            "Price":x[1],
            "Rating":x[2]
        },filtered_data
    ))
    sorted_data=sorted(
        mapped_data,
        key=lambda x:x["Rating"],
        reverse=True
    )
    return sorted_data
data_input = [
    ("Laptop", "Price: 1200", "Rating: 4.8"),
    ("Phone", "Price: 800", "Rating: 4.5"),
    ("Mouse", "Price: 25", "Rating: 4.7"),
    ("Charger", "Price: 15", "Rating: 4.2")
]
result=dynamic_Data_pipeline(data_input)
print(result)