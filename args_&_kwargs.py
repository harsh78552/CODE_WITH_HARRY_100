# def student_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)


def fun_args(normal, *anything_at_the_pace_of_args, **kwargs):  # *args
    print(normal)
    for item in anything_at_the_pace_of_args:
        print(
            item,
        )
    print("\n")
    for key, value in kwargs.items():
        print(f"{key} is {value}")


name = ["Harsh", "Happy", "Adarsh", "Aryan", "Pushkar", "The Programmer"]
normal = "I am a normal Argument."
Dictionary = {
    "Apple": "Fruit",
    "Monkey": "Mammals",
    "Crocodile": "Amphibians",
    "Tulsi": "Medicinal Plant",
}
fun_args(normal, *name, **Dictionary)
# student_name_print("Harsh", "Happy", "Adarsh", "Aryan", "Pushkar")
